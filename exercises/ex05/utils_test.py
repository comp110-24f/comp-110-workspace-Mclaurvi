__author__: str = "730669314"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

# only_evens tests


def test_only_evens_return() -> None:
    """supposed to only show even nums"""
    a: list[int] = [2, 3, 6]
    assert only_evens(a) == [2, 6]


def test_only_evens_mutation() -> None:
    """not supposed to mutate list"""
    b: list[int] = [2, 3, 6]
    only_evens(b)
    assert b == [2, 3, 6]


def test_only_evens_empty() -> None:
    """should return empty list"""
    c: list[int] = []
    assert only_evens(c) == []


def test_only_evens_0() -> None:
    """Should return 0 (zero can be divided by 2 so its even, fuck you)"""
    d: list[int] = [0, 3, 7]
    assert only_evens(d) == [0]


# sub tests


def test_sub_return() -> None:
    """should return sublist of nums in the index interval given"""
    e: list[int] = [2, 4, 6, 8, 10]
    assert sub(e, 1, 3) == [4, 6]


def test_sub_mutation() -> None:
    """should not mutate list"""
    f: list[int] = [2, 4, 6, 8, 10]
    sub(f, 1, 3)
    assert f == [2, 4, 6, 8, 10]


def test_sub_too_big_interval_end() -> None:
    """should just put numbers that are in the list and still in interval"""
    g: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert sub(g, 2, 8) == [5, 7, 9, 11, 13]


def test_sub_too_big_interval_front() -> None:
    """should just put numbers that are in the list and still in interval"""
    h: list[int] = [1, 5, 10, 15]
    assert sub(h, -2, 2) == [1, 5]


# add_at_index tests


def test_add_at_index_output() -> None:
    """should return None"""
    i: list[int] = [1, 3, 5, 9]
    assert add_at_index(i, 7, 3) == None


def test_add_at_index_mutation() -> None:
    """should add the input at the specified index in the list"""
    j: list[int] = [1, 3, 5, 9]
    add_at_index(j, 7, 3)
    assert j == [1, 3, 5, 7, 9]


def test_add_at_index_too_high() -> None:
    """should return index error"""
    k: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(k, 5, 7)


def test_add_at_index_too_low() -> None:
    """should return index error"""
    l: list[int] = [4, 5, 6]
    with pytest.raises(IndexError):
        add_at_index(l, 1, -2)
