"""learning how to work with lists"""

# both ways to create an empty list
my_numbers: list[float] = []  # literal version
my_numbers: list[float] = list()  # constructor version

print(my_numbers)  # only prints [] if list is empty

my_numbers.append(6.9)  # adding a value to the list
my_numbers.append(2.3)

print(my_numbers)

# my_name: list[str] = "" #literal
# my_name: list[str] = str() #constructor

game_points: list[int | float] = [
    102,
    86,
    94,
    94,
]  # can put ints or floats in the list now
print(game_points)

last_game: int = game_points[2]

game_points[1] = 72  # changes index 1 in the list
print(game_points[1])
print(len(game_points))


game_points.pop(1)  # removes an item from the list
print(game_points)


# practice time :)
words: list[str] = ["hi", "two"]


def display(fun_things: list) -> None:
    idx: int = 0
    while idx < len(fun_things):
        print(fun_things[idx])
        idx += 1


display(words)


print(["Kris", "Kaki", "Alyssa"][1])
