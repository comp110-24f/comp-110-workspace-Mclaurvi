"""turns your message into a coded message via a substitution cypher"""

# how do I get the code all in one line?


def code(message: str, sub_num: int) -> None:
    index: int = 0

    while index < len(message):  # will continue until end of message
        print(
            chr(ord(message[index]) + sub_num)
        )  # does the substitution by a user-inputed number
        index += 1  # prevents infinite loop

    return None


code(
    message=input("What is the message you want to code?"),
    sub_num=int(input("How many substitutions do you want to make?")),
)
