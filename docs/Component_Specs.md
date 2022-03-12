# Taggit Component Specs

## Purpose of this document:
The purpose of the Component Design Specification is to describe the intended behavior and operation of the Taggit 
package's public classes and methods. This document does not contain technical details on how this behavior is achieved.

### taggit.py Module
This is the only Python module in the project and contains the primary Tag class as well as all the public and private 
methods and functions. The taggit module is imported with a “import taggit” command.


### taggit.Tag:
taggit.Tag is a class object that holds the name, color, and color code of a tag. The user creates
a Tag object by passing two parameters. A name string and either a color string or color code representation 
of a color. Tags are also created using a pure string representation, and by passing a tuple containing
string representations of the name and color (str,str).
If a color or color code is not provided when the class object is created then the color is defaulted to None.

When printed the Tag returns the exact string representation that is used to store the tag in the OS. For Mac OSX
this looks like "tag\ncolor_code" so if the tag name = test and the color_code = 4 the string would be "test\n3".

The Tag object representation (__ repr__) is explicit and looks like Tag("Name", "Color").

When checking for equality, two separate tag objects with the same name and color evaluate as equal.

### taggit.add_tag(tag, file)
the taggit.add_tag function accepts a tag or list of tags and a file path. It applies the tags to the
file without adding duplicate tags or removing existing tags.

### taggit.remove_tag(tag, file):
the taggit.remove_tag function accepts a tag or list of tags and a file path. It removes the tags from
the file without generating an error if the passed tag(s) don't exist. It only removes tags that are specified.

### taggit.remove_all_tags(file)
The taggit.remove_all_tags function accepts a file path and removes all existing tags from that file.

### taggit.get_tags(file)
The taggit.get_tags function accepts a file path and returns a list of tags that are on the file.



Author: Grant Savage