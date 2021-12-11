"""solution.py: Solution to Day 11 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from os.path import isfile, join, dirname
from typing import Union, List, Tuple

# 3rd Party modules
from numpy import array, where, zeros, alltrue

class OctopusConsortium(object):
    def __init__(self, octopuses: array) -> None:
        self.octopuses: array = octopuses

    def find_first_syncronization(self) -> int:
        flash_count: int = self.pass_time(1)
        epoch_count: int = 1

        while flash_count < len(self.octopuses)**2:
            flash_count: int = self.pass_time(1)
            epoch_count += 1

        return epoch_count

    def pass_time(self, epochs: int) -> int:
        flash_count: int = 0

        for epoch in range(epochs):
            flashed: array = zeros(self.octopuses.shape, dtype=bool)
            self.octopuses += 1

            while not self.flash_finished(flashed=flashed):
                
                flash_indices: Tuple[array, array] = where(self.octopuses > 9)
                
                for flash_row, flash_column in zip(flash_indices[0], flash_indices[1]):
                    if not flashed[flash_row, flash_column]:
                        neighborhood_row_start: int = flash_row - 1
                        if neighborhood_row_start < 0:
                            neighborhood_row_start = 0

                        neighborhood_row_stop: int = flash_row + 2
                        if neighborhood_row_stop >= self.octopuses.shape[0]:
                            neighborhood_row_stop = self.octopuses.shape[0]

                        neighborhood_column_start: int = flash_column - 1
                        if neighborhood_column_start < 0:
                            neighborhood_column_start = 0

                        neighborhood_column_stop: int = flash_column + 2
                        if neighborhood_column_stop >= self.octopuses.shape[1]:
                            neighborhood_column_stop = self.octopuses.shape[1]

                        self.octopuses[neighborhood_row_start:neighborhood_row_stop, neighborhood_column_start:neighborhood_column_stop] += 1

                        # Flash
                        flashed[flash_row, flash_column] = True
                        flash_count += 1
            self.octopuses[flashed] = 0

        return flash_count

    def flash_finished(self, flashed: array) -> bool:
        flash_indices: Tuple[array, array] = where(self.octopuses > 9)
        return alltrue(flashed[flash_indices])

    @staticmethod
    def load(puzzle_input_file_path: str) -> OctopusConsortium:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        octopuses: Union[List[array], array] = []

        with open(puzzle_input_file_path) as puzzle_input_file:
            for puzzle_line in puzzle_input_file.readlines():
                octopuses.append(array([int(octopus_brightness) for octopus_brightness in puzzle_line[:-1]]))

        return OctopusConsortium(octopuses=array(octopuses))


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        octopus_consortium: OctopusConsortium = OctopusConsortium.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(octopus_consortium.pass_time(100), 1656)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        octopus_consortium: OctopusConsortium = OctopusConsortium.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(octopus_consortium.find_first_syncronization(), 195)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        octopus_consortium: OctopusConsortium = OctopusConsortium.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {octopus_consortium.pass_time(100)}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        octopus_consortium: OctopusConsortium = OctopusConsortium.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {octopus_consortium.find_first_syncronization()}.")

if __name__ == "__main__":
    main()
