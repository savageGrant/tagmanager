# Taggit Design Specifications

## Purpose of this document:
Define the high-level design decisions of the project as well as the lower-level design style and standards that are followed and enforced.

## Package Structure
The package structure adheres to popular convention.

```
taggit
|   README.md
|   LICENSE
|   .gitignore
|   poetry.lock
|   pyproject.toml
|───taggit
|   |   __init__.py
|   |   taggit.py
|───tests
|   |   test_taggit.py
|───docs
|   |   Functional_Specs.md
|   |   Design_Specs.md
|───sample_folder
|   |   sample_file.txt
```

## High level design decisions



## Style and standards

### Formatting and Style
PEP 8 is followed and enforced via Flake8.

The Zen of Python (PEP 20) is channeled and often reflected upon, but not enforced.

### Documentation
Docstrings are used and required for all public and private classes, methods and functions.
Multi-line docstrings are expected, single line docstrings should only be used when functionality
is remarkably obvious (developer's discretion).

Comments should be kept to a minimum and only used when functionality is non-obvious. In-line comments preferred.

The README contains high level information and examples for getting started with this package.

Other documentation files are stored in the /docs directory. This shouldn't be surprising, you're in it right now!

### Testing
Tests are stored in the tests directory and test code-coverage is maintained at 100%. 
Pytest is used in tandem with Coverage via the pytest-cov pluggin.
```zsh
pytest --cov=taggit tests/    
```
### Dependency Management and Packaging
This project specifies build dependencies with pyproject.toml in accordance with PEP 518 
and uses Poetry to help orchestrate the project and its dependencies.


Author: Grant Savage