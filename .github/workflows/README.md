# GitHub Actions Workflows

This directory contains GitHub Actions workflows to automate testing, code quality checks, and package publishing.

## Workflows

### `python-ci.yml`

This workflow runs on every push to the main branch and on pull requests:

- Sets up Python 3.13 (as specified in the project requirements)
- Installs the package and development dependencies
- Runs code quality checks:
  - Linting with Ruff
  - Formatting checks with Black
  - Type checking with mypy
- Runs tests with pytest and collects code coverage
- Uploads coverage reports to Codecov

### `python-publish.yml`

This workflow builds and publishes the package to PyPI when:
- A new GitHub release is created
- The workflow is manually triggered with a version number

## Setting Up Secrets

For the PyPI publishing workflow, you'll need to set up the following:

1. Create a PyPI API token at [pypi.org](https://pypi.org/manage/account/token/)
2. Add the token to your GitHub repository:
   - Go to Settings > Secrets and variables > Actions
   - Create a secret named `PYPI_API_TOKEN` with your token as the value

## Manual Triggers

The publishing workflow can be triggered manually from the "Actions" tab in your GitHub repository. When doing so, you'll be prompted to input the version number for the release.

## Code Coverage

To see code coverage reports, you'll need to:
1. Sign up for a free account at [codecov.io](https://codecov.io/)
2. Connect your GitHub repository to Codecov