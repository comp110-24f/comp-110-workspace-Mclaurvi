"""Practice with conditionals"""


def less_than_10(num: int) -> bool:
    """tells you if the num is less than 10"""
    if num < 10:
        print("Small number :(")
    else:
        print("Big number :)")
    print("Have a nice day!")


# less_than_10(num=3)


def should_i_eat(hungry: bool) -> None:
    """Tells you if you should eat based on hunger"""
    if hungry:  # contional/ boolean expression
        print("Go eat bitch")  # if-then
    else:
        print("You're good then, dont eat")  # if-else
    print("computer out!")  # do this either way


# should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "Match!"  # if true
    else:
        return "No match!"  # if false

    # print(
    check_first_letter(
        word=input("What is your word?"), letter=input("What is your letter?")
    )


# print(check_first_letter(word="happy", letter="s"))


def how_big(num: int) -> str:
    if num > 50:
        if num > 100:
            return "very big number!!"
        else:
            return "big number!"
    else:
        if num < 5:
            return "very small number!"
        else:
            return "small number!"


print(how_big(num=int(input("What is your number?"))))
