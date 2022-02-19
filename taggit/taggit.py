from enum import Enum
from typing import Tuple, ClassVar
from xattr import xattr
from biplist import writePlistToString, readPlistFromString


class Color(Enum):
    NONE = 0
    GRAY = 1
    GREEN = 2
    PURPLE = 3
    BLUE = 4
    YELLOW = 5
    RED = 6
    ORANGE = 7

    def __str__(self) -> str:
        return str(self.value)


class Tag:
    """
    accepts name and color of the tag
    """
    name: str
    color: Color = Color.NONE
    tag_locations: ClassVar[Tuple['str', 'str']] = ('com.apple.metadata:_kMDItemUserTags', 'com.apple.metadata:kMDItemOMUserTags')

    def __init__(self, file_volume):
        self.xattr = xattr(file_volume)
