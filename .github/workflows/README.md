# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated testing and code quality checks.

## Current Workflow

### 🧪 `python-ci.yml` - Continuous Integration

**Triggers:**
- Push to `main` branch
- Pull requests to `main` branch  
- Manual dispatch

**What it does:**

1. **Environment Setup:**
   - Sets up Python 3.13
   - Installs project dependencies and dev tools
   - Configures pip cache for faster builds

2. **Code Quality Checks:**
   - **Linting**: Runs Ruff to check code style and common issues
   - **Formatting**: Validates code formatting with Black
   - **Type Checking**: Performs static type analysis with pyrefly
   - **Testing**: Executes test suite with pytest and generates coverage reports

3. **Coverage Reporting:**
   - Uploads coverage data to Codecov for tracking test coverage over time

4. **Auto-Tagging (main branch only):**
   - Extracts version from `pyproject.toml`
   - Compares with latest Git tag
   - Creates new tag if version is newer
   - **Note**: This only runs on push to `main` branch, NOT on pull requests

## Setup Instructions

### 1. Basic Repository Setup

The CI workflow will run automatically on pushes and PRs. No additional setup is required for basic functionality.

### 2. Codecov Integration (Optional)

To see coverage reports and trends:

1. Sign up for a free account at [codecov.io](https://codecov.io/)
2. Connect your GitHub repository to Codecov
3. Coverage reports will be automatically uploaded after each CI run

### 3. Local Development

To run the same checks locally before pushing:

```bash
# Install dependencies
pip install -e .[dev]

# Run linting
ruff check .

# Check formatting
black --check .

# Run type checking
pyrefly check

# Run tests with coverage
pytest --cov=generatecv
```

### Understanding the CI Process

### Workflow Stages

```mermaid
graph TD
    A[Code Push/PR] --> B[Setup Python 3.13]
    B --> C[Install Dependencies]
    C --> D[Lint with Ruff]
    D --> E[Check Formatting with Black]
    E --> F[Type Check with pyrefly]
    F --> G[Run Tests with pytest]
    G --> H[Generate Coverage Report]
    H --> I[Upload to Codecov]
    I --> J{All Checks Pass?}
    J -->|No| L[❌ CI Failed]
    J -->|Yes| M{Push to main?}
    M -->|No (PR)| K[✅ CI Success]
    M -->|Yes| N[Check Version in pyproject.toml]
    N --> O{Version > Latest Tag?}
    O -->|No| P[Skip Tagging]
    O -->|Yes| Q[Create & Push Tag]
    Q --> K
    P --> K
```

### What Each Tool Does

- **Ruff**: Fast Python linter that checks for code style, common bugs, and best practices
- **Black**: Automatic code formatter that ensures consistent code style
- **pyrefly**: Static type checker that catches type-related errors
- **pytest**: Test runner that executes your test suite and measures code coverage

## Troubleshooting Common Issues

### CI Fails on Linting
```bash
# Fix automatically where possible
uv run ruff check --fix .

# Check what needs manual fixing
uv run ruff check .
```

### CI Fails on Formatting
```bash
# Auto-format code
uv run black .

# Check what would be changed
uv run black --check --diff .
```

### CI Fails on Type Checking
```bash
# Run type checker locally
uv run pyrefly check

# Check specific files
uv run pyrefly check src/generatecv/
```

### CI Fails on Tests
```bash
# Run tests locally
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test
uv run pytest tests/test_specific.py
```

## Auto-Tagging Explained

### How Auto-Tagging Works

1. **Trigger**: Only runs when code is pushed to `main` branch (not on PRs)
2. **Version Check**: Reads version from `pyproject.toml`
3. **Comparison**: Compares with latest Git tag
4. **Tag Creation**: Creates new tag only if version is newer

### Example Scenarios

**Scenario 1: Version Bump**
```
Latest tag: v0.0.0
pyproject.toml version: 0.0.1
Result: ✅ Creates tag v0.0.1
```

**Scenario 2: No Version Change**
```
Latest tag: v0.0.1
pyproject.toml version: 0.0.1
Result: ⚠️ Skips tagging (same version)
```

**Scenario 3: Pull Request**
```
Event: Pull request to main
Result: 🚫 Auto-tag job doesn't run (PR only runs tests)
```

### Why No PR for Auto-Tag?

Auto-tagging happens **after** your code is already merged to main:

1. You create a PR with version bump
2. CI runs tests on the PR (no tagging)
3. PR gets merged to main
4. CI runs again on main branch
5. Auto-tag job creates the tag

## Best Practices

### Before Committing
1. Run tests locally: `uv run pytest`
2. Check formatting: `uv run black --check .`
3. Run linter: `uv run ruff check .`
4. Verify types: `uv run pyrefly check`

### Pull Request Guidelines
- Ensure all CI checks pass
- Maintain or improve test coverage
- Write clear commit messages
- Keep changes focused and atomic

### Version Management
- Update version in `pyproject.toml` when ready to release
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Only merge version bumps when ready to tag

### Code Quality Standards
- Follow PEP 8 style guidelines (enforced by Black and Ruff)
- Add type hints to new code (checked by pyrefly)
- Write tests for new functionality
- Aim for high test coverage (visible in Codecov reports)

## Monitoring CI Health

- **Status**: Check the Actions tab in GitHub for recent CI runs
- **Coverage**: Review coverage trends in Codecov dashboard
- **Performance**: Monitor CI run times to catch performance regressions

The CI workflow helps maintain code quality and catches issues early in the development process. All checks must pass before code can be merged to the main branch.