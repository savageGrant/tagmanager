# Taggit Component Specs

# Purpose of this document:
The purpose of the Component Design Specification is to describe the intended behavior and operation of the Taggit 
package's public classes and methods. This document does not contain technical details on how this behavior is achieved.

## taggit.py Module
This is the only Python module in the project and contains the primary ParentTag class, the class MacOSTagManager class 
and the OSManager class. The taggit module is imported with a “import taggit” command.

## taggit class ParentTag:
taggit.ParentTag is a class object that holds the name and color of a tag. The user creates
a ParentTag object by passing two parameters. A name string and a color string. 
ParentTags are also created using a pure string representation, and by passing a tuple containing
string representations of the name and color (str,str).
If a color is not provided when the class object is created then the color is defaulted to None.

When printed the ParentTag returns the string representation of the tag name.

The Tag object representation (__ repr__) is explicit and looks like Tag("Name", "Color").

When checking for equality, two separate tag objects with the same name and color evaluate as equal.

## taggit class OSManager
OSManager sets up the available OS managers via the register_manager() method. 
Once an OS manager is registered the OSManager can create an instance of that manager with the create method.
This class is intended to be used to set the intended OS manager to provide the correct methods to edit tags in that OS.

### OSManager method register_manager(key, manager)
Adds a key, value pair {key:manager} to the _managers dictionary.

### OSManager method create(key) 
Looks up a registered tag manager and creates a class object of the manager if it exits.

## taggit class MacOSTagManager
Manages the implementations of Taggit for MacOS. This class contains all the macOS specific parameters as well as all
the methods to interact with a masOS tag. The public methods are add_tag(), remove_tag(), remove_all_tags() and
get_tags().

### MacOSTagManager Nested Class Tag
The Tag class is nested in the MacOSTagManager and inherits from ParentTag and is the macOS representation of a tag. 
the object holds the name and color of the tag as well as the color_code. The user creates the Tag object by passing 
two parameters A name string and a color string. 

the string (__ str__) representation looks like "tag\ncolor_code" so if the tag name = test and the color_code = 4 
the string would be "test\n4".

### MacOSTagManager method add_tag(tag, file)
the add_tag method accepts a tag or list of tags and a file path. It applies the tags to the
file without adding duplicate tags or removing existing tags.

### MacOSTagManager method remove_tag(tag, file):
the remove_tag method accepts a tag or list of tags and a file path. It removes the tags from
the file without generating an error if the passed tag(s) don't exist. It only removes tags that are specified.

### MacOSTagManager method remove_all_tags(file)
The remove_all_tags method accepts a file path and removes all existing tags from that file.

### MacOSTagManager method get_tags(file)
The get_tags method accepts a file path and returns a list of tags that are on the file.



Author: Grant Savage
