from setuptools import setup, find_packages

setup(
    name="generatecv",
    version="0.1.0",
    description="A Python package for generating professional CVs from structured data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="yantology",
    author_email="work@yantology.dev",
    url="https://github.com/yourusername/generatecv",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.13",
    install_requires=[
        "pydantic>=2.11.5",
        "pyyaml>=6.0.2",
        "reportlab>=4.4.1",
    ],
    entry_points={
        "console_scripts": [
            "generatecv-example=tool.main:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest>=8.3.5",
            "pytest-cov>=4.1.0",
            "mypy>=1.5.1",
            "ruff>=0.1.5",
            "black>=23.9.1",
            "types-PyYAML>=6.0.12.12",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
    package_data={
        "generatecv": ["py.typed"],
    },
)
