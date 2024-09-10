# function definition example
def sum(num1: int, num2: int) -> int:
    """adds the inputed numbers"""
    return num1 + num2


from random import randint

# function call example
print(sum(num1=randint(1, 10), num2=randint(1, 10)))  # <- arguments
