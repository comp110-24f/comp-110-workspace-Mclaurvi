__author__: str = 730669314
"""defines get_coords for importing"""


def get_coords(xs: str, ys: str) -> None:
    """takes 2 strings and prints one letter from each one until all of the different combinations have been reached"""
    xidx: int = 0
    yidx: int = 0

    while xidx < len(
        xs
    ):  # changes the index of xs so it can be printed with all the indexes of ys in the next while loop
        yidx = 0
        while yidx < len(ys):  # prints each index of ys with only one index of xs
            print("(" + xs[xidx] + "," + ys[yidx] + ")")
            yidx += 1
        xidx += 1
