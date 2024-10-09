"""Summing the elements of a list using different loops"""

__author__: str = "730669314"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in vals:
        sum += vals[int(idx)]  # idx needs to be int to work
    return sum  # this returns 2.9??? why??


# print(f_sum([1.1, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum


# print(f_range_sum([1.1, 0.9, 1.0]))
