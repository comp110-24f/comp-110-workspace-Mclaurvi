"""counts the number of characters in a phrase"""

__author__: str = "730669314"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # how many times the character has appeared so far
    index: int = 0
    while index < len(phrase):
        if (
            phrase[index] == search_char
        ):  # looks at each character and sees if it is the character we are searching for
            count = count + 1
        index = (
            index + 1
        )  # keeping this outside of the if phrase so that it's not an infinite loop
    return count
