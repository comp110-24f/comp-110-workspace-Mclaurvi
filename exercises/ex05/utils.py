__author__: str = "730669314"


def only_evens(lst: list[int]) -> list[int]:
    only_evens_list: list[int] = []
    for nums in lst:
        if nums % 2 == 0:
            only_evens_list.append(nums)
    return only_evens_list


def sub(lst: list[int], start_idx: int, end_idx: int) -> list[int]:
    sub_list: list[int] = []
    idx: int = 0
    while idx <= end_idx and idx < len(lst):
        if idx >= start_idx:
            sub_list.append(lst[idx])
        idx += 1
    return sub_list


def add_at_index(lst: list[int], element: int, switch_idx: int) -> None:
    lst.append(" ")
    current_idx: int = len(lst) - 1
    while current_idx >= switch_idx:
        lst[current_idx] = lst[current_idx - 1]
        current_idx = current_idx - 1
    if switch_idx >= len(lst) or switch_idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    else:
        lst[switch_idx] = element
