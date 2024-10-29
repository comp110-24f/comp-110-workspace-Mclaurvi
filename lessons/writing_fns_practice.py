def odd_and_even(lst: list[int]) -> list[int]:
    new_list: list[int] = []
    for idx in range(0, len(lst)):
        if lst[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(lst[idx])
    return new_list


print(odd_and_even([2, 3, 4, 5]))
print(odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8]))


# def short_words(list_1: list[str]) -> list[str]:
# list_2: list[str] = []
# for word in list_1:


def str_size(list_1: list[str]) -> list[int]:
    list_2: list[int] = []
    for str in list_1:
        list_2.append(len(str))
    return list_2


print(str_size(["hi", "bee", "love"]))


def add_fun(list_1: list[str]) -> None:
    for idx in range(0, len(list_1)):
        list_1[idx] += "!"


fun_things: list[str] = ["games", "art"]
add_fun(fun_things)
print(fun_things)
