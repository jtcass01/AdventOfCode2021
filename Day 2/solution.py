"""solution.py: Solution to Day 2 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

from typing import List
from enum import Enum, unique
from os.path import dirname, join, isfile
from unittest import TestCase, main
from parse import parse

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

@unique
class DIRECTION(Enum):
    FORWARD: str = "forward"
    DOWN: str = "down"
    UP: str = "up"

class Action(object):
    FORMAT_STRING: str = "{} {}"

    def __init__(self, direction: DIRECTION, units: int) -> None:
        """Constructor.

        Args:
            direction (DIRECTION): [description]
            units (int): [description]"""
        self.direction: DIRECTION = direction
        self.units: int = units

class Submarine(object):
    def __init__(self) -> None:
        """Constructor."""
        self.horizontal_position: int = 0
        self.depth: int = 0
        self.aim: int = 0

    def __str__(self) -> str:
        return str({"horizontal_position": self.horizontal_position,
                    "depth": self.depth})

    def evaluate(self) -> int:
        return self.depth * self.horizontal_position

    def perform_action(self, action: Action, part: PART) -> None:
        """[summary]

        Args:
            action (Action): [description]"""
        if part == PART.ONE:
            if action.direction == DIRECTION.FORWARD:
                self.horizontal_position += action.units
            elif action.direction == DIRECTION.DOWN:
                self.depth += action.units
            elif action.direction == DIRECTION.UP:
                self.depth -= action.units
        elif part == PART.TWO:
            if action.direction == DIRECTION.FORWARD:
                self.horizontal_position += action.units
                self.depth += self.aim * action.units
            elif action.direction == DIRECTION.DOWN:
                self.aim += action.units
            elif action.direction == DIRECTION.UP:
                self.aim -= action.units

def read_input_file(input_file_path: str) -> List[Action]:
    """[summary]

    Args:
        input_file_path (str): [description]

    Returns:
        List[int]: [description]"""
    assert isfile(input_file_path), f"File not found: {input_file_path}"
    actions: List[Action] = []

    with open(input_file_path) as input_file:
        for file_line in input_file.readlines():
            direction, units = parse(Action.FORMAT_STRING, file_line)
            actions.append(Action(direction=DIRECTION(direction), units=int(units)))

    return actions

class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        example_submarine: Submarine = Submarine()
        actions: List[Action] = read_input_file(input_file_path=join(dirname(__file__), "example.txt"))

        for action in actions:
            example_submarine.perform_action(action=action, part=PART.ONE)

        self.assertEqual(example_submarine.horizontal_position, 15)
        self.assertEqual(example_submarine.depth, 10)
        self.assertEqual(example_submarine.evaluate(), 150)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        example_submarine: Submarine = Submarine()
        actions: List[Action] = read_input_file(input_file_path=join(dirname(__file__), "example.txt"))

        for action in actions:
            example_submarine.perform_action(action=action, part=PART.TWO)

        self.assertEqual(example_submarine.horizontal_position, 15)
        self.assertEqual(example_submarine.depth, 60)
        self.assertEqual(example_submarine.evaluate(), 900)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        submarine: Submarine = Submarine()
        actions: List[Action] = read_input_file(input_file_path=join(dirname(__file__), "input.txt"))

        for action in actions:
            submarine.perform_action(action=action, part=PART.ONE)

        print(f"Part one solution calculated to be: {submarine.evaluate()}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        submarine: Submarine = Submarine()
        actions: List[Action] = read_input_file(input_file_path=join(dirname(__file__), "input.txt"))

        for action in actions:
            submarine.perform_action(action=action, part=PART.TWO)

        print(f"Part two solution calculated to be: {submarine.evaluate()}.")

if __name__ == "__main__":
    main()
