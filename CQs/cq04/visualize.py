__author__: str = 730669314
"""imports funcions and runs them with different arguments"""

from CQs.cq04.concatenation import concat  # importing the function :)

x: str = "123"
y: str = "abc"

print(concat(x, y))

from CQs.cq04.coordinates import get_coords  # importing the other fn

get_coords(x, y)
