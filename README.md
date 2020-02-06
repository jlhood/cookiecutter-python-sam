# cookiecutter-python-sam

In the same spirit as [cookiecutter-aws-sam-python](https://github.com/aws-samples/cookiecutter-aws-sam-python), but with a lot more opinions and therefore a lot less options. 😊 This is my personal, opinionated way of structuring python-based SAM apps.

## Features/Opinions

1. Lambda functions use python 3.8.
1. Lambda functions have X-Ray enabled.
1. pipenv is used for dependency management.
1. VS Code is used for editing.
1. flake8 and pydocstyle static analysis checks are run on Lambda function code.
1. Lambda function code is unit tested with an enforced code line coverage minimum (85%).
1. cfn-lint is run to validate the SAM template.
1. Lambda functions support runtime-configurable log level via template parameters and environment variables.
1. SAM CLI is used for build/package/local test/deploy/publish.
1. App is published to the AWS Serverless Application Repository (SAR).
1. Makefile is included with the following targets:
    1. `clean` - remove build artifacts.
    1. `bootstrap` - run once after initializing from cookiecutter to lock and install dependencies.
    1. `init` - used by CI build to install pre-requisites and locked dependencies.
    1. `compile` - run linters on python code and SAM template, run sam build.
    1. `build` - default target. Executes `compile` target.
    1. `package` - packages dependencies and uploads to S3, outputting a packaged template for deployment.
    1. `publish` - create/update corresponding app in AWS SAR.

## Using the cookiecutter template

**NOTE:** This template assumes you have SAM CLI installed and the `sam` command is on your path. SAM CLI installation instructions can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

Here's my flow for starting a new SAM app. Note, I use a Macbook and have not tested this template on anything else. Theoretically, it should work on any *nix OS, maybe with minor tweaks.

1. Create a [new repository](https://github.com/new) in GitHub.
    1. For the sake of this example, let's say you decided to name it my-sam-app.
    1. Do NOT have GitHub automatically create any files, e.g., README, etc.
1. cd to your workspace.
1. `sam init --location gh:jlhood/cookiecutter-python-sam`
    1. When prompted for project name, enter the name of your GitHub repo, e.g., my-sam-app.
    1. Choose 'y' for push_to_github.
    1. Answer remaining questions.
1. The cookiecutter template will automatically
    1. initialize the app from the template
    1. bootstrap dependencies
    1. initialize git and commit the app template changes
    1. push the changes to the GitHub remote repo
1. Add LICENSE file through GitHub UI
    1. Click "Create new file"
    1. Name the new file LICENSE
    1. Click "Choose a license template"
    1. Follow the steps to create and commit the LICENSE file from a template

Now you're ready to start making changes and testing using `sam local`:

1. `make`
1. `sam local invoke --no-event`

or deploy it like this:

1. `PACKAGE_BUCKET=my-bucket make package`
1. `sam deploy --template-file .aws-sam/packaged-template.yml --stack-name my-stack --capabilities CAPABILITY_IAM`

## CI Setup

I like to setup CI via AWS CodeBuild for my SAM apps to ensure all PRs can be packaged and built successfully before merging them to master. If you use this cookiecutter template, setting up CI is simple, because I've published an app to the AWS Serverless Application Repository (SAR) that creates a CI CodeBuild project specifically designed to work out of the box with this cookiecutter template. To install, go to [the app's SAR page](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:277187709615:applications~python-sam-codebuild-ci) and follow the instructions in the README.

## License Summary

This sample code is made available under the MIT license. See the LICENSE file.
