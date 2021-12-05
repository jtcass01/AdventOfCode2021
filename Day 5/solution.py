"""solution.py: Solution to Day 5 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from enum import unique, Enum
from os.path import isfile, join, dirname
from typing import List, Tuple, Dict
from parse import parse

# 3rd Party modules
from numpy import array

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

class Line(object):
    FORMAT: str = "{},{} -> {},{}"
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.points: List[Tuple[int, int]] = Line.get_points(x1=x1, y1=y1, 
                                                             x2=x2, y2=y2)

    def __str__(self) -> str:
        return f"({self.x1},{self.y1}) -> ({self.x2},{self.y2}) : {self.points}"

    @staticmethod
    def get_points(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
        if y1 == y2:
            if x1 > x2:
                return [(x, int(y1)) for x in range(x1, x2-1, -1)]
            else:
                return [(x, int(y1)) for x in range(x1, x2+1, 1)]
        elif x1 == x2:
            if y1 > y2:
                return [(x1, int(y)) for y in range(y1, y2-1, -1)]
            else:
                return [(x1, int(y)) for y in range(y1, y2+1, 1)]
        else:
            slope: float = Line.slope(x1=x1, y1=y1, x2=x2, y2=y2)
            y_intercept: float = Line.y_intercept(x1=x1, y1=y1, x2=x2, y2=y2)

            if x1 > x2:
                return [(x, int(Line.evaluate(x=x, slope=slope, y_intercept=y_intercept))) for x in range(x1, x2-1, -1)]
            else:
                return [(x, int(Line.evaluate(x=x, slope=slope, y_intercept=y_intercept))) for x in range(x1, x2+1, 1)]

    @staticmethod
    def evaluate(x: int, slope: int, y_intercept: int) -> int:
        return slope*x+y_intercept

    @staticmethod
    def slope(x1: int, y1: int, x2: int, y2: int) -> float:
        return (y1 - y2) / (x1 - x2)

    @staticmethod
    def y_intercept(x1: int, y1: int, x2: int, y2: int) -> float:
        return (x1*y2 - x2*y1) / (x1-x2)

class Puzzle(object):
    def __init__(self, lines: List[Line]) -> None:
        self.point_counts: Dict[Tuple[int, int], int] = Puzzle.count_points(lines=lines)

    def evaluate(self) -> int:
        return Puzzle.overlap_count(point_counts=self.point_counts)

    @staticmethod
    def overlap_count(point_counts: Dict[Tuple[int, int], int]) -> int:
        return len([(point, point_count) for (point, point_count) in point_counts.items() if point_count > 1])

    @staticmethod
    def count_points(lines: List[Line]) -> Dict[Tuple[int, int], int]:
        point_counts: Dict[Tuple[int, int], int] = {}

        for line in lines:
            for point in line.points:
                if point in point_counts:
                    point_counts[point] += 1
                else:
                    point_counts[point] = 1

        return point_counts


    @staticmethod
    def load(puzzle_input_file_path: str, part: PART) -> Puzzle:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        lines: List[array] = []
        with open(puzzle_input_file_path) as puzzle_input_file:
            for text_line in puzzle_input_file.readlines():
                x1, y1, x2, y2 = parse(Line.FORMAT, text_line)
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                line: Line = Line(int(x1), int(y1), int(x2), int(y2))

                if x1 == x2 or y1 == y2:
                    lines.append(line)
                else:
                    if part == PART.TWO:
                        slope: int = Line.slope(int(x1), int(y1), int(x2), int(y2))

                        if slope == 1 or slope == -1:
                            lines.append(line)

        return Puzzle(lines=lines)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"),
                                          part=PART.ONE)
        self.assertEqual(test_puzzle.evaluate(), 5)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"),
                                          part=PART.TWO)
        self.assertEqual(test_puzzle.evaluate(), 12)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"),
                                          part=PART.ONE)

        print(f"Part one solution calculated to be: {test_puzzle.evaluate()}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"),
                                          part=PART.TWO)

        print(f"Part two solution calculated to be: {test_puzzle.evaluate()}.")

if __name__ == "__main__":
    main()
