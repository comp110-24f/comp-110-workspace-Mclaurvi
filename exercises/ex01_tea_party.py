"""Determines how many tea bags and treats are needed for a party of x people and how much that would cost"""

__author__: str = "730669314"


def main_planner(guests: int) -> None:
    """Runs all the fns with user input of number of guests and prints the results"""
    print(
        "A cozy tea party for " + str(guests) + " People!"
    )  # the arguments need to be turned into strings to work (why didn't we do this in the fn defs? That would make so much more sense)
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # calling treats and tea_bags to get the numbers for the arguments


def tea_bags(people: int) -> int:
    """Determines how many teabags are needed for x amount of people"""
    return people * 2


def treats(people: int) -> int:
    """determines how many treats should be prepared based on the number of teabags"""
    return int(
        tea_bags(people=people)
        * 1.5  # check whether putting the other fn's parameter as an argument in this fn counts as using a keyword argument
    )


def cost(tea_count: int, treat_count: int) -> float:
    """finds the cost of x number of treats and x number of tea bags"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # using tea_count and treat_count intead of calling tea_bags and treats so I can put in seperate values for them? (or just to avoid putting the name of a fn as a parameter, that might mess stuff up)


if (
    __name__ == "__main__"
):  # remember to find out why we use this conditional specifically/how it works
    main_planner(guests=int(input("How many guests are attending your tea party?")))
