# Setup Instructions for generatecv

This document provides step-by-step instructions to set up all the workflows and integrations for the generatecv project.

## 🚀 PyPI Publishing Setup (OIDC Trusted Publishing)

### 1. PyPI Account Setup

1. **Create PyPI Account**:
   - Go to [pypi.org](https://pypi.org/account/register/)
   - Create an account with your email

2. **Setup Trusted Publishing**:
   - Go to [PyPI Publishing Settings](https://pypi.org/manage/account/publishing/)
   - Click "Add a new pending publisher"
   - Fill in the details:
     - **PyPI project name**: `generatecv`
     - **Owner**: `yantology`
     - **Repository name**: `generatecv`
     - **Workflow filename**: `publish.yml`
     - **Environment name**: `pypi`

3. **Optional: Setup TestPyPI**:
   - Go to [test.pypi.org](https://test.pypi.org/account/register/)
   - Repeat the same process for testing
   - Use environment name: `testpypi`

### 2. GitHub Repository Environments

1. **Go to Repository Settings**:
   - Navigate to `Settings` → `Environments`

2. **Create PyPI Environment**:
   - Click "New environment"
   - Name: `pypi`
   - **Protection rules** (recommended):
     - ✅ Required reviewers: `yantology`
     - ✅ Deployment branches: Selected branches → `main`

3. **Create TestPyPI Environment** (optional):
   - Name: `testpypi`
   - Same protection rules as above

### 3. GitHub Repository Settings

1. **Enable GitHub Pages**:
   - Go to `Settings` → `Pages`
   - Source: `Deploy from a branch`
   - Branch: `gh-pages` (will be created automatically)

2. **Repository Secrets** (if needed):
   - Go to `Settings` → `Secrets and variables` → `Actions`
   - Add `CODECOV_TOKEN` (optional, for better coverage reporting)

## 🔒 Security Integration Setup

### 1. Codecov Integration (Optional)

1. **Sign up for Codecov**:
   - Go to [codecov.io](https://codecov.io/)
   - Sign up with your GitHub account
   - Add your repository

2. **Get Codecov Token**:
   - In Codecov dashboard, go to repository settings
   - Copy the upload token
   - Add it as `CODECOV_TOKEN` in GitHub Secrets

### 2. Repository Labels

Create these labels in your repository (`Issues` → `Labels`):

**Priority Labels:**
- `high-priority` (color: `#d73a4a`)
- `medium-priority` (color: `#fbca04`)
- `low-priority` (color: `#0075ca`)

**Type Labels:**
- `security-scan` (color: `#d73a4a`)
- `security-alert` (color: `#b60205`)
- `automated` (color: `#7057ff`)
- `needs-triage` (color: `#fbca04`)
- `weekly-summary` (color: `#0075ca`)

**Size Labels:**
- `size/XS` (color: `#3cbf00`)
- `size/S` (color: `#5cbf00`)
- `size/M` (color: `#fbca04`)
- `size/L` (color: `#ff9500`)
- `size/XL` (color: `#d73a4a`)

**Category Labels:**
- `dependencies` (color: `#0366d6`)
- `github-actions` (color: `#000000`)
- `documentation` (color: `#0075ca`)
- `breaking-change` (color: `#b60205`)
- `tests` (color: `#0e8a16`)

## 📚 Documentation Setup

### 1. Enable GitHub Pages

1. **Repository Settings**:
   - Go to `Settings` → `Pages`
   - Source: `Deploy from a branch`
   - Branch: `gh-pages` / `(root)`

2. **First Run**:
   - Push to main branch to trigger docs build
   - Documentation will be available at: `https://yantology.github.io/generatecv`

## 🔧 Development Environment Setup

### 1. Local Development

```bash
# Clone the repository
git clone https://github.com/yantology/generatecv.git
cd generatecv

# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --dev

# Install additional dev tools
uv sync --group docs --group security
```

### 2. Pre-commit Setup (Optional)

```bash
# Install pre-commit hooks
uv add --dev pre-commit
uv run pre-commit install

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.8
    hooks:
      - id: ruff
        args: [--fix]
EOF
```

## 🚦 Testing the Setup

### 1. Test Workflows Locally

```bash
# Run tests
uv run pytest

# Run linting
uv run ruff check .

# Run formatting check
uv run black --check .

# Run type checking
uv run pyrefly check

# Run security scanning
uv run bandit -r src/
uv run safety check

# Build documentation
uv run mkdocs build

# Build package
uv build
```

### 2. Test PyPI Publishing

1. **Test with TestPyPI first**:
   - Create a test release in GitHub
   - Use workflow dispatch with TestPyPI option
   - Verify package appears on test.pypi.org

2. **Production Release**:
   - Create a proper GitHub Release
   - Verify package publishes to PyPI

## 📋 Verification Checklist

After setup, verify these are working:

### CI/CD Pipeline:
- [ ] ✅ Multi-platform tests pass
- [ ] ✅ Security scans run without issues
- [ ] ✅ Documentation builds successfully
- [ ] ✅ Package builds without errors
- [ ] ✅ Auto-tagging works on version bump

### Integrations:
- [ ] ✅ PyPI publishing environment configured
- [ ] ✅ GitHub Pages shows documentation
- [ ] ✅ Codecov reports coverage (if enabled)
- [ ] ✅ Dependabot creates PRs for updates
- [ ] ✅ Auto-labeling works on new issues/PRs

### Security:
- [ ] ✅ Security scans create issues when problems found
- [ ] ✅ Vulnerability detection works
- [ ] ✅ Code security analysis runs

## 🎯 Release Process

When you're ready to release:

1. **Update version** in `pyproject.toml`
2. **Commit and push** to main branch
3. **Create GitHub Release**:
   - Go to Releases → Draft a new release
   - Create tag: `v0.0.2` (matching pyproject.toml version)
   - Generate release notes automatically
   - Publish release
4. **Verify**:
   - Check Actions tab for workflow runs
   - Verify package appears on PyPI
   - Check documentation is updated

## 🆘 Troubleshooting

### Common Issues:

1. **PyPI Publishing Fails**:
   - Verify environment name matches exactly: `pypi`
   - Check PyPI trusted publisher settings
   - Ensure version in pyproject.toml is newer than last published

2. **Security Scans Fail**:
   - Update dependencies to fix vulnerabilities
   - Review and fix code security issues flagged by Bandit

3. **Documentation Build Fails**:
   - Check mkdocs.yml syntax
   - Ensure all referenced files exist
   - Verify Python imports work

4. **Tests Fail on Different Platforms**:
   - Check for platform-specific code
   - Verify file path handling (Windows vs Unix)
   - Review dependency compatibility

For more help, create an issue in the repository with the `question` label.