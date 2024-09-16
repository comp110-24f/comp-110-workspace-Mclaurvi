"""User inputs a number and the program tells them whether it matches the number in the code"""

__author__: str = "730669314"


def guess_a_number() -> None:
    secret: int = 7
    guess_num: str = input("Guess a number: ")
    print("Your guess was " + guess_num)
    if int(guess_num) == secret:
        print("You got it!")
    elif int(guess_num) < secret:  # both need to be ints
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # secret needs to be made into a string to work here
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
