__author__: str = "730669314"


def find_and_remove_max(lst: list[int]) -> int:
    biggest_num: int = -1
    for nums in lst:
        if nums > biggest_num:
            biggest_num = nums
    idx: int = 0
    while idx < len(lst):
        if lst[idx] == biggest_num:
            lst.pop(idx)
        else:
            idx += 1
    return biggest_num
