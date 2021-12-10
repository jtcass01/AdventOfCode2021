"""solution.py: Solution to Day 10 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from enum import unique, Enum
from os.path import isfile, join, dirname
from typing import List, Union
from math import floor

@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

@unique
class BRACKETS(Enum):
    PARENTHESIS: str = "()"
    SQUARE_BRACKET: str = "[]"
    SWIRLY_BRACKET: str = "{}"
    SHARP_BRACKET: str = "<>"

@unique
class OPEN_BRACKET(Enum):
    PARENTHESIS: str = "("
    SQUARE_BRACKET: str = "["
    SWIRLY_BRACKET: str = "{"
    LESS_THAN: str = "<"

    def get_matching_closed_bracket(self) -> str:
        if self == OPEN_BRACKET.PARENTHESIS:
            return ")"
        elif self == OPEN_BRACKET.SQUARE_BRACKET:
            return "]"
        elif self == OPEN_BRACKET.SWIRLY_BRACKET:
            return "}"
        elif self == OPEN_BRACKET.LESS_THAN:
            return ">"

@unique
class CLOSING_BRACKET(Enum):
    PARENTHESIS: str = ")"
    SQUARE_BRACKET: str = "]"
    SWIRLY_BRACKET: str = "}"
    GREATER_THAN: str = ">"

    def score(self, part: PART) -> int:
        if part == PART.ONE:
            if self == CLOSING_BRACKET.PARENTHESIS:
                return 3
            elif self == CLOSING_BRACKET.SQUARE_BRACKET:
                return 57
            elif self == CLOSING_BRACKET.SWIRLY_BRACKET:
                return 1197
            elif self == CLOSING_BRACKET.GREATER_THAN:
                return 25137
        elif part == PART.TWO:
            if self == CLOSING_BRACKET.PARENTHESIS:
                return 1
            elif self == CLOSING_BRACKET.SQUARE_BRACKET:
                return 2
            elif self == CLOSING_BRACKET.SWIRLY_BRACKET:
                return 3
            elif self == CLOSING_BRACKET.GREATER_THAN:
                return 4

class NavigationSubsystem(object):
    def __init__(self, navigation_subsystem_report: List[str]) -> None:
        self.navigation_subsystem_report: List[str] = navigation_subsystem_report

    def get_corrupted_syntax_error_score(self) -> int:
        def get_first_illegal_character(remaining_report_line: str) -> Union[str, None]:
            reduced: bool = False

            for bracket in list(BRACKETS):
                if remaining_report_line.find(bracket.value) != -1:
                    remaining_report_line = remaining_report_line.replace(bracket.value, "")
                    reduced = True

            if reduced:
                return get_first_illegal_character(remaining_report_line=remaining_report_line)
            else:
                try:
                    first_closed_bracket_index: int = min([remaining_report_line.find(closing_bracket.value) for closing_bracket in list(CLOSING_BRACKET)\
                                                            if remaining_report_line.find(closing_bracket.value) != -1])
                    return remaining_report_line[first_closed_bracket_index]
                except ValueError:
                    return None

        illegal_characters: List[str] = []
        for report_line in self.navigation_subsystem_report:
            illegal_characters.append(get_first_illegal_character(remaining_report_line=report_line))

        score: int = 0
        for closing_bracket in list(CLOSING_BRACKET):
            score += illegal_characters.count(closing_bracket.value) * closing_bracket.score(part=PART.ONE)

        return score

    def get_incomplete_syntax_error_score(self) -> int:
        def get_syntax_needed_for_compeletion(remaining_report_line: str) -> Union[None, str]:
            reduced: bool = False

            for bracket in list(BRACKETS):
                if remaining_report_line.find(bracket.value) != -1:
                    remaining_report_line = remaining_report_line.replace(bracket.value, "")
                    reduced = True

            if reduced:
                return get_syntax_needed_for_compeletion(remaining_report_line=remaining_report_line)
            else:
                try:
                    min([remaining_report_line.find(closing_bracket.value) for closing_bracket in list(CLOSING_BRACKET)\
                         if remaining_report_line.find(closing_bracket.value) != -1])
                    return None
                except ValueError:
                    return "".join([OPEN_BRACKET(open_bracket).get_matching_closed_bracket() for open_bracket in remaining_report_line[::-1]])

        completion_characters: List[Union[str, None]] = []
        for report_line in self.navigation_subsystem_report:
            completion_characters.append(get_syntax_needed_for_compeletion(remaining_report_line=report_line))

        scores: List[int] = []
        for completion_character_string in completion_characters:
            score: int = 0

            if completion_character_string is not None:
                for completion_character in completion_character_string:
                    score *= 5
                    score += CLOSING_BRACKET(completion_character).score(part=PART.TWO)
                scores.append(score)

        scores.sort()

        return scores[floor(len(scores) / 2)]

    @staticmethod
    def load(puzzle_input_file_path: str) -> NavigationSubsystem:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        with open(puzzle_input_file_path) as puzzle_input_file:
            navigation_subsystem_report: List[str] = [puzzle_line[:-1] for puzzle_line in puzzle_input_file.readlines()]

        return NavigationSubsystem(navigation_subsystem_report=navigation_subsystem_report)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        navigation_subsystem: NavigationSubsystem = NavigationSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(navigation_subsystem.get_corrupted_syntax_error_score(), 26397)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        navigation_subsystem: NavigationSubsystem = NavigationSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(navigation_subsystem.get_incomplete_syntax_error_score(), 288957)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        navigation_subsystem: NavigationSubsystem = NavigationSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {navigation_subsystem.get_corrupted_syntax_error_score()}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        navigation_subsystem: NavigationSubsystem = NavigationSubsystem.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {navigation_subsystem.get_incomplete_syntax_error_score()}.")

if __name__ == "__main__":
    main()


