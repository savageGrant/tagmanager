# tagmanager
### A Python library for tagging files.
#### Author: Grant Savage
## Installation

```zsh
pip install tagmanager
```

## Current Package Limitations
This package currently works on Mac OS X 10.9 and newer. It was developed on Mac OS X 12.2
There is currently no functionality for Linux or Windows.

## Package Structure
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

## Tutorial

Add tag to file:

```python
from tagmanager import tag_manager as tm

>> > file_location = "sample_folder/sample_file.txt"

# Add tag via Tag object
>> > tag = tm.Tag(name="green_tag", color="green")

>> > tm.add_tag(tag, file_location)

# Add tag via string
>> > tm.add_tag("blue_tag\nblue", file_location)

# Add colorless tag via string
>> > tm.add_tag("no_color_tag", file_location)

# Add tag via tuple
>> > tm.add_tag(("purple_tag", 'purple'), file_location)

# Add multiple tags via list of tuples
>> > red_list = [('first_red', 'red'), ('second_red', 'red')]

>> > tm.add_tag(red_list, file_location)
```

Return tags by file:

```python
>>> tm.get_tags(file_location)
[Tag("blue_tag", "BLUE"), Tag("green_tag", "GREEN"), Tag("no_color_tag", "NONE"), Tag("purple_tag", "PURPLE"), Tag("first_red", "RED"), Tag("second_red", "RED")]
```

Remove tags from file:

```python
# Remove tag via Tag object
>>> blue_tag = tm.Tag("blue_tag", "blue")

>>> tm.remove_tag(blue_tag, file_location)

# Remove tag via string
>>> tm.remove_tag("green_tag\ngreen", file_location)

# Remove colorless tag via string
>>> tm.remove_tag("no_color_tag", file_location)

# Remove tag via tuple
>>> tm.remove_tag(("purple_tag", "purple"), file_location)

# Remove multiple tags via list of tuples
>>> red_list = [('first_red', 'red'), ('second_red', 'red')]

>>> tm.remove_tag(red_list, file_location)

# Adding one tag back to show tags were removed
>>> tm.add_tag("new_tag", file_location)

>>> tm.get_tags(file_location)
[Tag("new_tag", "NONE")]

```
