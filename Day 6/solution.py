"""solution.py: Solution to Day 6 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from os.path import isfile, join, dirname
from typing import List

class LaternFishSchool(object):
    def __init__(self, initial_fish_days: List[int]) -> None:
        # indices represent days until reproduction
        self.latern_fish: List = [0] * 9

        for initial_fish_day in initial_fish_days:
            self.latern_fish[initial_fish_day] += 1

    def run(self, days: int) -> int:
        for day in range(days):
            for days_left_to_reproduce, latern_fish in enumerate(self.latern_fish):
                if days_left_to_reproduce == 0:
                    momma_daddy_fish: int = latern_fish
                    self.latern_fish[0] -= latern_fish
                else:
                    self.latern_fish[days_left_to_reproduce-1] += latern_fish
                    self.latern_fish[days_left_to_reproduce] -= latern_fish
            self.latern_fish[8] += momma_daddy_fish # baby fish
            self.latern_fish[6] += momma_daddy_fish

        return sum(self.latern_fish)

    @staticmethod
    def load(puzzle_input_file_path: str) -> LaternFishSchool:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        with open(puzzle_input_file_path) as puzzle_input_file:
            initial_fish_days = [int(initial_state) for initial_state in puzzle_input_file.read().split(",")]

        return LaternFishSchool(initial_fish_days=initial_fish_days)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        latern_fish_school: LaternFishSchool = LaternFishSchool.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))

        self.assertEqual(latern_fish_school.run(days=18), 26)
        self.assertEqual(latern_fish_school.run(days=62), 5934)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        latern_fish_school: LaternFishSchool = LaternFishSchool.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(latern_fish_school.run(days=256), 26984457539)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        latern_fish_school: LaternFishSchool = LaternFishSchool.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {latern_fish_school.run(days=80)}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        latern_fish_school: LaternFishSchool = LaternFishSchool.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {latern_fish_school.run(days=256)}.")

if __name__ == "__main__":
    main()
