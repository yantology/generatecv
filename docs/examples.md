# Examples

Here are some comprehensive examples of using `generatecv` to create professional CVs in PDF format.

## Getting Started with the Example Template

The easiest way to start is by using the built-in example system:

### 1. Download Example Template

```bash
# Download example YAML to current directory
generatecv-example

# Or specify a custom output path
generatecv-example --output my_cv_data.yaml
```

### 2. Customize and Generate

```python
from generatecv.pdf_generator import yamltocv, generatepdf

# Load the example data (modify the YAML file first with your information)
cv_data = yamltocv("example.yaml")

# Generate your CV
output_path = generatepdf(
    cv_data=cv_data,
    output_path="my_cv.pdf",
    style="classic",
    page_size="A4"
)

print(f"CV generated: {output_path}")
```

The example YAML contains realistic data that you can customize:

```yaml
personal_info:
  name: Muhamad Wijayanto
  email: work@yantology.dev
  phone: "+6285804155314"
  location: "East Java"
  website: "https://www.yantology.dev"
  linkedin: "https://linkedin.com/in/muhamad-wijayanto"
  github: "https://github.com/yantology"
  summary: "I am a passionate software engineer..."
  title: "Backend Engineer"

# Full example includes education, experience, skills, projects
# Edit this file with your own information
```

## Basic Example (Python Data)

This example shows how to define CV data directly in Python using the Pydantic models and then generate a PDF.

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import (
    CV, PersonalInfo, Education, CompanyExperience, Role, Skill, Project,
    Certificate, Language, Reference
)

# 1. Construct your CV data using Pydantic models
cv_data = CV(
    personal_info=PersonalInfo(
        name="Jane Smith",
        email="jane.smith@example.com",
        phone="+1 (555) 123-4567",
        location="San Francisco, CA",
        linkedin="https://linkedin.com/in/janesmith",
        github="https://github.com/janesmith",
        summary="Experienced software engineer with 5+ years in full-stack development.",
        title="Senior Software Engineer"
    ),
    experience=[
        CompanyExperience(
            company="Tech Corp",
            location="San Francisco, CA",
            roles=[
                Role(
                    title="Senior Software Engineer",
                    start_date="2021-01",
                    end_date="Present",
                    description="Lead development of microservices architecture.",
                    achievements=[
                        "Reduced system latency by 40%",
                        "Led team of 5 engineers",
                        "Implemented CI/CD pipeline"
                    ]
                )
            ]
        )
    ],
    education=[
        Education(
            institution="Stanford University",
            degree="Bachelor of Science in Computer Science",
            location="Stanford, CA",
            start_date="2015-09",
            end_date="2019-06",
            gpa="3.8/4.0"
        )
    ],
    skills=[
        Skill(category="Programming Languages", name="Python, JavaScript, Java"),
        Skill(category="Frameworks/Tools", name="React, Docker, AWS, Django")
    ],
    projects=[
        Project(
            name="Open Source Contribution",
            description="Contributed to a popular open-source library.",
            technologies=["Python", "Git"],
            link="https://github.com/janesmith/project-example"
        )
    ],
    languages=[
        Language(name="English", proficiency="Native"),
        Language(name="Spanish", proficiency="Conversational")
    ]
    # You can add certifications, references, publications, awards, interests, custom_sections as needed
)

# 2. Generate the CV PDF
try:
    output_pdf_path = generatepdf(
        cv_data=cv_data,
        output_path="jane_smith_cv.pdf",
        style="classic",  # Currently 'classic' is the main style
        page_size="A4"    # 'A4' or 'letter'
    )
    print(f"CV successfully generated at: {output_pdf_path}")
