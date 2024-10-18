"""defines unit test to test list_fns"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """should return first item in a list"""
    colors: list[str] = [
        "crimson",
        "blue",
        "lavender",
        "green",
    ]  # needto define individually in each fn so list doesn't change between them
    assert (get_first(colors)) == "crimson"


def test_remove_first() -> None:
    """should return None"""
    # desired function return
    colors: list[str] = ["crimson", "blue", "lavender", "green"]
    assert remove_first(colors) == None


def test_remove_first_behavior() -> None:
    """should remove first item in list"""
    # desired behavior
    colors: list[str] = ["crimson", "blue", "lavender", "green"]
    remove_first(colors)
    assert colors == ["blue", "lavender", "green"]


# python -m pytest lessons/unit_tests/list_fns_test.py (how to test in terminal)


def test_get_first_edge_case() -> None:
    """get_first called with empty list should return empty str"""
    assert get_first([]) == ""
