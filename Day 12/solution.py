"""solution.py: Solution to Day 12 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from copy import copy
from os.path import isfile, join, dirname
from typing import Dict, List
from parse import parse, Result


class Cave(object):
    FORMAT_CONNECTION: str = "{}-{}"

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.connected_caves: Dict[str, Cave] = {}

    def __str__(self) -> str:
        return f"{self.name} | connected to: {self.connected_caves}"

    def add_connection(self, cave: Cave) -> None:
        if cave.name not in self.connected_caves:
            self.connected_caves[cave.name] = cave

    def list_connections(self) -> List[Cave]:
        return [cave for cave_name, cave in self.connected_caves.items()]

class CaveSystem(object):
    def __init__(self, caves: Dict[str, Cave]) -> None:
        self.caves: Dict[str, Cave] = caves

    def count_paths_that_visit_small_caves_at_most_n_times(self, n: int) -> int:
        """Breadth First Search."""
        start_cave: Cave = self.caves['start']
        valid_paths: List[List[Cave]] = []

        def search_for_connected_cave_paths(cave: Cave, current_path: List[Cave]) -> None:
            current_path.append(cave)
            for adjacent_cave in cave.list_connections():
                if cave.name == "end":
                    valid_paths.append(current_path)
                    return
                valid_path: bool = False

                # Determine if large cave
                if adjacent_cave.name.isupper():
                    valid_path = True
                else:
                    max_small_cave_frequency: int = max([cave_frequency for cave, cave_frequency in CaveSystem.count_small_cave_frequencies(path=current_path).items()])
                    if max_small_cave_frequency < n and adjacent_cave.name != "start":
                        valid_path = True
                    else:
                        if adjacent_cave.name not in [cave.name for cave in current_path]:
                            valid_path = True

                if valid_path:
                    search_for_connected_cave_paths(cave=adjacent_cave, current_path=copy(current_path))

        search_for_connected_cave_paths(cave=start_cave, current_path=[])
        return len(valid_paths)

    @staticmethod
    def count_small_cave_frequencies(path: List[Cave]) -> Dict[Cave, int]:
        small_cave_frequencies: Dict[Cave, int] = {}

        for cave in path:
            if cave.name.islower():
                if cave in small_cave_frequencies:
                    small_cave_frequencies[cave] += 1
                else:
                    small_cave_frequencies[cave] = 1
        
        return small_cave_frequencies

    @staticmethod
    def load(puzzle_input_file_path: str) -> CaveSystem:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"
        caves: Dict[str, Cave] = {}

        with open(puzzle_input_file_path) as puzzle_input_file:
            cave_connections: List[Result] = [parse(Cave.FORMAT_CONNECTION, cave_connection) for cave_connection in puzzle_input_file.readlines()]

            for cave_connection in cave_connections:
                left_cave: str = cave_connection[0]
                right_cave: str = cave_connection[1]

                if left_cave not in caves: caves[left_cave] = Cave(name=left_cave)
                if right_cave not in caves: caves[right_cave] = Cave(name=right_cave)
                caves[left_cave].add_connection(caves[right_cave])
                caves[right_cave].add_connection(caves[left_cave])

        return CaveSystem(caves=caves)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")
        examples: Dict[str, int] = {"example.txt": 10,
                                    "example_1.txt": 19,
                                    "example_2.txt": 226}

        for example_file_name, expected_result in examples.items():
            test_cave_system: CaveSystem = CaveSystem.load(puzzle_input_file_path=join(dirname(__file__), example_file_name))
            self.assertEqual(test_cave_system.count_paths_that_visit_small_caves_at_most_n_times(n=1), expected_result)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        test_cave_system: CaveSystem = CaveSystem.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(test_cave_system.count_paths_that_visit_small_caves_at_most_n_times(n=2), 36)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        cave_system: CaveSystem = CaveSystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {cave_system.count_paths_that_visit_small_caves_at_most_n_times(n=1)}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        cave_system: CaveSystem = CaveSystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {cave_system.count_paths_that_visit_small_caves_at_most_n_times(n=2)}.")

if __name__ == "__main__":
    main()


