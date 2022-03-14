import sys
import warnings
import plistlib

import xattr


class ParentTag:
    """Returns a ParentTag object.

    Attributes
    ----------
    name : Str representation of the tag name
    color : Str representation of color.

    Methods
    --------
    from_string(cls, string_tag: str)
    from_tuple(cls, tup)
    """

    def __init__(self, name, color):
        """Constructs a ParentTag object.

        Parameters
        ----------
        name : str representation of the tag name
        color : Str representation of color.
        """
        self.name = name
        self.color = self.color

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'Tag("{self.name}", "{self.color}")'

    def __eq__(self, other):
        if not isinstance(other, self.Tag):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.color == other.color

    @classmethod
    def from_string(cls, string_tag: str):
        """Parses string and calls the Tag constructor. Returns a Tag object.

        Parameters
        ----------
        string_tag : str representation of the tag to be created.

        Returns
        -------
        Tag object
        """
        if '\n' in string_tag:
            name, color = string_tag.splitlines()
            return cls(name, color)
        else:
            return cls(string_tag, 'NONE')

    @classmethod
    def from_tuple(cls, tag_tup):
        """Parses tuple and calls the Tag constructor. Returns a Tag object.

        Parameters
        ----------
        tag_tup : tuple representation of the tag to be created.

        Returns
        -------
        Tag object
        """
        if len(tag_tup) == 1:
            return cls(tag_tup[0], 'NONE')
        else:
            return cls(tag_tup[0], tag_tup[1])


