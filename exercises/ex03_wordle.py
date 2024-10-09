"""works like worlde, you guess and it tells you if letter is in word/in right position"""

__author__: str = "730669314"


def input_guess(secret_length: int) -> str:
    guess: str = input(f"Enter a {secret_length} character word: ")

    while secret_length != len(guess):
        # keeps the inputs going until the guess is the correct length
        if secret_length != len(guess):
            guess = input(f"That wasn't {secret_length} chars! Try again: ")
            # lets them put in another input
    return guess


def contains_char(secret_word: str, letter_guess: str) -> bool:
    """searches the secret word for a specific letter"""
    assert len(letter_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == letter_guess:
            return True  # ends loop early if letter is found
        idx += 1
    return False


def emojified(secret_word: str, word_guess: str) -> str:
    """compares secret word and guess (must be same length!) and prints emojis based on whether the letters are in the secret word and at the same index"""
    # The arguments are switched in the 'do this to see if your code works' section, if I have to switch these for the autograder to work I swear to God I'm going to murder somebody holy fuck
    assert len(word_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emojis: str = ""
    while idx < len(word_guess):
        if word_guess[idx] == secret_word[idx]:
            # if letter is in word and in the right place
            emojis += GREEN_BOX
        else:
            if (
                contains_char(secret_word=word_guess, letter_guess=secret_word[idx])
                == True
            ):
                # if letter is in word but not the right place
                emojis += YELLOW_BOX
            else:
                # if letter is not in word
                emojis += WHITE_BOX
        idx += 1  # prevents infinite loop
    return emojis


def main(secret_word: str) -> None:
    """runs all the functions"""
    turn: int = 1
    win: bool = False
    turn_guess: str = ""
    while (turn <= 6) and (win == False):  # needs to end when you win
        print(f"=== Turn {turn}/6 ===")
        turn_guess = input_guess(
            secret_length=len(secret_word)
        )  # needs to be called here so that I can use it to see if you won or not

        print(emojified(secret_word=secret_word, word_guess=turn_guess))

        if secret_word == turn_guess:  # if they are all correct
            print(f"You won in {turn}/6 turns!")
            # might have to move this outside if the autograder doesn't like it
            win = True
        turn += 1
    if win == False:  # if you run out of turns
        print("X/6 - Sorry, try again tommorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
