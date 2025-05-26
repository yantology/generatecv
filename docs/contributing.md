# Contributing

We welcome contributions to generatecv! This document provides guidelines for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.9 or higher or ++++
- [uv](https://docs.astral.sh/uv/) package manager

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/yourusername/generatecv.git
cd generatecv
```

3. Install dependencies using uv:

```bash
uv sync --dev
```

4. Create a virtual environment and activate it:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Development Workflow

### Making Changes

1. Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the coding standards below

3. Write or update tests for your changes

4. Run the test suite to ensure everything works:

```bash
uv run pytest
```

5. Run code quality checks:

```bash
uv run ruff check .
uv run ruff format .
uv run pyright
```

### Code Quality Standards

We maintain high code quality standards using several tools:

#### Code Formatting
- **Ruff**: For code formatting and import sorting
- Run `uv run ruff format .` to format your code
- Run `uv run ruff check .` to check for issues

#### Type Checking
- **Pyright**: For static type checking
- Run `uv run pyright` to check types
- Add type hints to all new functions and classes

#### Testing
- **pytest**: For running tests
- Aim for high test coverage (>90%)
- Write unit tests for all new functionality
- Include integration tests where appropriate

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=generatecv

# Run specific test file
uv run pytest tests/test_specific.py

# Run tests in watch mode during development
uv run pytest-watch
```

### Documentation

- Update documentation for any new features
- Use docstrings with Google style formatting
- Update the changelog for significant changes
- Build documentation locally to test:

```bash
uv run mkdocs serve
```

## Contribution Guidelines

### Pull Request Process

1. Ensure your code passes all tests and quality checks
2. Update documentation as needed
3. Add entries to CHANGELOG.md for significant changes
4. Create a pull request with:
   - Clear title and description
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

### Commit Message Convention

We follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

Examples:
```
feat(templates): add new minimal template
fix(pdf): resolve font rendering issue
docs(api): update CV class documentation
```

### Code Style Guidelines

#### Python Code Style
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Keep functions small and focused
- Add docstrings to all public functions and classes
- Use type hints consistently

#### Docstring Format
Use Google style docstrings:

```python
def create_cv(data: dict, template: str = "modern") -> CV:
    """Create a new CV instance.

    Args:
        data: Dictionary containing CV data
        template: Template name to use (default: "modern")

    Returns:
        A new CV instance

    Raises:
        ValidationError: If data validation fails
        TemplateError: If template is not found

    Example:
        >>> cv = create_cv({"personal": {"name": "John Doe"}})
        >>> cv.save("cv.pdf")
    """
```

## Project Structure

```
generatecv/
├── src/
│   └── generatecv/
│       ├── __init__.py
│       ├── core/           # Core CV functionality
│       ├── templates/      # CV templates
│       ├── exporters/      # Output format exporters
│       └── utils/          # Utility functions
├── tests/
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── fixtures/          # Test data
├── docs/                  # Documentation
├── examples/              # Usage examples
└── scripts/               # Development scripts
```

## Types of Contributions

### Bug Reports

When filing a bug report, please include:
- Python version and operating system
- generatecv version
- Minimal code example that reproduces the issue
- Expected vs actual behavior
- Error messages and stack traces

### Feature Requests

For feature requests, please:
- Describe the feature and its use case
- Explain why it would be valuable
- Consider if it fits the project scope
- Propose an implementation approach if possible

### Code Contributions

We welcome contributions in these areas:
- Bug fixes
- New CV templates
- Output format support
- Performance improvements
- Documentation improvements
- Test coverage improvements

## Release Process

Releases are managed by maintainers and follow semantic versioning:
- Major version: Breaking changes
- Minor version: New features (backward compatible)
- Patch version: Bug fixes

## Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment:
- Be respectful and professional
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect different viewpoints and experiences

### Getting Help

- Check existing issues and documentation first
- Use GitHub Discussions for questions
- Join our community chat (link in README)
- Tag maintainers if you need urgent help

## Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub contributor graphs

## License

By contributing to generatecv, you agree that your contributions will be licensed under the same license as the project (MIT License).

## Questions?

If you have questions about contributing, please:
- Check this document first
- Search existing issues and discussions
- Create a new discussion for general questions
- Create an issue for specific problems

Thank you for contributing to generatecv! 🎉
