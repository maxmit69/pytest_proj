from utils import arrs
from utils import dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], None, None) == []
    assert arrs.my_slice([1, 2, 3], None, None) == [1, 2, 3]


def test_dicts():
    assert dicts.get_val({"a": 1, "b": 2, "c": 3}, "a", "c") == 1
    assert dicts.get_val({"a": 1, "b": 2, "c": 3}, "c", "c") == 3
    assert dicts.get_val({}, "a", "c") == "c"
    assert dicts.get_val({"a": 1, "b": 2, "c": 3}, None, "c") == "c"
