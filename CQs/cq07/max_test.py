__author__: str = "730669314"

from CQs.cq07.find_max import find_and_remove_max


def test_farm_return() -> None:
    a: list[int] = [2, 8, 8, 5, 7]
    assert find_and_remove_max(a) == 8


def test_farm_mutation() -> None:
    a: list[int] = [2, 8, 8, 5, 7]
    find_and_remove_max(a)
    assert a == [2, 5, 7]


def test_farm_weird_return() -> None:
    b: list[int] = []
    assert find_and_remove_max(b) == -1
