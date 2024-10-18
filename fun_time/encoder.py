"""turns your message into a coded message via a substitution cypher"""

uncoded_letters: list[str] = []
coded_letters: list[str] = []


def code(input_message: str, sub_num: int) -> str:
    """takes message/does substitution cypher"""
    idx: int = 0
    final_message: str = ""
    while idx < len(input_message):
        """ "puts the letters of the input individually into the uncoded_letters list"""
        if input_message[idx] == " ":
            uncoded_letters.append(" ")
        else:
            uncoded_letters.append(input_message[idx])
        idx += 1
    for letters in uncoded_letters:
        """changes the letters and puts the changed letters into a new list"""
        if letters == " ":
            coded_letters.append(" ")
        else:
            coded_letters.append(chr(ord(letters) + sub_num))
    for letters in coded_letters:
        final_message += letters
    return f"This is your coded message: {final_message}"


print(
    code(
        input_message=input("What is the message you want to code?"),
        sub_num=int(input("How many substitutions do you want to make?")),
    )
)
