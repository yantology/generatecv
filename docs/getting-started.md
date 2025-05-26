# Getting Started

This guide will help you get started with `generatecv` to create PDF resumes.

## Installation

```bash
pip install generatecv
```

Or using `uv`:

```bash
uv add generatecv
```

## Quick Start with Example Template

The fastest way to get started is using the built-in example system:

### 1. Get the Example Template

After installing `generatecv`, use the CLI tool to download a starter template:

```bash
# Download example YAML to current directory (creates example.yaml)
generatecv-example

# Or specify a custom output path
generatecv-example --output my_cv_data.yaml
```

This creates a YAML file with sample CV data that you can customize.

### 2. Customize Your Data

Edit the generated YAML file with your information:

```yaml
personal_info:
  name: "Your Name"
  email: "your.email@example.com"
  phone: "+1234567890"
  location: "Your City, Country"
  summary: "Your professional summary"
  title: "Your Job Title"

education:
  - institution: "Your University"
    degree: "Your Degree"
    start_date: "2019"
    end_date: "2023"
    # ... add more fields as needed

experience:
  - company: "Your Company"
    location: "Company Location"
    roles:
      - title: "Your Role"
        start_date: "2023-01"
        end_date: "Present"
        description: "Your role description"
        # ... add achievements, etc.

# Add skills, projects, and other sections as needed
```

### 3. Generate Your PDF

```python
from generatecv.pdf_generator import yamltocv, generatepdf

# Load your CV data from YAML
cv_data = yamltocv("example.yaml")  # or your custom filename

# Generate PDF
output_path = generatepdf(
    cv_data=cv_data,
    output_path="my_cv.pdf",
    style="classic",
    page_size="A4"
)

print(f"CV generated successfully: {output_path}")
```

## Alternative: Define Data in Python

If you prefer to define your CV data directly in Python instead of using YAML, here's how:

You'll use models from `generatecv.models` to structure your information:

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import (
    CV, PersonalInfo, Education, CompanyExperience, Role, Skill
)

# Construct your CV data
cv_data = CV(
    personal_info=PersonalInfo(
        name="Your Name",
        email="your.email@example.com",
        phone="+1 234 567 8900",
        location="Your City, Country",
        summary="A brief professional summary about yourself.",
        title="Your Professional Title (e.g., Software Engineer)"
    ),
    education=[
        Education(
            institution="University Name",
            degree="Bachelor of Science in Computer Science",
            start_date="2018-09",
            end_date="2022-06",
            location="City, Country",
            gpa="3.8/4.0"
        )
    ],
    experience=[
        CompanyExperience(
            company="Company Name",
            location="Company Location",
            roles=[
                Role(
                    title="Software Engineer",
                    start_date="2022-07",
                    end_date="Present", # or a specific end date like "2023-12"
                    description="Brief description of your role and responsibilities.",
                    achievements=[
                        "Key achievement 1",
                        "Key achievement 2"
                    ]
                )
            ]
        )
    ],
    skills=[
        Skill(category="Programming Languages", name="Python, Java, JavaScript"),
        Skill(category="Tools", name="Git, Docker, Kubernetes")
    ]
    # You can also add projects, certifications, languages, references, etc.
)

# Generate the PDF
try:
    output_file = generatepdf(
        cv_data=cv_data,
        output_path="my_cv.pdf",
        style="classic",  # Currently 'classic' is the primary style
        page_size="A4"    # Options: "A4" or "letter"
    )
    print(f"CV generated successfully: {output_file}")
except ValueError as e:
    print(f"Error generating PDF: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Styles

`generatecv` uses a style system to define the appearance of the PDF.
- `classic`: This is the default and currently the main implemented style. It provides a traditional CV layout.

You specify the style via the `style` parameter in the `generatepdf` function:
```python
generatepdf(cv_data=your_data, output_path="my_cv.pdf", style="classic")
```

## Page Size

You can set the page size for your PDF:
- `A4` (default)
- `letter`

Specify this using the `page_size` parameter in `generatepdf`:
```python
generatepdf(cv_data=your_data, output_path="my_cv.pdf", page_size="letter")
```

## Output Format

The `generatepdf` function is specifically designed to output PDF files. Other formats like HTML or DOCX are not supported by this function.

## Command Line Tool

The `generatecv-example` command supports these options:

```bash
# Download to current directory as example.yaml
generatecv-example

# Download to a specific path
generatecv-example --output my_cv.yaml
generatecv-example -o custom_filename.yaml

# View help
generatecv-example --help
```

## Error Handling

When working with YAML files or generating PDFs, use proper error handling:

```python
from generatecv.pdf_generator import yamltocv, generatepdf
from pydantic import ValidationError
import yaml

try:
    # Load CV data from YAML
    cv_data = yamltocv("example.yaml")
    
    # Generate PDF
    output_path = generatepdf(
        cv_data=cv_data,
        output_path="my_cv.pdf",
        style="classic",
        page_size="A4"
    )
    print(f"Success: {output_path}")
    
except FileNotFoundError:
    print("Error: YAML file not found")
except yaml.YAMLError as e:
    print(f"Error: Invalid YAML syntax - {e}")
except ValidationError as e:
    print(f"Error: Invalid CV data - {e}")
except ValueError as e:
    print(f"Error: Invalid parameters - {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Next Steps

- Check out the [API Reference](api/index.md) for detailed documentation on models and functions.
- See [Examples](examples.md) for more comprehensive use cases.
- Learn about [Contributing](contributing.md) to the project if you're interested in extending its capabilities.
</edits>