# API Reference

Auto-generated API documentation for the `generatecv` package.

## Core Functionality

The primary way to generate a CV PDF is by using the `generatepdf` function, which takes your CV data (as a `CV` object) and an output path. Data can be prepared using Pydantic models from `generatecv.models` or loaded from a YAML file using `yamltocv`.

### `generatepdf()`

Generates a PDF CV from the provided data.

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import CV, PersonalInfo, Education, CompanyExperience, Role # and other models

# Prepare your CV data according to the structure defined in generatecv.models.CV
cv_data = CV(
    personal_info=PersonalInfo(
        name="Full Name",
        email="email@example.com",
        phone="+1-555-123-4567",
        location="City, Country",
        website="https://example.com",
        linkedin="https://linkedin.com/in/username",
        github="https://github.com/username",
        summary="A brief professional summary.",
        title="Senior Software Engineer"
    ),
    education=[
        Education(
            institution="University Name",
            degree="Bachelor of Science",
            start_date="2018-09",
            end_date="2022-06",
            location="City, Country",
            details="Thesis title, honors, etc.",
            gpa="3.8/4.0"
        )
    ],
    experience=[
        CompanyExperience(
            company="Tech Solutions Inc.",
            location="New York, NY",
            roles=[
                Role(
                    title="Software Engineer",
                    start_date="2022-07",
                    end_date="Present",
                    location="New York, NY",
                    description="Role overview.",
                    achievements=["Achievement 1", "Achievement 2"]
                )
            ]
        )
    ],
    # ... other sections like skills, projects, etc.
)

output_file_path = generatepdf(cv_data=cv_data, output_path="my_cv.pdf", style="classic", page_size="A4")
print(f"CV generated at: {output_file_path}")
```

**Parameters:**
- `cv_data` (`generatecv.models.CV`): A Pydantic model instance containing all CV data.
- `output_path` (str): Path where the PDF will be saved.
- `style` (str): Style name for the CV (default: "classic"). Currently, only "classic" is implemented.
- `page_size` (str): Size of the page (default: "A4"). Supported: "A4", "letter".

**Returns:**
- `str`: Path to the generated PDF file.

### `yamltocv()`

Parses a YAML file, validates its content against the `generatecv.models.CV` structure, and returns a `CV` object. This function *does not* generate a PDF; it only prepares the data.

```python
from generatecv.pdf_generator import yamltocv, generatepdf
from generatecv.models import CV # For type hinting

# Assume 'cv_data.yaml' exists and is structured according to generatecv.models.CV
try:
    cv_data_from_yaml: CV = yamltocv(yaml_path="path/to/your/cv_data.yaml")
    # Now you can use cv_data_from_yaml with generatepdf
    generatepdf(cv_data=cv_data_from_yaml, output_path="cv_from_yaml.pdf")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e: # Catches yaml.YAMLError, pydantic.ValidationError
    print(f"Error processing YAML file: {e}")

