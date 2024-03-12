# CDK Construct Snippets for VS Code

[![Version](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cdk-snippets 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cdk-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cdk-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)

This extension adds L1 construct snippets from CDK into Visual Studio Code.

> [!TIP]
> If you're looking for expertise to elevate your cloud infrastructure, then don't hesitate to get in [touch with me](https://towardsthecloud.com/contact)!
>
> <details><summary>📚 <strong>Discover more about us</strong></summary>
>
> <br/>
>
> Towards the Cloud is a one-person agency with over 9 years of extensive hands-on experience in architecting and building highly scalable distributed systems on AWS Cloud using Infrastructure as Code for startups and enterprises.
>
> *Maximize your development speed by harnessing our expertise in crafting high-performance Cloud infrastructures.*
>
> #### Why Choose Towards the Cloud?
>
> - **Expertise in AWS CDK**: Leverage the full power of AWS Cloud Development Kit (AWS CDK) with our deep expertise. We architect and build infrastructure as code (IaC) solutions that are maintainable, scalable, and fully automated.
> - **Tailored Solutions**: Your business is unique, and so are your cloud needs. We provide personalized consultations and solutions tailored to perfectly align with your project requirements and business goals.
> - **Cost-Effective and Efficient**: Benefit from our streamlined processes and deep AWS knowledge to optimize costs without compromising on performance or security.
> - **One-on-One Attention**: As a one-person agency, Towards the Cloud guarantees you receive dedicated support and expertise directly from an AWS Cloud Engineer. This ensures high-quality deliverables and swift decision-making.<br/>
> - **Seamless CI/CD**: Empower your team to manage infrastructure changes confidently and efficiently through Pull Requests, leveraging the full power of GitHub Actions.
>
> <a href="https://towardsthecloud.com/contact"><img alt="Schedule introduction call" src="https://img.shields.io/badge/schedule%20introduction%20call-success.svg?style=for-the-badge"/></a>
> </details>

---

## New

- Added support for [Gitpod](https://github.com/dannysteenman/vscode-cloudformation-snippets/issues/14) by publishing this extension to the [Open VSX Registry](https://open-vsx.org/extension/dsteenman/cdk-snippets)

## Features

1. Supports all resources that are defined by CloudFormation in the form of L1 constructs in CDK
2. Triggers autocomplete by invoking `l1-<cloudformation-resource>`
3. The construct snippets are automatically updated every week after AWS updates their [CloudFormation Resource Specification.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
4. Has builtin support for placeholders. This means you can quickly jump from property to property in each resource by using `Tab`
5. The extension will show which property is required by adding a ```// required``` comment next to it.
6. The autocomplete prompt shows the matching CDK resource documentation URL in its description.

## Usage

* **Step 1.** Install [this extension](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
* **Step 2.** Start working in your CDK project (TypeScript)
* **Step 3.** Start adding L1 constructs in your code by using their prefix name e.g. ```l1-s3-bucket``` equals to L1 construct ```s3.CfnBucket```

![CDK Construct Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cdk-snippets/main/images/cdk-snippet-tutorial.gif)

> **Note:** Once you start typing a prefix (explained in step 3), the corresponding snippet shows up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 3).

---

## AWS CDK examples

If you'd like to learn more about AWS CDK, have a look at these [series of AWS CDK examples](https://towardsthecloud.com/category/infrastructure-as-code/aws-cdk) that I've pubished on my blog.

---

## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cdk-snippets/issues)


## Contributing

If you want to add more snippets or support another programming language, your contribution is more than welcome!

Review the [Contributing Guidelines](https://github.com/dannysteenman/vscode-cdk-snippets/blob/main/.github/CONTRIBUTING.md).

---

## Author

**[Danny Steenman](https://towardsthecloud.com)**

<p align="left">
  <a href="https://twitter.com/dannysteenman"><img src="https://img.shields.io/twitter/follow/dannysteenman?label=%40dannysteenman&style=social"></a>
</p>
