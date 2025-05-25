# Examples

Here are some comprehensive examples of using generatecv to create professional CVs.

## Basic Example

```python
import generatecv

# Simple CV data
cv_data = {
    "personal": {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "+1 (555) 123-4567",
        "location": "San Francisco, CA",
        "linkedin": "linkedin.com/in/janesmith",
        "github": "github.com/janesmith"
    },
    "summary": "Experienced software engineer with 5+ years in full-stack development",
    "experience": [
        {
            "title": "Senior Software Engineer",
            "company": "Tech Corp",
            "location": "San Francisco, CA",
            "duration": "2021 - Present",
            "description": "Lead development of microservices architecture",
            "highlights": [
                "Reduced system latency by 40%",
                "Led team of 5 engineers",
                "Implemented CI/CD pipeline"
            ]
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "Stanford University",
            "location": "Stanford, CA",
            "year": "2019",
            "gpa": "3.8/4.0"
        }
    ]
}

# Generate CV
cv = generatecv.create_cv(cv_data)
cv.save("jane_smith_cv.pdf")
```

## Academic CV Example

```python
import generatecv

academic_data = {
    "personal": {
        "name": "Dr. Michael Chen",
        "email": "m.chen@university.edu",
        "phone": "+1 (555) 987-6543",
        "location": "Boston, MA",
        "website": "michaelchen.com",
        "orcid": "0000-0000-0000-0000"
    },
    "summary": "Research scientist specializing in machine learning and computer vision",
    "education": [
        {
            "degree": "Ph.D. in Computer Science",
            "field": "Machine Learning",
            "institution": "MIT",
            "location": "Cambridge, MA",
            "year": "2020",
            "thesis": "Deep Learning Approaches for Medical Image Analysis",
            "advisor": "Prof. John Doe"
        },
        {
            "degree": "M.S. in Computer Science",
            "institution": "Stanford University",
            "year": "2016"
        }
    ],
    "experience": [
        {
            "title": "Postdoctoral Research Associate",
            "company": "Harvard Medical School",
            "duration": "2020 - Present",
            "description": "Research on AI applications in healthcare"
        }
    ],
    "publications": [
        {
            "title": "Deep Learning for Medical Image Segmentation",
            "authors": "M. Chen, J. Smith, A. Johnson",
            "journal": "Nature Machine Intelligence",
            "year": "2021",
            "volume": "3",
            "pages": "123-135"
        }
    ],
    "grants": [
        {
            "title": "NIH R01 Grant",
            "amount": "$500,000",
            "duration": "2021-2024",
            "role": "Co-PI"
        }
    ]
}

cv = generatecv.create_cv(academic_data, template="academic")
cv.save("michael_chen_academic_cv.pdf")
```

## Creative Professional Example

```python
import generatecv

creative_data = {
    "personal": {
        "name": "Sarah Williams",
        "email": "hello@sarahwilliams.design",
        "phone": "+1 (555) 456-7890",
        "location": "New York, NY",
        "website": "sarahwilliams.design",
        "behance": "behance.net/sarahwilliams",
        "instagram": "@sarahdesigns"
    },
    "summary": "Award-winning graphic designer with expertise in branding and digital design",
    "experience": [
        {
            "title": "Senior Graphic Designer",
            "company": "Creative Agency Inc.",
            "duration": "2020 - Present",
            "description": "Lead designer for major brand campaigns",
            "highlights": [
                "Designed rebrand for Fortune 500 company",
                "Won 3 design awards in 2022",
                "Managed design team of 4"
            ]
        }
    ],
    "skills": {
        "design": ["Adobe Creative Suite", "Figma", "Sketch"],
        "specialties": ["Brand Identity", "UI/UX Design", "Print Design"],
        "software": ["Photoshop", "Illustrator", "InDesign", "After Effects"]
    },
    "awards": [
        {
            "title": "Best Brand Identity Design",
            "organization": "Design Awards 2022",
            "year": "2022"
        }
    ],
    "portfolio": [
        {
            "project": "Nike Campaign Redesign",
            "description": "Complete visual identity overhaul",
            "url": "sarahwilliams.design/nike"
        }
    ]
}

cv = generatecv.create_cv(creative_data, template="creative")
cv.save("sarah_williams_cv.pdf")
```

## Recent Graduate Example

