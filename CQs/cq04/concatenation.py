__author__: str = 730669314
"""defines the concatination function/runs it"""


def concat(str1: str, str2: str) -> str:
    """combines the string inputs into 1 string"""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if (
    __name__ == "__main__"
):  # makes it so this only runs when this program is run (wont do this if imported)
    print(concat(word1, word2))
