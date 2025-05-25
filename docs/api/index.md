# API Reference

Auto-generated API documentation for generatecv package.

## Core Classes

### CV

The main class for creating and managing CV documents.

```python
from generatecv import CV

cv = CV(data, template="modern")
```

#### Methods

- `save(filename, format="pdf")` - Save the CV to a file
- `render()` - Render the CV content
- `set_template(template_name)` - Change the template

### CVData

Data structure for CV information.

```python
from generatecv import CVData

data = CVData({
    "personal": {...},
    "education": [...],
    "experience": [...]
})
```

## Functions

### create_cv()

Create a new CV instance.

```python
generatecv.create_cv(data, template="modern", **kwargs)
```

**Parameters:**
- `data` (dict): CV data dictionary
- `template` (str): Template name (default: "modern")
- `**kwargs`: Additional options

**Returns:**
- `CV`: A new CV instance

### load_template()

Load a specific template.

```python
generatecv.load_template(name)
```

**Parameters:**
- `name` (str): Template name

**Returns:**
- `Template`: Template object

## Templates

Available templates:

- `modern` - Clean, modern design
- `classic` - Traditional CV layout  
- `minimal` - Minimalist design
- `creative` - Creative layout

## Data Structure

### Personal Information

```python
personal = {
    "name": "Full Name",
    "email": "email@example.com",
    "phone": "+1 234 567 8900",
    "location": "City, Country",
    "website": "https://example.com",
    "linkedin": "linkedin.com/in/username",
    "github": "github.com/username"
}
```

### Education

```python
education = [
    {
        "degree": "Bachelor of Science",
        "field": "Computer Science",
        "institution": "University Name",
        "location": "City, Country",
        "year": "2020",
        "gpa": "3.8/4.0",
        "honors": ["Magna Cum Laude"]
    }
]
```

### Experience

```python
experience = [
    {
        "title": "Software Engineer",
        "company": "Company Name",
        "location": "City, Country",
        "duration": "2020 - Present",
        "description": "Brief description of role and achievements",
        "highlights": [
            "Achievement 1",
            "Achievement 2"
        ]
    }
]
```

### Skills

```python
skills = {
    "programming": ["Python", "JavaScript", "Java"],
    "frameworks": ["Django", "React", "Spring"],
    "tools": ["Git", "Docker", "AWS"],
    "languages": ["English (Native)", "Spanish (Fluent)"]
}
```

### Projects

```python
projects = [
    {
        "name": "Project Name",
        "description": "Brief project description",
        "technologies": ["Python", "Django", "PostgreSQL"],
        "url": "https://github.com/username/project",
        "highlights": [
            "Key achievement 1",
            "Key achievement 2"
        ]
    }
]
```

## Configuration

### Global Settings

```python
import generatecv

generatecv.config.set_default_template("modern")
generatecv.config.set_output_format("pdf")
```

### Template Options

```python
template_options = {
    "font_family": "Arial",
    "font_size": 11,
    "margins": {
        "top": 1.0,
        "bottom": 1.0,
        "left": 0.75,
        "right": 0.75
    },
    "colors": {
        "primary": "#2c3e50",
        "secondary": "#3498db",
        "text": "#333333"
    }
}

cv = generatecv.create_cv(data, template_options=template_options)
```

## Exceptions

### CVError

Base exception for generatecv errors.

```python
from generatecv.exceptions import CVError
```

### TemplateError

Raised when template-related errors occur.

```python
from generatecv.exceptions import TemplateError
```

### ValidationError

Raised when data validation fails.

```python
from generatecv.exceptions import ValidationError
```

## Examples

### Basic Usage

```python
import generatecv

data = {
    "personal": {
        "name": "John Doe",
        "email": "john@example.com"
    },
    "education": [...],
    "experience": [...]
}

cv = generatecv.create_cv(data)
cv.save("john_doe_cv.pdf")
```

### Custom Template

```python
cv = generatecv.create_cv(data, template="minimal")
cv.save("minimal_cv.pdf")
```

### Multiple Formats

```python
cv = generatecv.create_cv(data)
cv.save("cv.pdf")
cv.save("cv.html", format="html")
cv.save("cv.docx", format="docx")
```