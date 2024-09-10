__author__ = 730669314


def mimic(message: str) -> str:
    """returns the typed message back to you :)"""
    return message


def main() -> None:
    """running and printing mimic"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
