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

## Problem Addressed

The current OS X tagging capability is not automated and not sustainable on a large scale. 
A user has to manually adding tags one-by-one via OSx UI, a user can add a single tag to multiple files in the same 
directory in one action, however the user still has to manually select the desired files and add tags one at a time.

### Motivation for Data-Science
Model development is often done locally.
Small-to-medium problems can often be trained locally, and large problems can be built with sample 
data before training on more expensive compute. There can be various data and data iterations that are used and created 
during model building, training and evaluation. Currently, file management is done by directory or by appending prefix 
or suffix keys to file names. Tags are often a better solution.

Tags allow for directory-based search but also allow the user to cast a fast wide-net search. This capability can be 
powerful when a developer or data scientist wants to quickly retrieve like-files from multiple projects.git

#### Use-Case 1
Return all feature engineering files that contain a key feature. If I tag each fe_helper.py file I have with string
representations of a key features I can quickly find them and more easily reuse code from past projects.

#### Use-Case 2
Another use case (how I use tags daily) is to tag class files by type and organize them by week. 
This allows me to search by homework if I want to search for all homework from multiple weeks.

## High level design decisions

Focus on flexibility. Users should be able to create a tag successfully as long as they pass an interpretable value.
I do not want to force a single acceptable way of creating.

Tags should be able to be added without explicit creation of a tag object.

The design should allow for future expansion to multiple OS environments. Nothing passed by the user should be OS specific.

Cognative load should be reduced whenever possible. Each method and function should clearly state its functionality via
the name. Docstrings are non-negotiable.

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