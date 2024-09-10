"""Input a number and it tells you what letter of the alphabet it corresponds to"""


def alphabet(number: int) -> str:
    return (
        "The letter of the alphabet corresponding to that number is "
        + "-abcdefghijklmnopqrstuvwxyz"[number]
        + " :)"
    )


def main() -> None:
    """actually asks for the letter and runs alphabet"""
    return print(alphabet(number=int(input("Choose a number between 1 and 26"))))


if __name__ == "__main__":
    main()
