# AWS CDK Construct Snippets for VS Code

[![Version](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cdk-snippets 'Current Release')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cdk-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cdk-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)

This extension adds L1 Construct snippets from AWS CDK in Visual Studio Code.

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
## Features

1. **Comprehensive Support**: Seamlessly integrates all CloudFormation resources as L1 constructs within CDK, ensuring you have access to the latest AWS offerings.
2. **Effortless Autocomplete**: Activate autocomplete with `l1-<cloudformation-resource>` to streamline your coding process.
3. **Weekly Updates**: Construct snippets are refreshed weekly in line with AWS's updates to their [CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html), keeping you on the cutting edge.
4. **Placeholder Support**: Navigate efficiently through resource properties using the `Tab` key, thanks to built-in placeholder functionality.
5. **Required Property Highlighting**: Easily identify mandatory properties, highlighted with a `// required` comment for your convenience.
6. **Documentation at Your Fingertips**: Access the corresponding CDK resource documentation directly from the autocomplete prompt, enriching your development experience.

## Usage

* **Step 1.** Install [this extension](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
* **Step 2.** Start working in your CDK project (TypeScript)
* **Step 3.** Start adding L1 constructs in your code by using their prefix name e.g. ```l1-s3-bucket``` equals to L1 construct ```s3.CfnBucket```

![CDK Construct Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cdk-snippets/main/images/cdk-snippet-tutorial.gif)

> **Note:** Once you start typing a prefix (explained in step 3), the corresponding snippet shows up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 3).

---
## AWS CDK examples

Looking to level up your infrastructure-as-code skills with the power of AWS CDK? Check out the [AWS CDK Examples](https://github.com/dannysteenman/aws-cdk-examples) repository - a treasure trove of TypeScript-based solutions crafted by a seasoned cloud developer.

---
## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cdk-snippets/issues)

## Author

**[Danny Steenman](https://github.com/dannysteenman)**

<p align="left">
  <a href="https://twitter.com/dannysteenman"><img src="https://img.shields.io/twitter/follow/dannysteenman?label=%40dannysteenman&style=social"></a>
</p>
