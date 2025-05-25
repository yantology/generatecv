# generatecv

A Python package for generating professional CVs from structured data.

## Installation

This project uses Python 3.13+ and can be installed using `uv`:

```bash
# Clone the repository
git clone https://github.com/yourusername/generatecv.git
cd generatecv

# Create and activate a virtual environment
uv venv

# Install the package and development dependencies
uv pip install -e ".[dev]"
```

## Usage

To generate a CV:

```python
from generatecv.cv_generator import CVGenerator, create_sample_cv

# Create a CV generator (default is PDF format)
generator = CVGenerator()

# Generate from sample data
cv_data = create_sample_cv()
generator.generate(cv_data, "my_cv.pdf")

# Or load data from YAML
cv_data = generator.load_data_from_yaml("path/to/your_cv.yaml")
generator.generate(cv_data, "my_cv.pdf")
```

## Development

### Type Checking

This project uses `pyrefly` for static type checking:

```bash
# Run type checking
pyrefly check

# Suppress errors temporarily during migration
pyrefly check --suppress-errors
```

### Testing

Tests are written using `pytest`:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=generatecv

# Generate coverage report
pytest --cov=generatecv --cov-report=html
```

### Linting

This project uses `ruff` for linting:

```bash
# Run linter
ruff check .

# Automatically fix issues
ruff check --fix .
```

### Code Formatting

Code formatting is done with `black`:

```bash
# Format code
black .

# Format code with line length of 80 characters
black --line-length 80 .
```

## Project Structure

```
generatecv/
├── src/
│   ├── generatecv/        # Main package
│   │   ├── __init__.py
│   │   └── cv_generator.py
│   ├── tool/              # CLI tools
│   │   ├── __init__.py
│   │   └── main.py
│   └── py.typed           # PEP 561 marker
├── tests/                 # Test directory
│   ├── test_cv_generator.py
│   └── test_example.py
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
