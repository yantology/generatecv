# generatecv

Professional CV/Resume generator for Python.

## Features

- 🚀 **Quick Start**: Get started in minutes with built-in example templates
- 📄 **PDF Generation**: Create professional PDFs from structured data
- 🎨 **Customizable Styles**: Multiple templates and page formats
- 🔧 **Easy Python API**: Simple, type-safe Python interface
- 📝 **YAML Support**: Define CV data in readable YAML format
- ⌨️ **CLI Tools**: Command-line tools for rapid prototyping

## Quick Start

### 1. Install

```bash
pip install generatecv
```

### 2. Get Example Template

```bash
generatecv-example
```

### 3. Generate Your CV

```python
from generatecv.pdf_generator import yamltocv, generatepdf

# Load your data
cv_data = yamltocv("example.yaml")

# Generate PDF
generatepdf(cv_data, "my_cv.pdf")
```

That's it! You now have a professional CV in PDF format.

## What's Included

The example template includes:

- **Personal Information**: Contact details, summary, professional title
- **Experience**: Company roles with achievements and descriptions  
- **Education**: Academic background with GPA and details
- **Skills**: Organized by category (Programming, Tools, etc.)
- **Projects**: Portfolio projects with technologies used
- **And more**: Certificates, languages, references

## Example Output

The generated PDF includes:
- Clean, professional layout
- Proper typography and spacing
- Organized sections with clear hierarchy
- Contact information prominently displayed
- Skills and experience highlighted effectively

## Documentation

- [Getting Started](getting-started.md) - Complete setup and usage guide
- [Examples](examples.md) - Comprehensive examples and use cases  
- [API Reference](api/index.md) - Detailed API documentation
- [Contributing](contributing.md) - How to contribute to the project

## Command Line Tools

After installation, you have access to:

- `generatecv-example` - Download example CV template
- `generatecv-example --output custom.yaml` - Save to custom location

## Supported Formats

- **Input**: Python objects, YAML files
- **Output**: PDF (A4, Letter sizes)
- **Styles**: Classic (more coming soon)