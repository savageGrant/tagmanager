import difflib
import unittest
from unittest.mock import patch

import pytest

import taggit


def test_raise_an_error_on_unsupported():
    taggit.OPERATING_SYSTEM = 'Windows'
    with pytest.raises(RuntimeError):
        taggit._os_check()


def test_create_tag_from_string():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    assert taggit.Tag.from_string("tag\n1") == taggit.Tag("tag", "1")
    assert taggit.Tag.from_string("tag\n1") == taggit.Tag("tag", 1)
    assert taggit.Tag.from_string("tag\nRed") == taggit.Tag("tag", "Red")
    assert taggit.Tag.from_string("tag\nBlue") == taggit.Tag("tag", 4)
    assert taggit.Tag.from_string("tag") == taggit.Tag("tag", "None")
    assert taggit.Tag.from_string("tag") == taggit.Tag("tag", 0)


def test_create_tag_from_tuple():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    assert taggit.Tag.from_tuple(("tag", "1")) == taggit.Tag("tag", "1")
    assert taggit.Tag.from_tuple(("tag", 1)) == taggit.Tag("tag", 1)
    assert taggit.Tag.from_tuple(("tag", "Red")) == taggit.Tag("tag", "Red")
    assert taggit.Tag.from_tuple(("tag", "Blue")) == taggit.Tag("tag", 4)
    assert taggit.Tag.from_tuple(("tag",)) == taggit.Tag("tag", 0)


def test_remove_tag():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    taggit.remove_all_tags('test_file.txt')
    taggit.add_tag(("tag", "red"), 'test_file.txt')
    taggit.add_tag(("tag", "blue"), 'test_file.txt')
    assert taggit.get_tags('test_file.txt') == \
           [taggit.Tag("tag", "red"), taggit.Tag("tag", "blue")]
    taggit.remove_tag(('tag', 'red'), 'test_file.txt')
    assert taggit.get_tags('test_file.txt') == [taggit.Tag("tag", "blue")]