```

**Parameters:**
- `yaml_path` (str): Path to the YAML file containing CV data.
- `output_path` (str): This parameter is defined in the function signature but is **not used** by `yamltocv`.
- `style` (str): This parameter is defined in the function signature but is **not used** by `yamltocv`.
- `page_size` (str): This parameter is defined in the function signature but is **not used** by `yamltocv`.


**Returns:**
- `generatecv.models.CV`: A Pydantic model instance containing the validated CV data from the YAML file.

**Raises:**
- `FileNotFoundError`: If the YAML file does not exist.
- `yaml.YAMLError`: If the YAML file is malformed.
- `pydantic.ValidationError`: If the data in the YAML file does not conform to the `CV` model structure.

## Data Structure (`generatecv.models.CV`)

The `generatecv` package uses Pydantic models defined in `generatecv.models.py` to structure and validate CV data. The main model is `CV`.

```python
from generatecv.models import (
    PersonalInfo, Education, CompanyExperience, Role, Skill,
    Project, Certificate, Language, Reference, CV
)
```

### `PersonalInfo`

```python
personal_info = {
    "name": "Full Name",  # required, str
    "email": "user@example.com",  # required, EmailStr
    "phone": "+1-555-123-4567",  # optional, str
    "location": "City, Country",  # optional, str
    "website": "https://example.com",  # optional, HttpUrl
    "linkedin": "https://linkedin.com/in/username",  # optional, HttpUrl
    "github": "https://github.com/username",  # optional, HttpUrl
    "summary": "A brief professional summary.",  # optional, str
    "title": "Senior Software Engineer"  # optional, str
}
```

### `Education` (list item)

```python
education_item = {
    "institution": "University Name",  # required, str
    "degree": "B.S. in Computer Science",  # required, str
    "start_date": "YYYY-MM",  # required, str (e.g., "2018-09")
    "end_date": "YYYY-MM or Present",  # optional, str (e.g., "2022-06", "Present")
    "location": "City, Country",  # optional, str
    "details": "Thesis title, honors, etc.",  # optional, str
    "gpa": "3.8/4.0"  # optional, str
}
```

### `CompanyExperience` (list item)

This model groups roles by company.

```python
company_experience_item = {
    "company": "Company Name",  # required, str
    "location": "Company Location (e.g., New York, NY)",  # optional, str
    "roles": [  # required, list of Role objects
        {
            "title": "Software Engineer",  # required, str
            "start_date": "YYYY-MM",  # required, str (e.g., "2022-07")
            "end_date": "YYYY-MM or Present",  # optional, str
            "location": "Role Location (if different)",  # optional, str
            "description": "Role overview.",  # optional, str
            "achievements": ["Achievement 1", "Achievement 2"]  # optional, list[str]
        }
        # ... more roles at the same company
    ]
}
```

### `Skill` (list item)

```python
skill_item = {
    "category": "Programming Languages",  # required, str
    "name": "Python"  # required, str (Note: In pdf_generator, this is a single string of skills, not a list under the category)
}
# Note: The _add_skills method in pdf_generator.py currently iterates through `skills`
# and for each skill_item, it prints skill_item.category as a heading,
# and then skill_item.name as a paragraph.
# Example:
# skills = [
#     Skill(category="Programming Languages", name="Python, Java, C++"),
#     Skill(category="Frameworks", name="Django, Spring, React")
# ]
# This would render:
# Programming Languages
# Python, Java, C++
# Frameworks
# Django, Spring, React
```

### `Project` (list item)

```python
project_item = {
    "name": "Project Alpha",  # required, str
    "description": "A brief project description.",  # optional, str
    "technologies": ["Python", "React"],  # optional, list[str]
    "link": "https://github.com/username/project",  # optional, HttpUrl
    "start_date": "YYYY-MM",  # optional, str
    "end_date": "YYYY-MM or Ongoing",  # optional, str
    "achievements": ["Key outcome 1"]  # optional, list[str]
}
```

### `Certificate` (list item)

```python
certificate_item = {
    "name": "Certified Kubernetes Administrator",  # required, str
    "issuer": "Cloud Native Computing Foundation",  # required, str
    "date": "YYYY-MM",  # optional, str
    "description": "Details about the certification.",  # optional, str
    "link": "https://certs.example.com/id"  # optional, HttpUrl
}
```

### `Language` (list item)

```python
language_item = {
    "name": "English",  # required, str
    "proficiency": "Native"  # required, str
}
```

### `Reference` (list item)

```python
reference_item = {
    "name": "Dr. Jane Doe",  # required, str
    "position": "Professor",  # required, str
    "company": "University X",  # required, str
    "contact": "jane.doe@example.com or Available upon request",  # optional, str
    "relation": "Former Manager"  # optional, str
}
```

### Other `CV` Sections

The main `CV` model also supports:
- `publications: list[str] | None`
- `awards: list[str] | None`
- `interests: list[str] | None`
- `custom_sections: dict[str, str | list[str]] | None`

## PDF Generation (`generatecv.pdf_generator`)

The `pdf_generator.py` module contains the `_PDFGenerator` class, which is used by `generatepdf` to generate PDF documents. It handles the layout, formatting, and content addition for different sections of the CV using ReportLab.

The main user-facing function for PDF generation is `generatepdf`.

The `yamltocv` function in `pdf_generator.py` handles loading data from a YAML file and validating it into a `CV` object. It does not produce a PDF itself but prepares the data for `generatepdf`.

Key internal methods of `_PDFGenerator` include:
- `__init__(output_path, cv_data, style, page_size)`: Initializes the generator.
- `generate()`: Orchestrates the PDF generation.
- `_add_content()`: Iterates through CV data sections.
- `_add_personal_info()`
- `_add_section()` (generic section handler)
- `_format_company_experience()`
- `_format_education()`
- `_add_skills()`
- `_format_project()`
- `_format_certificate()`
- `_format_language()`
- `_format_reference()`
- `_add_simple_list_section()` (for publications, awards, interests)
- `_add_custom_sections()`

## Styles (Templates)

The visual appearance of the PDF is determined by styles. Currently, the `generatecv` package has one implemented style:
- `classic` - A traditional CV layout. This is the default style.

You can specify the style when calling `generatepdf(cv_data, output_path, style="classic")`.
The styles are defined in `generatecv.styles` (e.g., `ClassicStyle`).

## Configuration

Configuration is primarily done through the parameters passed to the `generatepdf` function:
- `output_path`: Specifies the filename for the PDF.
- `style`: Chooses the visual style (currently "classic").
- `page_size`: Sets the page dimensions ("A4" or "letter").

There is no separate global configuration file or mechanism described in the current `pdf_generator.py`.

## Exceptions

### `pydantic.ValidationError`
Raised by Pydantic models (e.g., `CV.model_validate()` used in `yamltocv`) if the provided data does not conform to the defined schema.
```python
from pydantic import ValidationError
```

### `FileNotFoundError`
Raised by `yamltocv` if the specified YAML file path does not exist.

### `yaml.YAMLError` (from PyYAML)
Raised by `yamltocv` if the YAML file is malformed and cannot be parsed.
```python
import yaml # For context, though you usually catch yaml.YAMLError
```

### `ValueError`
- Raised by `_PDFGenerator` (and thus `generatepdf`) if an invalid `style` name or `page_size` is provided.
- Raised by `parse_yaml_file` (used in `yamltocv`) if the YAML content does not result in a dictionary.

## Examples

### Basic Usage (Generating PDF from Python data)

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import CV, PersonalInfo, Education, CompanyExperience, Role # ... and other necessary models

# Construct data using Pydantic models
data = CV(
    personal_info=PersonalInfo(name="John Doe", email="john@example.com", title="Software Developer"),
    education=[Education(institution="State University", degree="BSc Computer Science", start_date="2019-01", end_date="2022-12")],
    experience=[
        CompanyExperience(
            company="Doe Corp",
            roles=[Role(title="Junior Developer", start_date="2023-01", end_date="Present")]
        )
    ]
    # ... add other sections as needed
)

try:
    file_path = generatepdf(cv_data=data, output_path="john_doe_cv.pdf", style="classic")
    print(f"CV saved to {file_path}")
except ValueError as e:
    print(f"Error generating PDF: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

### Generating PDF from a YAML file

```python
from generatecv.pdf_generator import yamltocv, generatepdf
from generatecv.models import CV # For type hinting
from pydantic import ValidationError
import yaml # For yaml.YAMLError

# 1. Create a YAML file (e.g., 'my_cv_data.yaml') with your CV details
#    following the structure of generatecv.models.CV

# 2. Use yamltocv to load and validate, then generatepdf
try:
    cv_object: CV = yamltocv(yaml_path="my_cv_data.yaml")
    pdf_file = generatepdf(cv_data=cv_object, output_path="cv_from_yaml.pdf")
    print(f"CV generated from YAML and saved to {pdf_file}")
except FileNotFoundError:
    print("Error: The YAML file was not found.")
except yaml.YAMLError:
    print("Error: The YAML file is not valid YAML.")
except ValidationError as ve:
    print(f"Data validation error in YAML: {ve}")
except ValueError as ve_gen:
    print(f"PDF generation error (e.g. invalid style): {ve_gen}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

### Output Formats

The `generatepdf` function specifically creates PDF files. Other output formats like HTML or DOCX are not supported by this function.
```python
# Only PDF is supported by generatepdf
file_path = generatepdf(cv_data=data, output_path="my_cv.pdf")
```