class MacOSTagManager():
    """Manages the implementations of Taggit for MacOS

    Attributes
    ----------
    TAG_LOCATION: string representation of where macOS stores tags
    FINDER_INFO: string representation of where finder info is stored on macOS

    Classes
    --------
    Tag: macOS specific implementation the of parent class ParentTag.

    Methods
    --------
    get_tags(cls, file)
    add_tag(cls, tag, file)
    remove_all_tags(cls, file)
    remove_tag(cls, tag, file)
    _get_raw_tags(cls, file)
    _delete_existing_finder_info(cls, file)
    _set_tags(cls, tags, file)
    _generate_tag(cls, tag)
    """

    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = MacOSTagManager()
        return self._instance

    TAG_LOCATION = 'com.apple.metadata:_kMDItemUserTags'
    FINDER_INFO = "com.apple.FinderInfo"

    class Tag(ParentTag):
        """Returns a Tag object.

        Attributes
        ----------
        name : Str representation of the tag name.
        color : Str representation of color.
        color_code: Int representation of the color_code mapping.

        _COLOR_TO_CODE_MAPPING: Dict with color keys and code values.
        _CODE_TO_COLOR_MAPPING: Dict with code keys and color values.
        _COLOR_STRING: String of all valid colors.

        Methods
        --------
        _map_color_to_string(cls, color)
        _map_color_to_code(cls, color)
        """

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

        def __init__(self, name, color):
            """Constructs a Tag object.
            Inherits from ParentTag
            Parameters
            ----------
            name : str representation of the tag name
            color : Str representation of color.
            """
            self.name = name
            self.color = self._map_color_to_string(color)
            self.color_code = self._map_color_to_code(color)

        def __str__(self):
            return f"{self.name}\n{self.color_code}"

        # def __repr__(self):
        #     return f'Tag("{self.name}", "{self.color}")'

        def __eq__(self, other):
            if not isinstance(other, ParentTag):
                # don't attempt to compare against unrelated types
                return NotImplemented

            return self.name == other.name and self.color == other.color \
                   and self.color_code == other.color_code

        @classmethod
        def _map_color_to_string(cls, color):
            """Returns a color string representation given an input.

            Parameters
            ----------
            color : Str or Int representation of color.
                    Can be a "color code" or a "color".

            Returns
            -------
                Str: Str representation of a color in English.
                Returns "NONE" if no valid color is passed as input.
            """
            if str(color).isnumeric():
                if int(color) in cls._CODE_TO_COLOR_MAPPING:
                    return cls._CODE_TO_COLOR_MAPPING[int(color)]
                else:
                    warnings.warn(f"The number {color} does not map "
                                  f"to an available color not."
                                  f"Please select a mapping "
                                  f"from {cls._CODE_TO_COLOR_MAPPING}")
                    return cls._CODE_TO_COLOR_MAPPING[0]
            else:
                if color.upper() in cls._COLOR_TO_CODE_MAPPING:
                    return color.upper()
                else:
                    warnings.warn(f"The color {color} is not available, NONE "
                                  f"was used. Valid colors are: {cls._COLOR_STRING}")
                    return 'NONE'

        @classmethod
        def _map_color_to_code(cls, color):
            """Returns a color_code int representation given an input.

            Parameters
            ----------
            color : Str or Int representation of color.
                    Can be a "color code" or a "color".

            Returns
            -------
                Int: integer representation of a color_code.
                Returns 0 if no valid color is passed as input.
            """
            if not str(color).isnumeric():
                if color.upper() in cls._COLOR_TO_CODE_MAPPING:
                    return cls._COLOR_TO_CODE_MAPPING[color.upper()]
                else:
                    warnings.warn(f"The color {color} is not available, NONE "
                                  f"was used. Valid colors are: {cls._COLOR_STRING}")
                    return cls._COLOR_TO_CODE_MAPPING['NONE']
            else:
                if int(color) in cls._CODE_TO_COLOR_MAPPING:
                    return int(color)
                else:
                    warnings.warn(f"Color code {color} is not available. Select "
                                  f"a valid code from {cls._CODE_TO_COLOR_MAPPING}")
                    return 0


    @classmethod
    def get_tags(cls, file):
        """Gets Tag(s) associated with a file.

        Parameters
        ----------
        file: a string representation of the file location
        """
        return [cls.Tag.from_string(tag) for tag in cls._get_raw_tags(file)]

    @classmethod
    def add_tag(cls, tag, file) -> None:
        """Adds Tag(s) to a file.

        Parameters
        ----------
        tag : a tag or list of the tags
        file: a string representation of the file location
        """
        if isinstance(tag, list):
            tag_list = [cls._generate_tag(t) for t in tag]
        else:
            try:
                tag_list = [cls._generate_tag(tag)]
            except TypeError:
                sys.exit(1)
        tags = cls._get_raw_tags(file)
        for tag in tag_list:
            if str(tag) not in tags:
                tags.append(str(tag))
        cls._set_tags(tags, file)

    @classmethod
    def remove_all_tags(cls, file) -> None:
        """Removes all Tags from a file.

        Parameters
        ----------
        file: a string representation of the file location
        """
        cls._set_tags([], file)

    @classmethod
    def remove_tag(cls, tag, file) -> None:
        """Removes Tag(s) from a file.

        Parameters
        ----------
        tag : a tag or list of the tags to remove
        file: a string representation of the file location
        """
        if isinstance(tag, list):
            tag_list = [cls._generate_tag(t) for t in tag]
        else:
            try:
                tag_list = [cls._generate_tag(tag)]
            except TypeError:
                sys.exit(1)
        tags = cls._get_raw_tags(file)
        for tag in tag_list:
            if str(tag) in tags:
                tags.pop(tags.index(str(tag)))
        cls._set_tags(tags, file)

    @classmethod
    def _get_raw_tags(cls, file: str):
        """List the tags on the file.

        Parameters
        ----------
        file: a string representation of the file location
        """

        try:
            tag_list = xattr.getxattr(file, cls.TAG_LOCATION)
        except OSError:
            return []
        return plistlib.loads(tag_list)

    @classmethod
    def _delete_existing_finder_info(cls, file):
        """removes existing finder info.

        Parameters
        ----------
        file: a string representation of the file location
        """
        if cls.FINDER_INFO in xattr.listxattr(file):
            xattr.removexattr(file, cls.FINDER_INFO)

    @classmethod
    def _set_tags(cls, tags, file):
        """Adds Tag(s) to a file.

        Parameters
        ----------
        tags : a list of the tags to add
        file: a string representation of the file location
        """
        cls._delete_existing_finder_info(file)
        tags = [str(t) if isinstance(t, cls.Tag)
                else str(cls.Tag.from_string(t)) for t in tags]
        plist = plistlib.dumps(tags)
        xattr.setxattr(file, cls.TAG_LOCATION, plist)

    @classmethod
    def _generate_tag(cls, tag) -> Tag:
        """calls appropriate Tag constructor and returns Tag object.

        Parameters
        ----------
        tag : a representation of the tag to be created

        Returns
        -------
        Tag object
        """
        if isinstance(tag, str):
            return cls.Tag.from_string(tag)
        elif isinstance(tag, tuple):
            return cls.Tag.from_tuple(tag)
        else:
            return tag


class OSManager:
    """Manages the implementations of Taggit for each OS.

    Attributes
    ----------
    _managers : Dictionary to be populated with the relevant OS manager

    Methods
    --------
    register_manager(self, key, manager)
    create(self, key, **kwargs)
    """
    def __init__(self):
        self._managers = {}

    def register_manager(self, key, manager):
        """adds a key, value pair to the _managers dictionary.

        Parameters
        ----------
        key : string representation of the key to be created.
              It should be a string representation of an OS.
        manager: manager class to use
        """
        self._managers[key] = manager

    def create(self, key, **kwargs):
        """creates a class object of a tag manager.

        Parameters
        ----------
        key : string representation of the key to look up.
              It should be a string representation of an OS.

        Returns
        -------
        Class object of the OS Manager found by the key value.
        """
        manager = self._managers.get(key)
        if not manager:
            raise ValueError(key)
        return manager(**kwargs)






