def get_first(lst: list[str]) -> str:
    if len(lst) == 0:
        return ""
    return lst[0]


def remove_first(lst: list[str]) -> None:
    lst.pop(0)


def get_and_remove_first(lst: list[str]) -> str:
    first_value: str = lst[
        0
    ]  # need to save this first bc returning it would end fn early but calling idx later would give second value
    lst.pop(0)
    return first_value
