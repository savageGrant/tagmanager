import difflib
import unittest
from unittest.mock import patch

import pytest
import taggit
from taggit import tag_manager as tm


def test_raise_an_error_on_unsupported():
    taggit.OPERATING_SYSTEM = 'Windows'
    with pytest.raises(RuntimeError):
        taggit._os_check()


def test_create_tag_from_string():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    assert tm.Tag.from_string("testtag\n1") == tm.Tag("testtag", "1")
    assert tm.Tag.from_string("tag\n1") == tm.Tag("tag", 1)
    assert tm.Tag.from_string("tag\nRed") == tm.Tag("tag", "Red")
    assert tm.Tag.from_string("tag\nBlue") == tm.Tag("tag", 4)
    assert tm.Tag.from_string("tag") == tm.Tag("tag", "None")
    assert tm.Tag.from_string("tag") == tm.Tag("tag", 0)


def test_create_tag_from_tuple():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    assert tm.Tag.from_tuple(("tag", "1")) == tm.Tag("tag", "1")
    assert tm.Tag.from_tuple(("tag", 1)) == tm.Tag("tag", 1)
    assert tm.Tag.from_tuple(("tag", "Red")) == tm.Tag("tag", "Red")
    assert tm.Tag.from_tuple(("tag", "Blue")) == tm.Tag("tag", 4)
    assert tm.Tag.from_tuple(("tag",)) == tm.Tag("tag", 0)


def test_remove_tag():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    test_file = 'tests/test_file.txt'
    tm.remove_all_tags(test_file)
    tm.add_tag(("tag", "red"), test_file)
    tm.add_tag(("tag", "blue"), test_file)
    assert tm.get_tags(test_file) == \
           [tm.Tag("tag", "red"), tm.Tag("tag", "blue")]
    tm.remove_tag(('tag', 'red'), test_file)
    assert tm.get_tags(test_file) == [tm.Tag("tag", "blue")]

def test_str_representation_tag_object():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    str(tm.Tag('Red_tag', 'red')) == 'Red_tag\n6'