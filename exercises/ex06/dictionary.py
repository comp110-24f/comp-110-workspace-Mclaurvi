__author__: str = "730669314"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    dict_2: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in dict_2:
            raise KeyError(
                "Oops, you have multiple values for one key! That won't work here"
            )
        dict_2[dict_1[key]] = key
    return dict_2


def favorite_color(fav_colors: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    for name in fav_colors:
        if fav_colors[name] in color_count:
            color_count[fav_colors[name]] += 1
        else:
            color_count[fav_colors[name]] = 1
    highest_count: int = 0
    for color in color_count:
        if highest_count < color_count[color]:
            highest_count = color_count[color]
    for color in color_count:
        if color_count[color] == highest_count:
            return color


def count(list_1: list[str]) -> dict[str, int]:
    final_count: dict[str, int] = {}
    for num in list_1:
        if num in final_count:
            final_count[num] += 1
        else:
            final_count[num] = 1
    return final_count


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    alphabet_dict: dict[str, list[str]] = {}
    for word in words:
        if word[0].lower() in alphabet_dict:
            alphabet_dict[word[0].lower()].append(word)
        else:
            alphabet_dict[word[0].lower()] = [word]
    return alphabet_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> dict[str, list[str]]:
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict
