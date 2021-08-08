# CDK Construct Snippets for VS Code

[![Version](https://vsmarketplacebadge.apphb.com/version/dsteenman.cdk-snippets.svg 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cdk-snippets)
[![Installs](https://vsmarketplacebadge.apphb.com/installs-short/dsteenman.cdk-snippets.svg 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dsteenman.cdk-snippets)
[![Rating](https://vsmarketplacebadge.apphb.com/rating-star/dsteenman.cdk-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=dsteenman.cdk-snippets)

This extension adds L1 construct snippets from CDK into Visual Studio Code.

## Features

1. Supports all resources that are defined by CloudFormation in the form of L1 constructs in CDK
2. Triggers autocomplete by invoking `l1-<cloudformation-resource>`
3. The construct snippets are automatically updated every week after AWS updates their [CloudFormation Resource Specification.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
4. Has builtin support for placeholders. This means you can quickly jump from property to property in each resource by using `Tab`
5. The extension will show which property is required by adding a ```// required``` comment next to it.
6. The autocomplete prompt shows the matching CDK resource documentation URL in its description.

## Usage

* **Step 1.** Install [this extension](https://marketplace.visualstudio.com/items?itemName=dsteenman.cdk-snippets)
* **Step 2.** Start working in your CDK project (TypeScript)
* **Step 3.** Start adding L1 constructs in your code by using their prefix name e.g. ```l1-s3-bucket``` equals to L1 construct ```s3.CfnBucket```

![CDK Construct Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cdk-snippets/main/images/cdk-snippet-tutorial.gif)

> **Note:** Once you start typing a prefix (explained in step 3), the corresponding snippet shows up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 3).

---

## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cdk-snippets/issues)


## Contributing

If you want to add more snippets or support another programming language, your contribution is more than welcome!

Review the [Contributing Guidelines](https://github.com/dannysteenman/vscode-cdk-snippets/blob/main/.github/CONTRIBUTING.md).

---

## Author

**[Danny Steenman](https://dannys.cloud)**

<p align="left">
  <a href="https://dannys.cloud/twitter"><img src="https://img.shields.io/twitter/follow/dannysteenman?label=%40dannysteenman&style=social"></a>
</p>
