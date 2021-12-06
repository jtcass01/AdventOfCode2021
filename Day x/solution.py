"""solution.py: Solution to Day x Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from enum import unique, Enum
from os.path import isfile, join, dirname

# 3rd Party modules

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

class Puzzle(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def load(puzzle_input_file_path: str) -> Puzzle:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        with open(puzzle_input_file_path) as puzzle_input_file:
            pass

        return Puzzle()


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        print(f"Part one solution calculated to be: {0.}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        print(f"Part two solution calculated to be: {0.}.")

if __name__ == "__main__":
    main()
