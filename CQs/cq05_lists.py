"""Mutating functions"""

__author__: str = "730669314"


def manual_append(int_list: list[int], add_num: int) -> None:
    """adds things to a list"""
    int_list.append(add_num)


def double(list: list[int]) -> None:
    """doubles every number in the list (and replaces them with the duplicated numbers)"""
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
