# tagmanager Functional Design Specifications

## Purpose of this document:
Define the high-level design decisions of the project as well as the lower-level design style and standards that are followed and enforced.

## Package Structure
The package structure adheres to popular convention.

```
tagmanager
|   README.md
|   LICENSE
|   .gitignore
|   poetry.lock
|   pyproject.toml
|───tagmanager
|   |   __init__.py
|   |   tagmanager.py
|───tests
|   |   test_tagmanager_macOS.py
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
Tag each feature engineering helper file with string representations of the key features of the model.
I can then quickly return all feature engineering files that contain a key feature allowing me to more 
easily reuse code from past projects.

#### Use-Case 2
Another use case (how I use tags daily) is to tag class files by type and organize them by week. 
This allows me to search by homework if I want to search for all homework from multiple weeks.

#### Use-Case 3
Remove tags for dated projects or invalidated assumptions.

## High level design decisions

My primary design consideration has been to focus on flexibility. What I mean by flexibility is that whenever possible,
methods should “just work”. Users should be able to create a tag successfully by passing a variety of interpretable
values (strings, lists, tuples). I do not want to enforce a single acceptable way of creating a tag. Tags should be
able to be added without explicit creation of a tag object. 

Another import design consideration is allowing for future expansion to multiple OS environments. Nothing passed by 
the user should be required to be OS specific for functionality to work. This is achieved with a factory method pattern
design.

Cognitive load should be reduced whenever possible. Each method and function should clearly state its functionality 
via naming convention. Docstrings are non-negotiable. Class docstrings should provide information about the attributes, 
methods, and final class object. Function and method docstrings should provide a one-liner as well as parameter and 
return object information.

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
Pytest is used in tandem with Coverage via the pytest-cov plugin.
```zsh1
pytest --cov=tagmanager tests/    
```
### Dependency Management and Packaging
This project specifies build dependencies with pyproject.toml in accordance with PEP 518 
and uses Poetry to help orchestrate the project and its dependencies.


Author: Grant Savage
