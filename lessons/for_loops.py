"""Understanding for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for names in pets:
    """calls all the pets a good boy :)"""
    print(f"Good boy, {names}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, 3):
    """prints out the names and indexes of the names together"""
    print(f"{idx}: {names[idx]}")
