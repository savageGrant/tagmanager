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
    assert taggit.Tag.from_string("test_tag\n1") == taggit.Tag("test_tag", "1")
    assert taggit.Tag.from_string("test_tag\n1") == taggit.Tag("test_tag", 1)
    assert taggit.Tag.from_string("test_tag\nRed") == taggit.Tag("test_tag", "Red")
    assert taggit.Tag.from_string("test_tag\nBlue") == taggit.Tag("test_tag", 4)
    assert taggit.Tag.from_string("test_tag") == taggit.Tag("test_tag", "None")
    assert taggit.Tag.from_string("test_tag") == taggit.Tag("test_tag", 0)


def test_create_tag_from_tuple():
    # Tests for Mac OSx
    taggit._OPERATING_SYSTEM = 'Darwin'
    assert taggit.Tag.from_tuple(("test_tag", "1")) == taggit.Tag("test_tag", "1")
    assert taggit.Tag.from_tuple(("test_tag", 1)) == taggit.Tag("test_tag", 1)
    assert taggit.Tag.from_tuple(("test_tag", "Red")) == taggit.Tag("test_tag", "Red")
    assert taggit.Tag.from_tuple(("test_tag", "Blue")) == taggit.Tag("test_tag", 4)
    assert taggit.Tag.from_tuple(("test_tag",)) == taggit.Tag("test_tag", 0)