```python
import generatecv

graduate_data = {
    "personal": {
        "name": "Alex Rodriguez",
        "email": "alex.rodriguez@email.com",
        "phone": "+1 (555) 234-5678",
        "location": "Austin, TX",
        "linkedin": "linkedin.com/in/alexrodriguez",
        "github": "github.com/alexr"
    },
    "objective": "Recent computer science graduate seeking entry-level software engineering position",
    "education": [
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "University of Texas at Austin",
            "location": "Austin, TX",
            "year": "2023",
            "gpa": "3.7/4.0",
            "honors": ["Dean's List", "Magna Cum Laude"],
            "relevant_coursework": [
                "Data Structures & Algorithms",
                "Software Engineering",
                "Database Systems",
                "Machine Learning"
            ]
        }
    ],
    "projects": [
        {
            "name": "E-commerce Web Application",
            "description": "Full-stack web app with user authentication and payment processing",
            "technologies": ["React", "Node.js", "MongoDB", "Stripe API"],
            "url": "github.com/alexr/ecommerce-app",
            "highlights": [
                "Implemented responsive design",
                "Integrated secure payment system",
                "Deployed on AWS"
            ]
        },
        {
            "name": "Machine Learning Stock Predictor",
            "description": "Python application using LSTM networks for stock price prediction",
            "technologies": ["Python", "TensorFlow", "Pandas", "NumPy"],
            "url": "github.com/alexr/stock-predictor"
        }
    ],
    "experience": [
        {
            "title": "Software Engineering Intern",
            "company": "StartupXYZ",
            "duration": "Summer 2022",
            "description": "Developed features for mobile application",
            "highlights": [
                "Contributed to codebase with 50+ commits",
                "Fixed 15+ bugs and implemented 5 new features",
                "Collaborated with cross-functional teams"
            ]
        }
    ],
    "skills": {
        "programming": ["Python", "JavaScript", "Java", "C++"],
        "web": ["React", "HTML/CSS", "Node.js", "Express"],
        "databases": ["MySQL", "MongoDB", "PostgreSQL"],
        "tools": ["Git", "Docker", "AWS", "VS Code"]
    }
}

cv = generatecv.create_cv(graduate_data, template="modern")
cv.save("alex_rodriguez_cv.pdf")
```

## Multiple Format Generation

```python
import generatecv

# Use the same data for multiple formats
data = {...}  # Your CV data

cv = generatecv.create_cv(data)

# Generate in different formats
cv.save("cv.pdf")
cv.save("cv.html", format="html")
cv.save("cv.docx", format="docx")
cv.save("cv.txt", format="text")
```

## Custom Template Options

```python
import generatecv

# Custom styling options
template_options = {
    "font_family": "Georgia",
    "font_size": 12,
    "line_height": 1.4,
    "margins": {
        "top": 0.8,
        "bottom": 0.8,
        "left": 0.7,
        "right": 0.7
    },
    "colors": {
        "primary": "#2c3e50",
        "secondary": "#3498db",
        "accent": "#e74c3c",
        "text": "#2c3e50"
    },
    "sections": {
        "show_summary": True,
        "show_skills": True,
        "show_projects": True,
        "experience_format": "detailed"
    }
}

cv = generatecv.create_cv(data, template="modern", template_options=template_options)
cv.save("custom_styled_cv.pdf")
```

## Batch CV Generation

```python
import generatecv
import json

# Generate CVs for multiple people
def generate_team_cvs():
    team_data = [
        {"name": "person1", "data": {...}},
        {"name": "person2", "data": {...}},
        {"name": "person3", "data": {...}}
    ]
    
    for person in team_data:
        cv = generatecv.create_cv(person["data"])
        cv.save(f"{person['name']}_cv.pdf")
        print(f"Generated CV for {person['name']}")

generate_team_cvs()
```

## Loading Data from File

```python
import generatecv
import yaml
import json

# Load from YAML
with open("cv_data.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

cv_yaml = generatecv.create_cv(yaml_data)
cv_yaml.save("from_yaml.pdf")

# Load from JSON
with open("cv_data.json", "r") as file:
    json_data = json.load(file)

cv_json = generatecv.create_cv(json_data)
cv_json.save("from_json.pdf")
```

## Error Handling

```python
import generatecv
from generatecv.exceptions import CVError, TemplateError, ValidationError

try:
    cv = generatecv.create_cv(data, template="invalid_template")
    cv.save("output.pdf")
except TemplateError as e:
    print(f"Template error: {e}")
except ValidationError as e:
    print(f"Data validation error: {e}")
except CVError as e:
    print(f"CV generation error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Template Comparison

```python
import generatecv

# Generate the same CV with different templates
templates = ["modern", "classic", "minimal", "creative"]

for template in templates:
    cv = generatecv.create_cv(data, template=template)
    cv.save(f"cv_{template}.pdf")
    print(f"Generated {template} version")
```

## Configuration Examples

```python
import generatecv

# Set global defaults
generatecv.config.set_default_template("modern")
generatecv.config.set_default_format("pdf")
generatecv.config.set_output_directory("./cvs/")

# Create CV with global settings
cv = generatecv.create_cv(data)
cv.save("cv_with_defaults.pdf")

# Override global settings for specific CV
cv_custom = generatecv.create_cv(data, template="minimal")
cv_custom.save("cv_minimal.pdf", format="html")
```

These examples demonstrate various use cases and features of generatecv. You can adapt them to your specific needs and requirements.