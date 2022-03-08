# Taggit Functional Specifications

## Purpose of this document:
The purpose of the Functional Design Specification is to describe the intended behavior and operation of the Taggit 
package's public classes and methods. This document does not contain technical details on how this behavior is achieved.

### taggit.Tag:
taggit.Tag is a class object that holds the name, color, and color code of a tag. The user should be able to create
a Tag object by passing two parameters. A name string and either a color string or color code representation 
of a color. Tags should also be able to be created using a pure string representation, and by passing a tuple containing
string representations of the name and color (str,str).
If a color or color code is not provided when the class object is created then the color should be defaulted to None.

When printed the Tag should return the exact string representation that is used to store the tag in the OS. For Mac OSX
this looks like "tag\ncolor_code" so if the tag name = test and the color_code = 4 the string would be "test\n3".

The Tag object representation (__ repr__) should be explicit and should look like Tag("Name", "Color").

When checking for equality, two separate tag objects with the same name and color should evaluate as equal.

### taggit.add_tag(tag, file)
the taggit.add_tag function should accept a tag or list of tags and a file path. It should apply the tags to the
file without adding duplicate tags or removing existing tags.

### taggit.remove_tag(tag, file, remove_all=False):
the taggit.remove_tag function should accept a tag or list of tags and a file path. It should remove the tags from
the file without generating an error if the passed tag(s) don't exist. It should only remove tags that are specified.

### taggit.remove_all_tags(file)
The taggit.remove_all_tags function should accept a file path and remove all existing tags from that file.

### taggit.get_tags(file)
The taggit.get_tags function should accept a file path and return a list of tags that are on the file.



Author: Grant Savage