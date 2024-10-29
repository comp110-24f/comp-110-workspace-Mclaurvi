"""examples of dictionaries using ice cream shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len(ice_cream) finds number of entries/keys
print(len(ice_cream))

# add key-values to dictionary
ice_cream["mint"] = 3

# access entries via key
print(ice_cream["chocolate"])

print(ice_cream)

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream
print(has_pbj)

# remove key-value from dictionary
ice_cream.pop("strawberry")

# for in loops better than while loops for dictionaries
# order is way they were entered (unless they were popped, then they wont appear)
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
