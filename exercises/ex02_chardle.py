"""Prompts user for 5 letter word + letter and checks if the word is correct/if the letter is in the word"""

__author__: str = "730669314"


def input_word() -> str:
    word_guess: str = input("Enter a 5-character word: ")
    if len(word_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_guess  # needs to be returned, not printed


def input_letter() -> str:
    letter_guess: str = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_guess


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    letter_count: int = 0
    if word[0] == letter:
        # can't use while loop bc we werent supposed to know it yet so the autograder will hate me
        print(letter + " found at index 0")
        letter_count += 1
    if word[1] == letter:
        # dont need to index weirdly bc there arent supposed to be ' around the word and letter anymore
        print(letter + " found at index 1")
        letter_count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        letter_count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        letter_count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        letter_count += 1
    if letter_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif letter_count == 1:
        print(str(letter_count) + " instance of " + letter + " found in " + word)
    else:
        print(str(letter_count) + " instances of " + letter + " found in " + word)
        # letter_count needs to be string


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# Why are we putting a main function in if we only have one line of function calls? wouldn't it be more consise to just do the line of function calls by itself?

if __name__ == "__main__":
    main()
