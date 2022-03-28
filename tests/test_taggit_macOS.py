import difflib
import unittest
from unittest.mock import patch

import pytest
from pytaggit import taggit
from pytaggit import tag_manager as tm
import pytaggit

pytaggit.OPERATING_SYSTEM = 'Windows'


def test_raise_an_error_on_unsupported():
    with pytest.raises(RuntimeError):
        pytaggit._os_check()


def test_parenttag_name_color():
    tag = taggit.ParentTag("testtag", "red")
    assert tag.color == "red"
    assert tag.name == "testtag"


def test_parentag_str():
    tag = taggit.ParentTag("testtag", "red")
    assert str(tag) == "testtag"


def test_parenttag_repr():
    tag = taggit.ParentTag("testtag", "blue")
    assert repr(tag) == 'Tag("testtag", "blue")'


def test_parenttag_equality():
    tag = taggit.ParentTag("testtag", "blue")
    second_tag = taggit.ParentTag("testtag", "blue")
    assert tag == second_tag

def test_parrenttag_inequality():
    tag = taggit.ParentTag("test", "red")
    not_tag = {"name": "tester"}
    assert tag != not_tag


def test_mac_tag_inequality():
    tag = tm.Tag("test", "red")
    not_tag = {"name": "tester"}
    assert tag != not_tag


def test_mac_map_color_to_string_warning():
    tag = tm.Tag("test", "17")
    secondtag = tm.Tag('test', "rainbow")
    assert tag.color_code == 0
    assert secondtag.color_code == 0


def test_mac_add_tag_by_list():
    test_file = 'tests/test_file.txt'
    tm.remove_all_tags(test_file)
    tag_list = [('t1', 'red'), ('t2', 'blue'), ('t3', 'purple')]
    tm.add_tag(tag_list, test_file)
    assert tm.get_tags(test_file) == \
           [tm.Tag("t1", "red"), tm.Tag("t2", "blue"), tm.Tag('t3', 'purple')]
    tm.remove_all_tags(test_file)


# def test_mac_add_tag_bad_type():
#     test_file = 'tests/test_file.txt'
#     bad_tag = {'not': 'supported'}
#     tm.add_tag(bad_tag, test_file)
#     assert tm.get_tags(test_file) == []


def test_remove_tag_with_list():
    test_file = 'tests/test_file.txt'
    tm.remove_all_tags(test_file)
    tag_list = [('t1', 'red'), ('t2', 'blue'), ('t3', 'purple')]
    tm.add_tag(tag_list, test_file)


def test_create_tag_from_string():
    # Tests for Mac OSx
    assert tm.Tag.from_string("testtag\n1") == tm.Tag("testtag", "1")
    assert tm.Tag.from_string("tag\n1") == tm.Tag("tag", 1)
    assert tm.Tag.from_string("tag\nRed") == tm.Tag("tag", "Red")
    assert tm.Tag.from_string("tag\nBlue") == tm.Tag("tag", 4)
    assert tm.Tag.from_string("tag") == tm.Tag("tag", "None")
    assert tm.Tag.from_string("tag") == tm.Tag("tag", 0)


def test_create_tag_from_tuple():
    # Tests for Mac OSx
    assert tm.Tag.from_tuple(("tag", "1")) == tm.Tag("tag", "1")
    assert tm.Tag.from_tuple(("tag", 1)) == tm.Tag("tag", 1)
    assert tm.Tag.from_tuple(("tag", "Red")) == tm.Tag("tag", "Red")
    assert tm.Tag.from_tuple(("tag", "Blue")) == tm.Tag("tag", 4)
    assert tm.Tag.from_tuple(("tag",)) == tm.Tag("tag", 0)


def test_remove_tag():
    # Tests for Mac OSx
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
    str(tm.Tag('Red_tag', 'red')) == 'Red_tag\n6'