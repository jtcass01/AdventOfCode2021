"""solution.py: Solution to Day 4 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from os.path import isfile, join, dirname
from typing import List, Union, Tuple
from enum import unique, Enum

# 3rd Party modules
from numpy import array, zeros, alltrue, apply_along_axis, fliplr, any, where

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

class BingoBoard(object):
    def __init__(self, puzzle_values: array) -> None:
        self.puzzle_values: array = puzzle_values
        self.puzzle_states: array = zeros(puzzle_values.shape, dtype=bool)

    def __str__(self) -> str:
        return str({"values": self.puzzle_values, 
                    "states": self.puzzle_states})
    
    def check_draw(self, draw: int) -> bool:
        draw_index: array = where(self.puzzle_values == draw)

        if len(draw_index[0]) > 0:
            row: int = draw_index[0]
            column: int = draw_index[1]

            self.puzzle_states[row, column] = True

    def is_winner(self) -> bool:
        def line_check(array_line: array) -> bool:
            return alltrue(array_line)

        checks: array = array([
            # row check
            any(apply_along_axis(line_check, axis=1, arr=self.puzzle_states)),
            # column check
            any(apply_along_axis(line_check, axis=0, arr=self.puzzle_states))])
            # diagnal check
            #line_check(array_line=self.puzzle_states.diagonal()),
            #line_check(array_line=fliplr(self.puzzle_states).diagonal())])

        return any(checks)

    def score(self, winning_draw: int) -> int:
        return self.puzzle_values[~self.puzzle_states].sum() * winning_draw


class BingoSubsystem(object):
    def __init__(self, draw_order: array, bingo_boards: List[BingoBoard]) -> None:
        self.draw_order: array = draw_order
        self.bingo_boards: List[BingoBoard] = bingo_boards

    def run(self, part: PART) -> Tuple[BingoBoard, int]:
        if part == PART.ONE:
            for draw in self.draw_order:
                for bingo_board in self.bingo_boards:
                    bingo_board.check_draw(draw=draw)
                    if bingo_board.is_winner():
                        return bingo_board, draw

            return None, None
        elif part == PART.TWO:
            for draw in self.draw_order:

                winning_boards: List[BingoBoard] = []
                for bingo_board in self.bingo_boards:
                    bingo_board.check_draw(draw=draw)

                    if bingo_board.is_winner():
                        winning_boards.append(bingo_board)

                for winning_board in winning_boards:
                    if len(self.bingo_boards) == 1:
                        return self.bingo_boards[0], draw
                    else:
                        self.bingo_boards.remove(winning_board)

            return None, None

    @staticmethod
    def load(puzzle_input_file_path: str, puzzle_size: int = 5) -> BingoSubsystem:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        with open(puzzle_input_file_path) as puzzle_input_file:
            # Load draw order
            draw_order: array = array([int(draw) for draw in puzzle_input_file.readline().split(",")])
            # Read empty line
            puzzle_input_file.readline()

            bingo_boards: List[BingoBoard] = []
            puzzle_line_count: int = 0
            puzzle_values: Union[List[array], array] = []
            for line in puzzle_input_file:
                if puzzle_line_count < puzzle_size:
                    puzzle_values.append(array([int(value) for value in line.split(" ") if value != ""]))
                    puzzle_line_count += 1
                else:
                    bingo_boards.append(BingoBoard(puzzle_values=array(puzzle_values)))
                    puzzle_line_count = 0
                    puzzle_values: Union[List[array], array] = []
            else:
                return BingoSubsystem(draw_order=draw_order, bingo_boards=bingo_boards)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        bingo_subsystem: BingoSubsystem = BingoSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        winning_board, winning_draw = bingo_subsystem.run(part=PART.ONE)

        self.assertEqual(winning_draw, 24)
        self.assertEqual(winning_board.score(winning_draw), 4512)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        bingo_subsystem: BingoSubsystem = BingoSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        winning_board, winning_draw = bingo_subsystem.run(part=PART.TWO)

        self.assertEqual(winning_draw, 13)
        self.assertEqual(winning_board.score(winning_draw=winning_draw), 1924)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    pass
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        bingo_subsystem: BingoSubsystem = BingoSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))
        winning_board, winning_draw = bingo_subsystem.run(part=PART.ONE)

        print(f"Part one solution calculated to be: {winning_board.score(winning_draw)}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        bingo_subsystem: BingoSubsystem = BingoSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))
        winning_board, winning_draw = bingo_subsystem.run(part=PART.TWO)

        print(f"Part two solution calculated to be: {winning_board.score(winning_draw)}.")

if __name__ == "__main__":
    main()
