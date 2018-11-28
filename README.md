# cookiecutter-python-sam

In the same spirit as [cookiecutter-aws-sam-python](https://github.com/aws-samples/cookiecutter-aws-sam-python), but with a lot more opinions and therefore a lot less options. 😊 This is my personal, opinionated way of structuring python-based SAM apps.

## Features/Opinions

1. Lambda functions use python 3.6.
1. Lambda functions have X-Ray enabled.
1. pipenv is used for dependency management.
1. flake8 and pydocstyle static analysis checks are run on Lambda function code.
1. Lambda function code is unit tested with an enforced code line coverage minimum (85%).
1. cfn-lint is run to validate SAM template.
1. Lambda functions support configurable log level via template parameters and environment variables.
1. SAM CLI is used for package/local test/deploy.
1. Makefile is included with the following targets:
    1. `clean` - remove build artifacts.
    1. `bootstrap` - run once after initializing from cookiecutter to lock and install dependencies.
    1. `init` - used by CI build to install locked dependencies.
    1. `compile` - run linters on python code and SAM template.
    1. `build` - default target. Executes `compile` target.
    1. `package` - packages dependencies and uploads to S3, outputting a packaged template for deployment.

## Using the cookiecutter template

Here's my flow for starting a new SAM app. Note, I use a Macbook and have not tested this template on anything else. Theoretically, it should work on any *nix OS, maybe with minor tweaks.

1. Create a [new repository](https://github.com/new) in GitHub.
    1. Check the box to create a README.
    1. Do NOT have GitHub generate a .gitignore.
    1. DO have GitHub generate a LICENSE file.
1. Clone the new GitHub repo to your workspace.
1. cd into the cloned repo directory.
1. `sam init --location gh:jlhood/cookiecutter-python-sam`
    1. When prompted for project name, enter `tmp`
1. `mv tmp/* tmp/.* . && rmdir tmp`
1. `make bootstrap`
1. `git add .`
1. `git commit -m 'Initial app from template'`

Now start making changes and testing using `sam local` or deploy it like this:

1. `PACKAGE_BUCKET=my-bucket make package`
1. `sam deploy --template-file dist/packaged-template.yml --stack-name my-stack --capabilities CAPABILITY_IAM`

## CI Setup

I like to setup CI via AWS CodeBuild for my SAM apps to ensure all PRs can be packaged and built successfully before merging them to master. If you use this cookiecutter template, setting up CI is simple, because I've published an app to the AWS Serverless Application Repository (SAR) that creates a CI CodeBuild project specifically designed to work out of the box with this cookiecutter template. To install, go to [the app's SAR page](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:277187709615:applications~python-sam-codebuild-ci) and follow the instructions in the README.

## License Summary

This sample code is made available under the MIT license. See the LICENSE file.