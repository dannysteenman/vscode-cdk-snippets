import argparse
import json
import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List

import requests

CFN_RESOURCE_SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
MAX_DEPTH = 10
MAX_LINES = 400
VALUE_TYPE_MAP = {
    "Boolean": "bool",
    "Double": "float",
    "Integer": "int",
    "Json": "dict",
    "Long": "int",
    "String": "str",
    "Timestamp": "datetime",
}

log_lock = threading.Lock()


def safe_print(*args, **kwargs):
    with log_lock:
        print(*args, **kwargs)


class ResourceParser:
    def __init__(self, max_depth: int, output_format: str):
        self.counter = [1]
        self.nested_types = set()
        self.max_depth = max_depth
        self.output_format = output_format
        self.resource_type = ""

    def parse_body(
        self, resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        self.resource_type = resource_type
        body = self._init_body(resource_type)
        self.counter[0] = 1
        parse_method = getattr(self, f"_parse_body_{self.output_format}")
        return parse_method(body, resource_properties, resource_type, response_data)

    def _init_body(self, resource_type: str) -> List[str]:
        service, resource = resource_type.split("::")[-2:]
        if self.output_format == "typescript":
            return [f"new {service.lower()}.Cfn{resource}(this, '${{1:id}}', {{"]
        elif self.output_format == "python":
            return [f'aws_{service.lower()}.Cfn{resource}(self, "${{1:id}}",']

    def _parse_body_typescript(
        self, body: List[str], resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        camel_case_properties = {self._format_property_name(k, True): v for k, v in resource_properties.items()}
        self._parse_properties(body, camel_case_properties, resource_type, response_data, 1, is_typescript=True)
        body.append("})")
        return body

    def _parse_body_python(
        self, body: List[str], resource_properties: Dict[str, Any], resource_type: str, response_data: Dict[str, Any]
    ) -> List[str]:
        snake_case_properties = {self._format_property_name(k, False): v for k, v in resource_properties.items()}
        self._parse_properties(body, snake_case_properties, resource_type, response_data, 1, is_typescript=False)
        body.append(")")
        return body

    def _parse_properties(
        self,
        body: List[str],
        properties: Dict[str, Any],
        resource_type: str,
        response_data: Dict[str, Any],
        depth: int,
        is_typescript: bool,
    ):
        for property_name, property_info in sorted(properties.items()):
            required = property_info.get("Required", False)
            item_type = self._get_item_type(property_info)
            indent = "  " * depth if is_typescript else " " * (depth * 4)

            if "Type" in property_info:
                type_handlers = {
                    "List": self._handle_list_type,
                    "Map": self._handle_map_type,
                }
                handler = type_handlers.get(property_info["Type"], self._handle_other_type)
                handler(
                    body, property_name, property_info, resource_type, response_data, required, depth, is_typescript
                )
            else:
                self._handle_simple_type(body, property_name, item_type, required, depth, is_typescript)

    def _handle_simple_type(
        self, body: List[str], property_name: str, item_type: str, required: bool, depth: int, is_typescript: bool
    ):
        indent = "  " * depth if is_typescript else " " * (depth * 4)
        value = self._get_value_type(item_type, is_typescript)
        comment = " // Required" if is_typescript else " # Required" if required else ""

        if is_typescript:
            body.append(f"{indent}{property_name}: {value},{comment}")
        else:
            if item_type == "String":
                body.append(f'{indent}{property_name}="{value}",{comment}')
            else:
                body.append(f"{indent}{property_name}={value},{comment}")

    def _handle_list_type(
        self, body, property_name, property_info, resource_type, response_data, required, depth, is_typescript
    ):
        indent = "  " * depth if is_typescript else " " * (depth * 4)
        comment = " // Required" if is_typescript else " # Required" if required else ""

        if property_name == "tags":
            if is_typescript:
                body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}: [{comment}")
                body.append(f"{indent}  {{")
            else:
                body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}=[{comment}")
                body.append(f"{indent}    cdk.CfnTag(")
            self._parse_properties(
                body,
                {
                    "key": {"PrimitiveType": "String", "Required": True},
                    "value": {"PrimitiveType": "String", "Required": True},
                },
                resource_type,
                response_data,
                depth + 2 if is_typescript else depth + 1,
                is_typescript,
            )
            if is_typescript:
                body.append(f"{indent}  }}")
            else:
                body.append(f"{indent}    ),")
            body.append(f"{indent}],")
            return

        if is_typescript:
            body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}: [{comment}")
        else:
            body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}=[{comment}")

        if "ItemType" in property_info:
            nested_properties = self._get_nested_properties(property_info["ItemType"], resource_type, response_data)
            if is_typescript:
                body.append(f"{indent}  {{")
            else:
                service = resource_type.split("::")[1].lower()
                type_name = property_info["ItemType"]
                body.append(f"{indent}    aws_{service}.Cfn{resource_type.split('::')[2]}.{type_name}Property(")
            self._parse_properties(
                body,
                nested_properties,
                resource_type,
                response_data,
                depth + 2 if is_typescript else depth + 1,
                is_typescript,
            )
            if is_typescript:
                body.append(f"{indent}  }}")
            else:
                body.append(f"{indent}    ),")
        elif "PrimitiveItemType" in property_info:
            inner_indent = "  " * (depth + 1) if is_typescript else " " * ((depth + 1) * 4)
            body.append(
                f"{inner_indent}{self._get_value_type(property_info['PrimitiveItemType'], is_typescript, in_list=True)},"
            )
        body.append(f"{indent}],")

    def _handle_map_type(
        self, body, property_name, property_info, resource_type, response_data, required, depth, is_typescript
    ):
        indent = "  " * depth if is_typescript else " " * (depth * 4)
        if is_typescript:
            body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}: {{")
        else:
            body.append(f"{indent}{self._format_property_name(property_name, is_typescript)}= {{")
        body.append(f"{indent}}},")

    def _handle_other_type(
        self, body, property_name, property_info, resource_type, response_data, required, depth, is_typescript
    ):
        indent = "  " * depth if is_typescript else " " * (depth * 4)
        comment = " // Required" if is_typescript else " # Required" if required else ""

        if is_typescript:
            body.append(f"{indent}{property_name}: {{")
        else:
            service = resource_type.split("::")[1].lower()
            resource = resource_type.split("::")[2]
            type_name = property_info["Type"]
            body.append(f"{indent}{property_name}=aws_{service}.Cfn{resource}.{type_name}Property({comment}")

        self._parse_properties(
            body,
            self._get_nested_properties(property_info["Type"], resource_type, response_data),
            resource_type,
            response_data,
            depth + 1,
            is_typescript,
        )

        if is_typescript:
            body.append(f"{indent}}},")
        else:
            body.append(f"{indent}),")

    def _get_nested_properties(self, item_type, resource_type, response_data):
        resource_property_name = f"{resource_type}.{item_type}"
        nested_properties = response_data.get("PropertyTypes", {}).get(resource_property_name, {}).get("Properties", {})
        return {
            self._format_property_name(k, self.output_format == "typescript"): v for k, v in nested_properties.items()
        }

    def _get_value_type(self, item, is_typescript, in_list=False):
        self.counter[0] += 1
        if is_typescript:
            if item == "String":
                return f"'${{{self.counter[0]}:str}}'"
            elif item in ["Integer", "Double", "Long"]:
                return f"${{{self.counter[0]}:0}}"
            elif item == "Boolean":
                return f"${{{self.counter[0]}:false}}"
            elif item == "Timestamp":
                return f"'${{{self.counter[0]}:new Date()}}'"
            elif item == "Json":
                return f"${{{self.counter[0]}:{{}}}}"
            else:
                return f"'${{{self.counter[0]:}}}'"
        else:
            if item == "String":
                return f'"${{{self.counter[0]}:str}}"' if in_list else f"${{{self.counter[0]}:str}}"
            elif item in ["Integer", "Double", "Long"]:
                return f"${{{self.counter[0]}:0}}"
            elif item == "Boolean":
                return f"${{{self.counter[0]}:False}}"
            elif item == "Timestamp":
                return f"${{{self.counter[0]}:datetime.now()}}"
            elif item == "Json":
                return f"${{{self.counter[0]}:{{}}}}"
            else:
                return f'"${{{self.counter[0]:}}}"'

    @staticmethod
    def _get_item_type(resource_property: Dict[str, Any]) -> str:
        return resource_property.get(
            "PrimitiveItemType", resource_property.get("PrimitiveType", resource_property.get("ItemType"))
        )

    @staticmethod
    def _format_property_name(name: str, is_typescript: bool) -> str:
        if is_typescript:
            return name[0].lower() + name[1:]
        else:
            s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
            return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process CloudFormation Resource Specification")
    parser.add_argument("--local", dest="local_path", help="Path to local JSON resource specification file (optional)")
    parser.add_argument(
        "--format",
        dest="output_format",
        choices=["typescript", "python"],
        default="typescript",
        help="Output format for the snippets (default: %(default)s)",
    )
    return parser.parse_args()


def get_resource_spec(local_path: str = None) -> Dict[str, Any]:
    if local_path:
        with open(os.path.abspath(local_path), "r") as f:
            return json.load(f)
    else:
        response = requests.get(CFN_RESOURCE_SPEC_URL)
        response.raise_for_status()
        return response.json()


def fetch_description(resource_type: Dict[str, Any], resource_type_str: str, output_format: str) -> List[str]:
    service, resource = resource_type_str.split("::")[-2:]
    cdk_l1_construct = f"{service.lower()}.Cfn{resource}"

    if output_format == "typescript":
        doc_url = f"https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_{service.lower()}.Cfn{resource}.html"
    elif output_format == "python":
        doc_url = f"https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_{service.lower()}/Cfn{resource}.html"
    else:
        doc_url = ""

    description = [
        f"Construct: {cdk_l1_construct}",
        f"Documentation: {doc_url}",
    ]

    if "Attributes" in resource_type:
        description.append("Attributes:")
        for attribute in resource_type["Attributes"]:
            description.append(f"  {attribute}")

    return description


def process_resource_type(
    resource_type: str, resource_data: Dict[str, Any], response_data: Dict[str, Any], output_format: str
) -> tuple:
    service, resource = resource_type.split("::")[-2:]
    cdk_l1_construct = f"{service.lower()}.Cfn{resource}"
    description = fetch_description(resource_data, resource_type, output_format)
    resource_properties = resource_data.get("Properties", {})

    parser = ResourceParser(MAX_DEPTH, output_format)
    updated_body = parser.parse_body(resource_properties, resource_type, response_data)

    line_count = len(updated_body)
    safe_print(f"Resource type {resource_type} has {line_count} lines")

    safe_print(f"Finished processing {resource_type}")
    return cdk_l1_construct, {
        "body": updated_body,
        "description": description,
        "prefix": f"l1-{service.lower()}-{resource.lower()}",
        "scope": output_format,
    }


def create_cfn_snippet(
    cloudformation_resource_spec: Dict[str, Any], local_path: str = None, output_format: str = "typescript"
) -> None:
    output = {}
    resource_types = cloudformation_resource_spec["ResourceTypes"]

    safe_print(f"Total number of resource types: {len(resource_types)}")

    with ThreadPoolExecutor() as executor:
        future_to_resource = {
            executor.submit(
                process_resource_type, resource_type, resource_data, cloudformation_resource_spec, output_format
            ): resource_type
            for resource_type, resource_data in resource_types.items()
        }

        for future in as_completed(future_to_resource):
            resource_type = future_to_resource[future]
            try:
                result = future.result()
                output[resource_type] = result[1]
            except Exception as exc:
                safe_print(f"{resource_type} generated an exception: {exc}")

    output_file_name = f"cdk-l1-constructs-{output_format}.json"
    snippet_directory = f"{os.getcwd()}/snippets"
    output_file_path = os.path.join(snippet_directory, output_file_name)

    os.makedirs(snippet_directory, exist_ok=True)

    safe_print(f"Saving snippets in: {output_file_path}")
    with open(output_file_path, "w") as file:
        json.dump(output, file, sort_keys=True, indent=4)


def main():
    args = parse_arguments()
    cloudformation_resource_spec = get_resource_spec(args.local_path)
    create_cfn_snippet(cloudformation_resource_spec, args.local_path, args.output_format)


if __name__ == "__main__":
    main()
