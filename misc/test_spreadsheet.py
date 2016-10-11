import pytest
from spreadsheet import SpreadSheet, Position

def test_get_set():
    sheet = SpreadSheet()
    pos = Position(3, 5)
    sheet.set(pos, 7)
    assert sheet.get(pos) == 7

def test_simple_sum():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    sheet.set(Position(1, 2), 1)
    sheet.set(Position(2, 1), 2)
    assert sheet.get(Position(2, 2)) == 3

def test_sum_fields_can_not_be_set():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    with pytest.raises(ValueError) as exp:
        sheet.set(Position(2,2), 5)
    assert 'Sum fields can not be set.' == str(exp.value)

def test_find_invalid_sum():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    with pytest.raises(ValueError) as exp:
        sheet.add_sum(Position(2, 2), Position(3, 3), Position(1, 2))
    assert 'Circular sum is invalid' == str(exp.value)

def test_cache_invalidate():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    sheet.set(Position(1, 2), 1)
    sheet.set(Position(2, 1), 2)
    assert sheet.get(Position(2, 2)) == 3
    sheet.set(Position(2, 1), 3)
    assert sheet.get(Position(2, 2)) == 4

def test_sum_field_not_set():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    sheet.set(Position(1, 2), 1)
    with pytest.raises(ValueError) as exp:
        sheet.get(Position(2, 2))
    assert 'One of the subfields not set' == str(exp.value)

def test_cascading_sum():
    sheet = SpreadSheet()
    sheet.add_sum(Position(1, 2), Position(2, 1), Position(2, 2))
    sheet.add_sum(Position(2, 2), Position(3, 3), Position(4, 4))
    sheet.set(Position(1, 2), 1)
    sheet.set(Position(2, 1), 2)
    sheet.set(Position(3, 3), 3)
    assert sheet.get(Position(4, 4)) == 6
