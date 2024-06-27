# AWS CDK Construct Snippets for VS Code

[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cdk-snippets?color=374151&label=Visual%20Studio%20Marketplace&labelColor=000&logo=visual-studio-code&logoColor=0098FF)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![](https://img.shields.io/visual-studio-marketplace/v/dannysteenman.cdk-snippets?color=374151&label=Open%20VSX%20Registry&labelColor=000&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyB2aWV3Qm94PSI0LjYgNSA5Ni4yIDEyMi43IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik0zMCA0NC4yTDUyLjYgNUg3LjN6TTQuNiA4OC41aDQ1LjNMMjcuMiA0OS40em01MSAwbDIyLjYgMzkuMiAyMi42LTM5LjJ6IiBmaWxsPSIjYzE2MGVmIi8+CiAgPHBhdGggZD0iTTUyLjYgNUwzMCA0NC4yaDQ1LjJ6TTI3LjIgNDkuNGwyMi43IDM5LjEgMjIuNi0zOS4xem01MSAwTDU1LjYgODguNWg0NS4yeiIgZmlsbD0iI2E2MGVlNSIvPgo8L3N2Zz4=&logoColor=0098FF)](https://open-vsx.org/extension/dannysteenman/cdk-snippets)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/dannysteenman.cdk-snippets 'Currently Installed')](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
[![Rating](https://img.shields.io/visual-studio-marketplace/stars/dannysteenman.cdk-snippets)](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)

This extension adds L1 Construct snippets from AWS CDK in Visual Studio Code.

> [!TIP]
> Struggling with AWS complexity or stuck on-premise? Let's transform your cloud journey.
>
> [Schedule a call with me](https://towardsthecloud.com/contact) to find out how I can enhance your existing AWS setup or guide your journey from on-premise to the Cloud.
>
> <details><summary>☁️ <strong>Discover more about my one-person business: Towards the Cloud</strong></summary>
>
> <br/>
>
> Hi, I'm Danny – AWS expert and founder of [Towards the Cloud](https://towardsthecloud.com). With over a decade of hands-on experience, I specialized myself in deploying well-architected, highly scalable and cost-effective AWS Solutions using Infrastructure as Code (IaC).
>
> #### When you work with me, you're getting a package deal of expertise and personalized service:
>
> - **AWS CDK Proficiency**: I bring deep AWS CDK knowledge to the table, ensuring your infrastructure is not just maintainable and scalable, but also fully automated.
> - **AWS Certified**: [Equipped with 7 AWS Certifications](https://www.credly.com/users/dannysteenman/badges), including DevOps Engineer & Solutions Architect Professional, to ensure best practices across diverse cloud scenarios.
> - **Tailored Solutions**: Understanding that no two businesses are alike, I Custom-fit cloud infrastructure for your unique needs.
> - **Cost-Effective**: I'll optimize your AWS spending without cutting corners on performance or security.
> - **Direct Access**: You work with me, not a team of managers. Expect quick decisions and high-quality work.
> - **Seamless CI/CD**: I'll set up smooth CI/CD processes using GitHub Actions, making changes a breeze through Pull Requests.
>
> *My mission is simple: I'll free you from infrastructure headaches so you can focus on what truly matters – your core business.*
>
> Ready to unlock the full potential of AWS Cloud?
>
> <a href="https://towardsthecloud.com/contact"><img alt="Schedule your call" src="https://img.shields.io/badge/schedule%20your%20call-success.svg?style=for-the-badge"/></a>
> </details>

---

## New in version 2!

- Added support for L1 constructs snippets in AWS CDK Python! Open up a CDK Python project and type `l1` to trigger the L1 construct autocomplete.

## Features

1. **Comprehensive Support**: Seamlessly integrates all CloudFormation resources as L1 constructs within CDK, ensuring you have access to the latest AWS offerings.
2. **Effortless Autocomplete**: Activate autocomplete with `l1-<cloudformation-resource>` to streamline your coding process.
3. **Weekly Updates**: Construct snippets are refreshed weekly in line with AWS's updates to their [CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html), keeping you on the cutting edge.
4. **Placeholder Support**: Navigate efficiently through resource properties using the `Tab` key, thanks to built-in placeholder functionality.
5. **Required Property Highlighting**: Easily identify mandatory properties, highlighted with a `// required` comment for your convenience.
6. **Documentation at Your Fingertips**: Access the corresponding CDK resource documentation directly from the autocomplete prompt, enriching your development experience.

## Usage

* **Step 1.** Install [this extension](https://marketplace.visualstudio.com/items?itemName=dannysteenman.cdk-snippets)
* **Step 2.** Start working in your CDK project (TypeScript or Python)
* **Step 3.** Start adding L1 constructs in your code by using their prefix name e.g. ```l1-s3-bucket``` equals to L1 construct ```s3.CfnBucket```

![CDK Construct Snippets example](https://raw.githubusercontent.com/dannysteenman/vscode-cdk-snippets/main/images/cdk-snippet-tutorial.gif)

> **Note:** Once you start typing a prefix (explained in step 3), the corresponding snippet shows up in the dropdown menu. If this doesn't happen automatically, press `ctrl + space` to invoke IntelliSense and search for the prefix of the resource type that you want to add (as listed in step 3).

---
## AWS CDK Examples

[Explore our AWS CDK Examples repository](https://github.com/dannysteenman/aws-cdk-examples) - a rich collection of TypeScript-based solutions that bring your cloud architecture to life. Crafted by a seasoned AWS professional.

---
## Support

If you have a feature request or an issue, please let me know on [Github](https://github.com/dannysteenman/vscode-cdk-snippets/issues)

## Author

Danny Steenman

[![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dannysteenman)
[![](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/dannysteenman)
[![](https://img.shields.io/badge/GitHub-2b3137?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dannysteenman)
