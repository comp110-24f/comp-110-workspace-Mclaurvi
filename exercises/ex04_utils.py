"""Doing things with for loops and while loops"""

__author__: str = "730669314"


def all(list: list[int], num_check: int) -> bool:
    idx: int = 0
    same_num: bool = False
    while idx < len(list):
        if list[idx] == num_check:
            same_num = True
        else:
            same_num = False
        if same_num == False:
            # if any number in the list isnt the same as num_check, it will end the fn/ return false
            return False
        idx += 1
    return same_num


# print(all([], 1))


def max(list: list[int]) -> int:
    biggest_num: int = (
        -999999999999999
    )  # if you use negative nums in the list starting at 0 won't work
    idx: int = 0
    while idx < len(
        list
    ):  # there's no point in using a for..in loop here bc we are working with index, hopefully we don't have to
        if list[idx] > biggest_num:
            biggest_num = list[idx]
        idx += 1
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    return biggest_num


# print(max([-5, -2, -3, -1]))


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Tells you if both lists are exactly the same or not"""
    num_same: bool = False
    if len(list_1) != len(list_2):
        # if the lists are different lengths they cant possibly be the same
        return False
    for idx in range(0, len(list_1)):  # need to use range for it to work properly
        # ok fine we'll use for loops for practice
        if list_1[idx] == list_2[idx]:
            num_same = True
        else:
            num_same = False
        if num_same == False:
            return False
        # they do look nicer than while loops at least
    return True


# print(is_equal([0, 0, 1], [1, 0, 0]))


def extend(list_1: list[int], list_2: list[int]) -> None:
    """adds the numbers in the second list to the end of the first list"""
    for idx in range(
        0, len(list_2)
    ):  # wouldn't work until i put it as a range function, would say the index is out of range otherwise?
        list_1.append(list_2[idx])
