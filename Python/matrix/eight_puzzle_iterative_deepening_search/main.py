import resource
import sys

from iddfs import IDDFS
from board import Board


def main():
    t = [8, 3, 1, 5, 4, 6, 0, 7, 2]
    c = [3, 2, 1, 4, 5, 6, 8, 7, 0]

    p = Board(c)
    p.set_target(t)

    steps = 0

    s = IDDFS(p, steps)
    s.solve()

    steps = s.number_of_steps()
    print("Number of moves")
    print(steps)

    print("Exiting program")


if __name__ == "__main__":
    main()
