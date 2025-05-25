# Getting Started

This guide will help you get started with generatecv.

## Installation

```bash
pip install generatecv
```

Or using uv:

```bash
uv add generatecv
```

## Basic Usage

```python
import generatecv

# Basic CV generation example
# Add your examples here
```

## Configuration

generatecv can be configured in several ways:

### Using a configuration file

Create a `cv_config.yaml` file:

```yaml
personal:
  name: "Your Name"
  email: "your.email@example.com"
  phone: "+1 234 567 8900"
  location: "Your City, Country"

education:
  - degree: "Bachelor of Science"
    institution: "University Name"
    year: "2020"

experience:
  - title: "Software Engineer"
    company: "Company Name"
    duration: "2020 - Present"
    description: "Brief description of your role"
```

### Using Python directly

```python
import generatecv

cv_data = {
    "personal": {
        "name": "Your Name",
        "email": "your.email@example.com",
        "phone": "+1 234 567 8900",
        "location": "Your City, Country"
    },
    "education": [
        {
            "degree": "Bachelor of Science",
            "institution": "University Name",
            "year": "2020"
        }
    ],
    "experience": [
        {
            "title": "Software Engineer",
            "company": "Company Name",
            "duration": "2020 - Present",
            "description": "Brief description of your role"
        }
    ]
}

# Generate CV
cv = generatecv.create_cv(cv_data)
cv.save("my_cv.pdf")
```

## Templates

generatecv supports multiple templates:

- `modern` - Clean, modern design
- `classic` - Traditional CV layout
- `minimal` - Minimalist design
- `creative` - Creative layout for design roles

```python
# Use a specific template
cv = generatecv.create_cv(cv_data, template="modern")
```

## Output Formats

Generate your CV in different formats:

```python
# PDF (default)
cv.save("cv.pdf")

# HTML
cv.save("cv.html", format="html")

# Word document
cv.save("cv.docx", format="docx")
```

## Next Steps

- Check out the [API Reference](api/index.md) for detailed documentation
- See [Examples](examples.md) for more use cases
- Learn about [Contributing](contributing.md) to the project