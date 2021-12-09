"""solution.py: Solution to Day x Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from os.path import isfile, join, dirname
from typing import Union, List, Tuple

# 3rd Party modules
from numpy import array, where, product
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.filters import minimum_filter


class Cave(object):
    def __init__(self, height_map: array) -> None:
        """Constructor.

        Args:
            height_map (array): Cave height as 2d array of integers"""
        self.height_map: array = height_map

    def get_minimum_risk_level(self) -> int:
        """Treats height map as an image and utilizes scipy.ndimage library to solve for risk level.

        Returns:
            int: risk_level"""
        neighborhood: array = generate_binary_structure(len(self.height_map.shape), 2)
        local_min: array = self.height_map[where(minimum_filter(self.height_map, footprint=neighborhood) == self.height_map)]
        risk_level: array = local_min + 1 
        return sum(risk_level)

    def size_three_largest_basins(self) -> int:
        def size_local_basin(minimum_x: int, minimum_y: int) -> int:
            basin_locations: List[Tuple[int, int]] = []
            basin_locations.append((minimum_x, minimum_y))

            def search_basin(x: int, y: int) -> None:
                current_value: int = self.height_map[x, y]

                # Search up
                if y - 1 >= 0:
                    up_value: int = self.height_map[x, y-1]

                    if up_value >= current_value and up_value != 9:
                        if (x, y-1) not in basin_locations:
                            basin_locations.append((x, y-1))
                            search_basin(x=x, y=y-1)
                
                if y + 1 < self.height_map.shape[1]:
                    down_value: int = self.height_map[x, y+1]

                    if down_value >= current_value and down_value != 9:
                        if (x, y+1) not in basin_locations:
                            basin_locations.append((x, y+1))
                            search_basin(x=x, y=y+1)

                if x - 1 >= 0:
                    left_value: int = self.height_map[x-1, y]

                    if left_value >= current_value and left_value != 9:
                        if (x-1, y) not in basin_locations:
                            basin_locations.append((x-1, y))
                            search_basin(x=x-1, y=y)
                
                if x + 1 < self.height_map.shape[0]:
                    right_value: int = self.height_map[x+1, y]

                    if right_value >= current_value and right_value != 9:
                        if (x+1, y) not in basin_locations:
                            basin_locations.append((x+1, y))
                            search_basin(x=x+1, y=y)

            search_basin(x=minimum_x, y=minimum_y)
            return len(basin_locations)

        neighborhood: array = generate_binary_structure(len(self.height_map.shape), 2)
        local_min_locations: array = where(minimum_filter(self.height_map, footprint=neighborhood) == self.height_map)

        basin_sizes: Union[List[int], array] = []
        for local_min_x, local_min_y in zip(local_min_locations[0], local_min_locations[1]):
            basin_sizes.append(size_local_basin(minimum_x=local_min_x, minimum_y=local_min_y))

        basin_sizes.sort()

        return product(basin_sizes[-3:])

    @staticmethod
    def load(puzzle_input_file_path: str) -> Cave:
        """Parses puzzle input file into Cave object.

        Args:
            puzzle_input_file_path (str): relative or absolute path to puzzle input file.

        Returns:
            Cave: Object-oriented representation of problem."""
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"
        height_map: Union[array, List[array]] = []

        with open(puzzle_input_file_path) as puzzle_input_file:
            for line in puzzle_input_file.readlines():
                height_line: array = array([int(value) for value in line if value !="\n"])
                height_map.append(height_line)

        return Cave(height_map=array(height_map))


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        test_cave: Cave = Cave.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(test_cave.get_minimum_risk_level(), 15)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        test_cave: Cave = Cave.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(test_cave.size_three_largest_basins(), 1134)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        test_cave: Cave = Cave.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {test_cave.get_minimum_risk_level()}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        test_cave: Cave = Cave.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {test_cave.size_three_largest_basins()}.")

if __name__ == "__main__":
    main()


