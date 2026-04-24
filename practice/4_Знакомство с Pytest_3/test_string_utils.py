from operator import contains

import pytest
from string_utils import StringUtils


string_utils = StringUtils()

#1test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



#2test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ('    skypro', 'skypro'),
    ('    hello world', 'hello world'),
    (' python', 'python'),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('', ''),
    ('    ', ''),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected



#3test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, sumbool, expected", [
    ('Skypro', 'S', True),
    ('Skypro', 'p', True ),
    ('123abc', '1', True)
])
def test_contains_positive(input_str, sumbool, expected):
    assert string_utils.contains(input_str, sumbool) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, sumbool, expected", [
    ('Skypro', 'e', False),
    ('', 'A', False),
    ('123', '4', False),
])
def test_contains_negative(input_str, sumbool, expected):
    assert string_utils,contains(input_str, sumbool) == expected


#test4
@pytest.mark.positive
@pytest.mark.parametrize('input_str, sumbool, expected', [
    ('Skypro', 'k', 'Sypro'),
    ('Skypro', 'Sky', 'pro'),
    ('aaa', 'a', ''),
])
def test_delete_sumbool_positive(input_str, sumbool, expected):
    assert string_utils.delete_symbol(input_str, sumbool) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, sumbool, expected", [
    ('Skypro', 'i', 'Skypro'),
    ('', 'A', ''),
    ('abc', '', 'abc'),
])
def test_delete_sumbool_negative(input_str, sumbool, expected):
    assert string_utils.delete_symbol(input_str, sumbool) == expected






















