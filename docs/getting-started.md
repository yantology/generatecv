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

## Basic Usage

The core of `generatecv` involves defining your CV data using Pydantic models and then using the `generatepdf` function to create a PDF document.

### 1. Define your CV Data in Python

You'll use models from `generatecv.models` to structure your information.

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

### 2. Using a YAML Configuration File

Alternatively, you can define your CV data in a YAML file and use the `yamltocv` function to load it, then pass the result to `generatepdf`.

**a. Create a `cv_config.yaml` file:**

```yaml
personal_info:
  name: "Your Name"
  email: "your.email@example.com"
  phone: "+1 234 567 8900"
  location: "Your City, Country"
  summary: "A brief professional summary."
  title: "Your Professional Title"

education:
  - institution: "University Name"
    degree: "Bachelor of Science"
    start_date: "2018-09"
    end_date: "2022-06"
    location: "City, Country"
    gpa: "3.8/4.0"

experience:
  - company: "Company Name"
    location: "Company Location"
    roles:
      - title: "Software Engineer"
        start_date: "2022-07"
        end_date: "Present"
        description: "Brief description of your role."
        achievements:
          - "Achievement A"
          - "Achievement B"

skills:
  - category: "Languages"
    name: "Python, Go, SQL"
  - category: "Databases"
    name: "PostgreSQL, MongoDB"

# Add other sections like projects, certifications, languages as needed
# Ensure the structure matches generatecv.models.CV
```

**b. Python script to process the YAML:**

```python
from generatecv.pdf_generator import yamltocv, generatepdf
from generatecv.models import CV # For type hinting
from pydantic import ValidationError
import yaml # For yaml.YAMLError

yaml_file_path = "cv_config.yaml"
output_pdf_path = "my_cv_from_yaml.pdf"

try:
    # Load data from YAML and validate it
    # Note: yamltocv has output_path, style, page_size params that are not used by it.
    cv_data_from_yaml: CV = yamltocv(yaml_path=yaml_file_path)

    # Generate PDF from the loaded data
    generated_file = generatepdf(
        cv_data=cv_data_from_yaml,
        output_path=output_pdf_path,
        style="classic",
        page_size="A4"
    )
    print(f"CV from YAML generated successfully: {generated_file}")

except FileNotFoundError:
    print(f"Error: YAML file not found at {yaml_file_path}")
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")
except ValidationError as e:
    print(f"Data validation error from YAML content: {e}")
except ValueError as e: # For generatepdf errors like invalid style
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

## Next Steps

- Check out the [API Reference](api/index.md) for detailed documentation on models and functions.
- See [Examples](examples.md) for more use cases.
- Learn about [Contributing](contributing.md) to the project if you're interested in extending its capabilities.