"""solution.py: Solution to Day x Advent of Code 2021"""

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from enum import unique, Enum

# 3rd Party modules

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    pass
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        print(f"Part one solution calculated to be: {0.}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        print(f"Part two solution calculated to be: {0.}.")

if __name__ == "__main__":
    main()
