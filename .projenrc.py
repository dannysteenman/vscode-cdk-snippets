from projen.python import PythonProject

project = PythonProject(
    author_email="danny.steenman@icloud.com",
    author_name="Danny Steenman",
    module_name="vscode_cdk_snippets",
    name="vscode-cdk-snippets",
    version="0.1.0",
    deps=["feedparser", "gitchangelog", "pystache", "requests", "wheel"],
    dev_deps=["requests"],
)

project.add_git_ignore("*.vsix")
project.add_git_ignore(".mypy_cache")
project.synth()
