"""solution.py: Solution to Day 1 Advent of Code 2021"""

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

from typing import List
from numpy import array, diff, count_nonzero, convolve, ones
from os.path import dirname, join, isfile
from unittest import TestCase, main

def read_input_file(input_file_path: str) -> array:
    """[summary]

    Args:
        input_file_path (str): [description]

    Returns:
        List[int]: [description]"""
    assert isfile(input_file_path), f"File not found: {input_file_path}"

    with open(input_file_path) as input_file:
        file_lines: List[str] = input_file.readlines()
        return array([int(file_line) for file_line in file_lines])

def count_depth_measurement_increases(input_file_path: str) -> int:
    """[summary]

    Args:
        input_file_path (str): [description]

    Returns:
        int: [description]"""
    file_data: array = read_input_file(input_file_path=input_file_path)
    diff_file_data: array = diff(file_data)
    return count_nonzero(diff_file_data > 0)

def count_sliding_window_depth_measurement_increases(input_file_path: str, sliding_window_size: int = 3) -> int:
    """[summary]

    Args:
        input_file_path (str): [description]
        sliding_window_size (int, optional): [description]. Defaults to 3.

    Returns:
        int: [description]"""
    file_data: array = read_input_file(input_file_path=input_file_path)
    sliding_sum: array = convolve(file_data, ones(sliding_window_size, dtype=int), mode='valid')
    diff_file_data: array = diff(sliding_sum)
    return count_nonzero(diff_file_data > 0)

class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        example_depth_measurement_increase_count: int = count_depth_measurement_increases(input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(7, example_depth_measurement_increase_count)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        example_depth_measurement_increase_count: int = count_sliding_window_depth_measurement_increases(input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(5, example_depth_measurement_increase_count)

        print(f"Unittest {Examples.test_part_two_example} was successful.")


class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        depth_measurement_increase_count: int = count_depth_measurement_increases(input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {depth_measurement_increase_count}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        depth_measurement_increase_count: int = count_sliding_window_depth_measurement_increases(input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {depth_measurement_increase_count}.")


if __name__ == "__main__":
    main()
