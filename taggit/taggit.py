import sys
from enum import Enum
import xattr
import plistlib
import warnings
from platform import system
from biplist import writePlistToString, readPlistFromString

_OPERATING_SYSTEM = system()

if _OPERATING_SYSTEM == 'Darwin':
    TAG_LOCATION = 'com.apple.metadata:_kMDItemUserTags'
    FINDER_INFO = "com.apple.FinderInfo"
    _COLOR_TO_CODE_MAPPING = {
        'NONE': 0,
        'GRAY': 1,
        'GREEN': 2,
        'PURPLE': 3,
        'BLUE': 4,
        'YELLOW': 5,
        'RED': 6,
        'ORANGE': 7
    }
    _CODE_TO_COLOR_MAPPING = {v: k for k, v in _COLOR_TO_CODE_MAPPING.items()}
    _COLOR_STRING = "[Gray, Green, Purple, Blue, Yellow, Red, Orange]"


class Tag:
    """
    accepts name and color of the tag
    """

    def __init__(self, name, color):
        self.name = name
        self.color = self._map_color_to_string(color)
        self.color_code = self._map_color_to_code(color)

    def __str__(self):
        return f"{self.name}\n{self.color_code}"

    def __repr__(self):
        return f'Tag("{self.name}", "{self.color}")'

    @staticmethod
    def _map_color_to_string(color):
        if str(color).isnumeric():
            if int(color) in _CODE_TO_COLOR_MAPPING:
                return _CODE_TO_COLOR_MAPPING[int(color)]
            else:
                warnings.warn("""The number {} does not map to an available color not. Please select a 
                          mapping from {}""".format(color, _CODE_TO_COLOR_MAPPING))
                return _CODE_TO_COLOR_MAPPING[0]
        else:
            if color.upper() in _COLOR_TO_CODE_MAPPING:
                return color.upper()
            else:
                warnings.warn(f"The color {color} is not available, NONE was used. Valid colors are: {_COLOR_STRING}")
                return 'NONE'

    @staticmethod
    def _map_color_to_code(color):
        if not str(color).isnumeric():
            if color.upper() in _COLOR_TO_CODE_MAPPING:
                return _COLOR_TO_CODE_MAPPING[color.upper()]
            else:
                warnings.warn(f"The color {color} is not available, NONE was used. Valid colors are: {_COLOR_STRING}")
                return _COLOR_TO_CODE_MAPPING['NONE']
        else:
            if int(color) in _CODE_TO_COLOR_MAPPING:
                return color
            else:
                warnings.warn("""The color code {} is not available. Please select a 
                              valid code from {}""".format(color, _CODE_TO_COLOR_MAPPING))
                return 0

    @classmethod
    def from_string(cls, string_tag: str):
        if '\n' in string_tag:
            name, color = string_tag.splitlines()
            return Tag(name, color)
        else:
            return Tag(string_tag, 'NONE')

    @classmethod
    def from_tuple(cls, tup):
        return cls(tup[0], tup[1])


def _generate_tag(tag) -> Tag:
    if isinstance(tag, str):
        return Tag.from_string(tag)
    elif isinstance(tag, tuple):
        return Tag.from_tuple(tag)
    else:
        return tag


def _delete_existing_finder_info(file):
    if FINDER_INFO in xattr.listxattr(file):
        xattr.removexattr(file, FINDER_INFO)


def _get_raw_tags(file: str):
    """List the tags on the `file`."""
    if _OPERATING_SYSTEM == 'Darwin':
        try:
            tag_list = xattr.getxattr(file, TAG_LOCATION)
            # for location in TAG_LOCATIONS:
            #     try:
            #         tag_list.append(xattr.getxattr(file, location))
            #     except OSError:
            #         pass
            # tag_list = list(set(x for x in tag_list))
        except OSError:
            return []
        return plistlib.loads(tag_list)
    else:
        return []


def get_tags(file):
    return [Tag.from_string(tag) for tag in _get_raw_tags(file)]


def _set_tags(tags, file):
        """Add tags to a file"""
        if _OPERATING_SYSTEM == 'Darwin':
            _delete_existing_finder_info(file)
            tags = [str(t) if isinstance(t, Tag) else str(Tag.from_string(t)) for t in tags]
            plist = plistlib.dumps(tags)
            xattr.setxattr(file, TAG_LOCATION, plist)


def add_tag(tag, file) -> None:
    """Add tag(s) to `file`."""
    if isinstance(tag, list):
        tag_list = [_generate_tag(t) for t in tag]
    else:
        try:
            tag_list = [_generate_tag(tag)]
        except TypeError:
            sys.exit(1)
    tags = _get_raw_tags(file)
    for tag in tag_list:
        if str(tag) not in tags:
            tags.append(str(tag))
    _set_tags(tags, file)


def remove_tag(tag, file, remove_all=False) -> None:
        """Remove tag(s) from `file`."""
        if remove_all:
            _set_tags([], file)
        else:
            if isinstance(tag, list):
                tag_list = [_generate_tag(t) for t in tag]
            else:
                try:
                    tag_list = [_generate_tag(tag)]
                except TypeError:
                    sys.exit(1)
            tags = _get_raw_tags(file)
            for tag in tag_list:
                if str(tag) in tags:
                    tags.pop(tags.index(str(tag)))
            _set_tags(tags, file)
