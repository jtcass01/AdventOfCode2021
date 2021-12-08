"""solution.py: Solution to Day 8 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from unittest import TestCase, main
from enum import Enum, unique
from os.path import isfile, join, dirname
from typing import List, Dict, Set

@unique
class DIGIT(Enum):
    """ 0:      1:      2:      3:      4:
         aaaa    ....    aaaa    aaaa    ....
        b    c  .    c  .    c  .    c  b    c
        b    c  .    c  .    c  .    c  b    c
         ....    ....    dddd    dddd    dddd
        e    f  .    f  e    .  .    f  .    f
        e    f  .    f  e    .  .    f  .    f
         gggg    ....    gggg    gggg    ....

        5:      6:      7:      8:      9:
         aaaa    aaaa    aaaa    aaaa    aaaa
        b    .  b    .  .    c  b    c  b    c
        b    .  b    .  .    c  b    c  b    c
         dddd    dddd    ....    dddd    dddd
        .    f  e    f  .    f  e    f  .    f
        .    f  e    f  .    f  e    f  .    f
         gggg    gggg    ....    gggg    gggg"""
    ZERO: int = 0
    ONE: int = 1
    TWO: int = 2
    THREE: int = 3
    FOUR: int = 4
    FIVE: int = 5
    SIX: int = 6
    SEVEN: int = 7
    EIGHT: int = 8
    NINE: int = 9

    def get_segments(self) -> Set[SEGMENT]:
        if self == DIGIT.ZERO:
            return set([SEGMENT.A, SEGMENT.B, SEGMENT.C, SEGMENT.E, SEGMENT.F, SEGMENT.G])
        elif self == DIGIT.ONE:
            return set([SEGMENT.C, SEGMENT.F])
        elif self == DIGIT.TWO:
            return set([SEGMENT.A, SEGMENT.C, SEGMENT.D, SEGMENT.E, SEGMENT.G])
        elif self == DIGIT.THREE:
            return set([SEGMENT.A, SEGMENT.C, SEGMENT.D, SEGMENT.F, SEGMENT.G])
        elif self == DIGIT.FOUR:
            return set([SEGMENT.B, SEGMENT.C, SEGMENT.D, SEGMENT.F])
        elif self == DIGIT.FIVE:
            return set([SEGMENT.A, SEGMENT.B, SEGMENT.D, SEGMENT.F, SEGMENT.G])
        elif self == DIGIT.SIX:
            return set([SEGMENT.A, SEGMENT.B, SEGMENT.D, SEGMENT.E, SEGMENT.F, SEGMENT.G])
        elif self == DIGIT.SEVEN:
            return set([SEGMENT.A, SEGMENT.C, SEGMENT.F])
        elif self == DIGIT.EIGHT:
            return set([SEGMENT.A, SEGMENT.B, SEGMENT.C, SEGMENT.D, SEGMENT.E, SEGMENT.F, SEGMENT.G])
        elif self == DIGIT.NINE:
            return set([SEGMENT.A, SEGMENT.B, SEGMENT.C, SEGMENT.D, SEGMENT.F, SEGMENT.G])

    def get_wires(self, segment_solution: Dict[SEGMENT, WIRE]) -> Set[WIRE]:
        if self == DIGIT.ZERO:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.E], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.ONE:
            return set([segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.F]])
        elif self == DIGIT.TWO:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.E], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.THREE:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.FOUR:
            return set([segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.F]])
        elif self == DIGIT.FIVE:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.SIX:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.E], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.SEVEN:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.F]])
        elif self == DIGIT.EIGHT:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.E], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])
        elif self == DIGIT.NINE:
            return set([segment_solution[SEGMENT.A], 
                        segment_solution[SEGMENT.B], 
                        segment_solution[SEGMENT.C], 
                        segment_solution[SEGMENT.D], 
                        segment_solution[SEGMENT.F], 
                        segment_solution[SEGMENT.G]])

    @staticmethod
    def get_digit(wires: Set[WIRE], segment_solution: Dict[SEGMENT, WIRE]) -> DIGIT:
        for digit in list(DIGIT):
            if wires == digit.get_wires(segment_solution=segment_solution):
                return digit

        return None


@unique
class SEGMENT(Enum):
    A: str = "a" # Occurs 8/10 times
    B: str = "b" # Occurs 6/10 times
    C: str = "c" # Occurs 8/10 times
    D: str = "d" # Occurs 7/10 times
    E: str = "e" # Occurs 4/10 times
    F: str = "f" # Occurs 9/10 times
    G: str = "g" # Occurs 7/10 times

    @staticmethod
    def possibile_segments_by_count(count: int) -> Set[SEGMENT]:
        if count == 8:
            return {SEGMENT.A, SEGMENT.C}
        elif count == 6:
            return {SEGMENT.B}
        elif count == 7:
            return {SEGMENT.D, SEGMENT.G}
        elif count == 4:
            return {SEGMENT.E}
        elif count == 9:
            return {SEGMENT.F}


@unique
class WIRE(Enum):
    A: str = "a"
    B: str = "b"
    C: str = "c"
    D: str = "d"
    E: str = "e"
    F: str = "f"
    G: str = "g"


class SevenSegmentDisplay(object):
    def __init__(self, signal_pattern: str, output_pattern: str) -> None:
        self.signal_pattern: str = signal_pattern,
        self.output_pattern: str = output_pattern
        self.decoded_output: List[DIGIT] = SevenSegmentDisplay.decode_seven_segment_display(signal_pattern=signal_pattern,
                                                                                            output_pattern=output_pattern)

    def output(self) -> int:
        return int("".join([str(output.value) for output in self.decoded_output]))

    def __str__(self) -> str:
        return str({"signal_pattern": self.signal_pattern,
                    "output_pattern": self.output_pattern,
                    "decoded_output": self.decoded_output})

    @staticmethod
    def decode_seven_segment_display(signal_pattern: str, output_pattern: str) -> List[DIGIT]:
        segment_solution: Dict[SEGMENT, WIRE] = {}
        wire_counts: Dict[WIRE, int] = {}
        
        possible_wires: Set[WIRE] = set(list(WIRE))
        possibilities: Dict[SEGMENT, Set[WIRE]] = {SEGMENT.A: possible_wires,
                                                   SEGMENT.B: possible_wires,
                                                   SEGMENT.C: possible_wires,
                                                   SEGMENT.D: possible_wires,
                                                   SEGMENT.E: possible_wires,
                                                   SEGMENT.F: possible_wires,
                                                   SEGMENT.G: possible_wires}

        possible_segments: Set[SEGMENT] = set(list(SEGMENT))
        possibilities_by_wire: Dict[WIRE, Set[SEGMENT]] = {WIRE.A: possible_segments,
                                                           WIRE.B: possible_segments,
                                                           WIRE.C: possible_segments,
                                                           WIRE.D: possible_segments,
                                                           WIRE.E: possible_segments,
                                                           WIRE.F: possible_segments,
                                                           WIRE.G: possible_segments}

        signals: List[Set[WIRE]] = [set([WIRE(signal_wire) for signal_wire in signal]) for signal in signal_pattern.split(" ") if signal != ""]

        for wire in possible_wires:
            wire_counts[wire] = 0

        # Start by counting wires.
        for signal in signals:
            for wire in possible_wires:
                if wire in signal:
                    wire_counts[wire] += 1
                
        # narrow down segment possibilities using wire counts.
        for wire, wire_count in wire_counts.items():
            possibile_segments_by_count = SEGMENT.possibile_segments_by_count(count=wire_count)
            possibilities_by_wire[wire] = possibilities_by_wire[wire].intersection(possibile_segments_by_count)

            if len(possibilities_by_wire[wire]) == 1:
                segment_solution[list(possibilities_by_wire[wire])[0]] = wire

        # Update wire segment possibilities using wire possibilities
        for segment in possibilities.keys():
            possibilities[segment] = possibilities[segment].intersection(set([wire for wire, possible_segments in possibilities_by_wire.items() if segment in possible_segments]))

        # Start with 1
        one_signal: Set[WIRE] = [signal for signal in signals if len(signal) == 2][0]
        for one_segment in DIGIT.ONE.get_segments():
            possibilities[one_segment] = possibilities[one_segment].intersection(one_signal)

        # Update possibilites by removing solved wire segments
        for solved_segment, wire in segment_solution.items():
            for segment in possibilities.keys():
                if segment != solved_segment:
                    possibilities[segment] = possibilities[segment].difference({wire})

        # Update possibilities 
        for segment, wire in segment_solution.items():
            possibilities[segment] = {wire}

        # Update solution with final possilities
        for segment, wire_possibilities in possibilities.items():
            if len(wire_possibilities) == 1:
                segment_solution[segment] = list(wire_possibilities)[0]

        # use 7 and 1 to determine segment A
        seven_signal: Set[WIRE] = [signal for signal in signals if len(signal) == 3][0]
        segment_solution[SEGMENT.A] = list(seven_signal.difference(possibilities[SEGMENT.C].union(possibilities[SEGMENT.F])))[0]
        possibilities[SEGMENT.A] = {segment_solution[SEGMENT.A]}

        # Use 4 to differentiate between Segments G and D
        four_signal: Set[WIRE] = [signal for signal in signals if len(signal) == 4][0]
        segment_solution[SEGMENT.G] = list(possibilities[SEGMENT.G].difference(four_signal))[0]
        possibilities[SEGMENT.G] = {segment_solution[SEGMENT.G]}
        segment_solution[SEGMENT.D] = list(possibilities[SEGMENT.D].difference({segment_solution[SEGMENT.G]}))[0]
        possibilities[SEGMENT.D] = {segment_solution[SEGMENT.D]}

        assert len(segment_solution) == 7

        output_signals: List[Set[WIRE]] = [set([WIRE(signal_wire) for signal_wire in signal]) for signal in output_pattern.split(" ") if signal != ""]
        output_digits: List[DIGIT] = []

        for output_signal in output_signals:
            output_digits.append(DIGIT.get_digit(wires=output_signal, segment_solution=segment_solution))

        assert None not in output_digits, print(signal_pattern)

        return output_digits


class Puzzle(object):
    def __init__(self, seven_segment_displays: List[SevenSegmentDisplay]) -> None:
        self.seven_segment_displays: List[SevenSegmentDisplay] = seven_segment_displays

    def __str__(self) -> str:
        return "\n".join([str(seven_segment_display) for seven_segment_display in self.seven_segment_displays])

    def sum_displays(self) -> int:
        return sum([seven_segment_display.output() for seven_segment_display in self.seven_segment_displays])

    def count_digits(self, digits: Set[DIGIT]) -> int:
        digit_count: int = 0

        for seven_segment_display in self.seven_segment_displays:
            for digit in digits:
                matching_digit_count: int = seven_segment_display.decoded_output.count(digit)
                digit_count += matching_digit_count

        return digit_count

    @staticmethod
    def load(puzzle_input_file_path: str) -> Puzzle:
        assert isfile(puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        seven_segment_displays: List[SevenSegmentDisplay] = []

        with open(puzzle_input_file_path) as puzzle_input_file:
            for line in puzzle_input_file.readlines():
                signal_pattern, output_pattern = line[:-1].split("|")
                seven_segment_displays.append(SevenSegmentDisplay(signal_pattern=signal_pattern,
                                                                  output_pattern=output_pattern))

        return Puzzle(seven_segment_displays=seven_segment_displays)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        #print(test_puzzle)
        print(test_puzzle.count_digits([DIGIT.ONE, DIGIT.FOUR, DIGIT.SEVEN, DIGIT.EIGHT]))

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(test_puzzle.sum_displays(), 61229)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {test_puzzle.count_digits({DIGIT.ONE, DIGIT.FOUR, DIGIT.SEVEN, DIGIT.EIGHT})}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        test_puzzle: Puzzle = Puzzle.load(puzzle_input_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {test_puzzle.sum_displays()}.")

if __name__ == "__main__":
    main()