except ValueError as e:
    print(f"Error during PDF generation: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Working with Custom YAML Files

Beyond the example template, you can create completely custom YAML files. `generatecv` can load CV data from any properly structured YAML file.

**1. Create your YAML data file (e.g., `my_cv_data.yaml`):**

```yaml
personal_info:
  name: "Dr. Michael Chen"
  email: "m.chen@university.edu"
  phone: "+1 (555) 987-6543"
  location: "Boston, MA"
  website: "http://michaelchen.com" # Ensure HttpUrl validity
  # orcid: "0000-0000-0000-0000" # Not a standard field in PersonalInfo, use custom_sections or summary
  summary: "Research scientist specializing in machine learning and computer vision. ORCID: 0000-0000-0000-0000"
  title: "Research Scientist"

education:
  - institution: "MIT"
    degree: "Ph.D. in Computer Science"
    # field: "Machine Learning" # Not a direct field in Education model, combine with degree or details
    details: "Field: Machine Learning. Thesis: Deep Learning Approaches for Medical Image Analysis. Advisor: Prof. John Doe"
    start_date: "2016-09"
    end_date: "2020-05"
    location: "Cambridge, MA"
  - institution: "Stanford University"
    degree: "M.S. in Computer Science"
    start_date: "2014-09"
    end_date: "2016-06"

experience: # This should be a list of CompanyExperience
  - company: "Harvard Medical School" # This is a CompanyExperience item
    roles: # It needs a 'roles' list
      - title: "Postdoctoral Research Associate"
        start_date: "2020-06"
        end_date: "Present"
        description: "Research on AI applications in healthcare."

publications: # This is a list of strings
  - "Chen, M., Smith, J., Johnson, A. (2021). Deep Learning for Medical Image Segmentation. Nature Machine Intelligence, 3, 123-135."

# grants: # Not a direct field in CV model, use custom_sections
#   - title: "NIH R01 Grant"
#     amount: "$500,000"
#     duration: "2021-2024"
#     role: "Co-PI"
custom_sections:
  grants:
    - "NIH R01 Grant: $500,000, Duration: 2021-2024, Role: Co-PI"

# ... other sections like skills, projects, etc.
```

**2. Python script to load custom YAML and generate PDF:**

```python
from generatecv.pdf_generator import yamltocv, generatepdf
from generatecv.models import CV # For type hinting
from pydantic import ValidationError
import yaml # For yaml.YAMLError

yaml_file = "my_cv_data.yaml" # Path to your YAML file
output_pdf = "michael_chen_academic_cv.pdf"

try:
    # Load and validate data from YAML
    cv_data_from_yaml: CV = yamltocv(yaml_path=yaml_file)

    # Generate PDF using the loaded data
    generated_path = generatepdf(
        cv_data=cv_data_from_yaml,
        output_path=output_pdf,
        style="classic",
        page_size="A4"
    )
    print(f"Academic CV generated from YAML and saved to: {generated_path}")

except FileNotFoundError:
    print(f"Error: The YAML file '{yaml_file}' was not found.")
except yaml.YAMLError as e:
    print(f"Error: The YAML file '{yaml_file}' is not valid YAML. Details: {e}")
except ValidationError as ve:
    print(f"Data validation error in '{yaml_file}': {ve}")
except ValueError as ve_gen: # For errors from generatepdf (e.g. invalid style)
    print(f"PDF generation error: {ve_gen}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

### Pro Tip: Start with the Example

Instead of creating a YAML from scratch, it's recommended to start with the example template:

```bash
# Get the example template first
generatecv-example --output michael_chen_cv.yaml

# Then modify michael_chen_cv.yaml with the academic data above
# This ensures you have the correct structure
```

## Complete CLI Workflow Example

Here's a complete example showing the entire process from installation to PDF generation using the command-line tool:

### Step 1: Install the Package

```bash
pip install generatecv
```

### Step 2: Download the Example Template

```bash
# Download to current directory as example.yaml
generatecv-example

# Or specify a custom name
generatecv-example --output my_cv.yaml
```

### Step 3: View the Generated Template

The command creates a YAML file with this structure:

```bash
cat example.yaml
```

```yaml
personal_info:
  name: Muhamad Wijayanto
  email: work@yantology.dev
  phone: "+6285804155314"
  location: "East Java"
  website: "https://www.yantology.dev"
  linkedin: "https://linkedin.com/in/muhamad-wijayanto"
  github: "https://github.com/yantology"
  summary: "I am a passionate software engineer with a strong foundation in backend development..."
  title: "Backend Engineer"

education:
  - institution: University of Jember
    degree: Bachelor of Information Systems
    start_date: "2019"
    end_date: "2024"
    location: "Jember, East Java"
    details: "Learning about software engineering, data science, and machine learning."
    gpa: "3.5/4.0"

experience:
  - company: Freelance
    location: "Remote"
    roles:
      - title: Fullstack Engineer
        start_date: "Jan 2025"
        end_date: "Present"
        description: "Developed and maintained web applications for various clients..."

# ... and more sections
```

### Step 4: Customize Your Data

Edit the YAML file with your information:

```bash
# Open in your preferred editor
nano example.yaml
# or
code example.yaml
# or
vim example.yaml
```

### Step 5: Generate the PDF

Create a Python script (`generate_cv.py`):

```python
#!/usr/bin/env python3
"""
Simple script to generate CV from YAML template
"""

from generatecv.pdf_generator import yamltocv, generatepdf
from pydantic import ValidationError
import yaml
import sys

def main():
    yaml_file = "example.yaml"  # or sys.argv[1] for command line input
    output_file = "my_cv.pdf"
    
    try:
        print(f"Loading CV data from {yaml_file}...")
        cv_data = yamltocv(yaml_file)
        
        print(f"Generating PDF...")
        result_path = generatepdf(
            cv_data=cv_data,
            output_path=output_file,
            style="classic",
            page_size="A4"
        )
        
        print(f"✅ Success! CV generated at: {result_path}")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{yaml_file}' not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error: Invalid YAML syntax - {e}")
        sys.exit(1)
    except ValidationError as e:
        print(f"❌ Error: Invalid CV data - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Step 6: Run the Script

```bash
python generate_cv.py
```

Expected output:
```
Loading CV data from example.yaml...
Generating PDF...
✅ Success! CV generated at: my_cv.pdf
```

### CLI Options Reference

The `generatecv-example` command supports these options:

```bash
# Show help
generatecv-example --help

# Download with default name (example.yaml)
generatecv-example

# Download with custom name
generatecv-example --output my_resume.yaml
generatecv-example -o custom_cv_data.yaml

# Download to specific directory
generatecv-example --output ~/Documents/my_cv.yaml
```

### One-liner for Quick Testing

For rapid prototyping, you can combine everything into a single command:

```bash
# Download template, then generate PDF in Python
generatecv-example && python -c "
from generatecv.pdf_generator import yamltocv, generatepdf
cv = yamltocv('example.yaml')
print('Generated:', generatepdf(cv, 'quick_cv.pdf'))
"
```
</edits>
</edits>

<edits>

<old_text>
# Clean up temporary files (optional)
import os
os.remove("temp_valid.yaml")
os.remove("temp_invalid_syntax.yaml")
os.remove("temp_invalid_data.yaml")
```

These examples demonstrate various use cases and features of `generatecv` focusing on the `pdf_generator` and `models`. Adapt them to your specific needs. Remember that the `style` parameter currently only supports "classic", and `page_size` supports "A4" and "letter".

## Creative Professional Example (using Python data)

This example focuses on a creative professional, showcasing how to structure data for skills and projects.

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import CV, PersonalInfo, CompanyExperience, Role, Skill, Project, Award # Assuming Award model exists or use custom_sections

# Data for a creative professional
creative_data = CV(
    personal_info=PersonalInfo(
        name="Sarah Williams",
        email="hello@sarahwilliams.design",
        phone="+1 (555) 456-7890",
        location="New York, NY",
        website="http://sarahwilliams.design", # Ensure HttpUrl validity
        # behance: "behance.net/sarahwilliams", # Use custom_sections or summary
        # instagram: "@sarahdesigns" # Use custom_sections or summary
        summary="Award-winning graphic designer with expertise in branding and digital design. Behance: behance.net/sarahwilliams, Instagram: @sarahdesigns",
        title="Senior Graphic Designer"
    ),
    experience=[
        CompanyExperience(
            company="Creative Agency Inc.",
            roles=[
                Role(
                    title="Senior Graphic Designer",
                    start_date="2020-03",
                    end_date="Present",
                    description="Lead designer for major brand campaigns.",
                    achievements=[
                        "Designed rebrand for Fortune 500 company",
                        "Won 3 design awards in 2022",
                        "Managed design team of 4"
                    ]
                )
            ]
        )
    ],
    skills=[
        Skill(category="Design Software", name="Adobe Creative Suite (Photoshop, Illustrator, InDesign), Figma, Sketch"),
        Skill(category="Specialties", name="Brand Identity, UI/UX Design, Print Design, Motion Graphics")
    ],
    projects=[ # 'portfolio' can be represented as 'projects'
        Project(
            name="Nike Campaign Redesign",
            description="Complete visual identity overhaul for a major sports brand.",
            link="http://sarahwilliams.design/nike", # Ensure HttpUrl validity
            technologies=["Branding", "Adobe Illustrator", "Adobe Photoshop"]
        ),
        Project(
            name="Mobile App UI/UX",
            description="Designed user interface and experience for a new lifestyle app.",
            technologies=["Figma", "User Research", "Prototyping"]
        )
    ],
    awards=[ # list of strings
        "Best Brand Identity Design - Design Awards 2022",
        "Gold Medal for Digital Illustration - Creative Annual 2021"
    ]
    # education, certifications, etc. can be added as needed
)

# Generate PDF
try:
    pdf_path = generatepdf(
        cv_data=creative_data,
        output_path="sarah_williams_creative_cv.pdf",
        style="classic" # You might want a 'creative' style in the future
    )
    print(f"Creative CV generated at: {pdf_path}")
except Exception as e:
    print(f"Error generating creative CV: {e}")
```

## Recent Graduate Example (Python Data)

Tailored for a recent graduate, emphasizing education, projects, and internships.

```python
from generatecv.pdf_generator import generatepdf
from generatecv.models import CV, PersonalInfo, Education, Project, CompanyExperience, Role, Skill

graduate_data = CV(
    personal_info=PersonalInfo(
        name="Alex Rodriguez",
        email="alex.rodriguez@email.com",
        phone="+1 (555) 234-5678",
        location="Austin, TX",
        linkedin="https://linkedin.com/in/alexrodriguez",
        github="https://github.com/alexr",
        summary="Recent computer science graduate seeking an entry-level software engineering position. Eager to apply academic knowledge and internship experience to real-world challenges.",
        title="Aspiring Software Engineer"
    ),
    education=[
        Education(
            institution="University of Texas at Austin",
            degree="Bachelor of Science in Computer Science",
            location="Austin, TX",
            start_date="2019-08",
            end_date="2023-05",
            gpa="3.7/4.0",
            details="Honors: Dean's List, Magna Cum Laude. Relevant Coursework: Data Structures & Algorithms, Software Engineering, Database Systems, Machine Learning."
        )
    ],
    projects=[
        Project(
            name="E-commerce Web Application",
            description="Full-stack web app with user authentication and payment processing.",
            technologies=["React", "Node.js", "MongoDB", "Stripe API"],
            link="https://github.com/alexr/ecommerce-app", # Ensure HttpUrl validity
            achievements=[
                "Implemented responsive design for optimal viewing on all devices.",
                "Integrated secure payment system using Stripe API.",
                "Deployed on AWS Elastic Beanstalk."
            ],
            start_date="2022-09",
            end_date="2023-01"
        ),
        Project(
            name="Machine Learning Stock Predictor",
            description="Python application using LSTM networks for stock price prediction.",
            technologies=["Python", "TensorFlow", "Pandas", "NumPy"],
            link="https://github.com/alexr/stock-predictor" # Ensure HttpUrl validity
        )
    ],
    experience=[ # For internships
        CompanyExperience(
            company="StartupXYZ",
            location="Austin, TX (Remote)",
            roles=[
                Role(
                    title="Software Engineering Intern",
                    start_date="2022-06",
                    end_date="2022-08",
                    description="Developed new features and fixed bugs for the company's flagship mobile application.",
                    achievements=[
                        "Contributed to codebase with 50+ commits in an Agile environment.",
                        "Successfully fixed 15+ bugs and implemented 5 new features.",
                        "Collaborated with cross-functional teams including product and QA."
                    ]
                )
            ]
        )
    ],
    skills=[
        Skill(category="Programming Languages", name="Python, JavaScript, Java, C++"),
        Skill(category="Web Technologies", name="React, HTML/CSS, Node.js, Express.js"),
        Skill(category="Databases", name="MySQL, MongoDB, PostgreSQL"),
        Skill(category="Tools & Platforms", name="Git, Docker, AWS (Basic), VS Code")
    ]
)

# Generate PDF
try:
    pdf_path = generatepdf(
        cv_data=graduate_data,
        output_path="alex_rodriguez_graduate_cv.pdf",
        style="classic",
        page_size="letter" # Example of using 'letter' page size
    )
    print(f"Graduate CV generated at: {pdf_path}")
except Exception as e:
    print(f"Error generating graduate CV: {e}")

```

## Error Handling

When using `generatepdf` or `yamltocv`, it's good practice to include error handling.

```python
from generatecv.pdf_generator import generatepdf, yamltocv
from generatecv.models import CV, PersonalInfo # For basic data
from pydantic import ValidationError
import yaml # For yaml.YAMLError

# Example data (can be more complex)
sample_data = CV(
    personal_info=PersonalInfo(name="Test User", email="test@example.com"),
    education=[], # Must be provided, even if empty, as it's not optional in CV model
    experience=[] # Must be provided, even if empty
)

# --- Test generatepdf ---
try:
    # Intentionally using an invalid style to trigger ValueError
    generatepdf(cv_data=sample_data, output_path="error_test.pdf", style="non_existent_style")
except ValueError as e:
    print(f"Caught expected ValueError from generatepdf: {e}")
except Exception as e:
    print(f"Unexpected error from generatepdf: {e}")

# --- Test yamltocv ---
# Create a dummy valid YAML file
valid_yaml_content = """
personal_info:
  name: "YAML User"
  email: "yaml@example.com"
education: []
experience: []
"""
with open("temp_valid.yaml", "w") as f:
    f.write(valid_yaml_content)

# Create a dummy invalid YAML file (syntax error)
invalid_yaml_syntax = """
personal_info:
  name: Bad YAML
  email: bad@yaml: com # Invalid syntax
education: []
experience: []
"""
with open("temp_invalid_syntax.yaml", "w") as f:
    f.write(invalid_yaml_syntax)

# Create a dummy YAML with data validation issues
invalid_yaml_data = """
personal_info: # Missing name and email which are required
  phone: "12345"
education: []
experience: []
"""
with open("temp_invalid_data.yaml", "w") as f:
    f.write(invalid_yaml_data)

# Test yamltocv with a non-existent file
try:
    yamltocv(yaml_path="non_existent_file.yaml")
except FileNotFoundError as e:
    print(f"Caught expected FileNotFoundError from yamltocv: {e}")
except Exception as e:
    print(f"Unexpected error from yamltocv (non_existent_file): {e}")

# Test yamltocv with invalid YAML syntax
try:
    yamltocv(yaml_path="temp_invalid_syntax.yaml")
except yaml.YAMLError as e:
    print(f"Caught expected YAMLError from yamltocv: {e}")
except Exception as e:
    print(f"Unexpected error from yamltocv (invalid_syntax): {e}")

# Test yamltocv with data validation error
try:
    yamltocv(yaml_path="temp_invalid_data.yaml")
except ValidationError as e:
    print(f"Caught expected ValidationError from yamltocv: {e}")
except Exception as e:
    print(f"Unexpected error from yamltocv (invalid_data): {e}")

# Test yamltocv with valid file (should not raise an error here)
try:
    cv_obj = yamltocv(yaml_path="temp_valid.yaml")
    print(f"Successfully loaded CV data for: {cv_obj.personal_info.name}")
    # Optionally, generate PDF from this
    generatepdf(cv_data=cv_obj, output_path="cv_from_temp_valid_yaml.pdf")
    print("PDF generated from temp_valid.yaml")
except Exception as e:
    print(f"Error during valid yamltocv processing: {e}")

# Clean up temporary files (optional)
import os
os.remove("temp_valid.yaml")
os.remove("temp_invalid_syntax.yaml")
os.remove("temp_invalid_data.yaml")
```

These examples demonstrate various use cases and features of `generatecv` focusing on the `pdf_generator` and `models`. Adapt them to your specific needs. Remember that the `style` parameter currently only supports "classic", and `page_size` supports "A4" and "letter".