"""solution.py: Solution to Day 3 Advent of Code 2021"""
from __future__ import annotations

__author__ = "Jacob Taylor Cassady"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in modules
from typing import List
from os.path import isfile, join, dirname
from unittest import TestCase, main

# 3rd Party modules
from numpy import array
from scipy.stats import mode
from scipy.stats.mstats_basic import ModeResult


class DiagnosticReport(object):
    def __init__(self, diagnostic_values: array) -> None:
        self.gamma_rate: int = DiagnosticReport.Calculation.gamma_rate(diagnostic_values=diagnostic_values)
        self.epsilon_rate: int = DiagnosticReport.Calculation.epsilon_rate(diagnostic_values=diagnostic_values)
        self.power_consuption: int = DiagnosticReport.Calculation.power_consumption(gamma_rate=self.gamma_rate,
                                                                                    epislon_rate=self.epsilon_rate)
        self.oxygen_generator_rating: int = DiagnosticReport.Calculation.oxygen_generator_rating(diagnostic_values=diagnostic_values)
        self.CO2_scrubber_rating: int = DiagnosticReport.Calculation.CO2_scrubber_rating(diagnostic_values=diagnostic_values)
        self.life_support_rating: int = DiagnosticReport.Calculation.life_support_rating(oxygen_generator_rating=self.oxygen_generator_rating,
                                                                                         CO2_scrubber_rating=self.CO2_scrubber_rating)

    def __str__(self) -> str:
        return str({"gamma_rate": self.gamma_rate,
                    "epsilon_rate": self.epsilon_rate,
                    "power_consumption": self.power_consuption,
                    "oxygen_generator_rating": self.oxygen_generator_rating,
                    "CO2_scrubber_rating": self.CO2_scrubber_rating,
                    "life_support_rating": self.life_support_rating})

    class Calculation:
        @staticmethod
        def gamma_rate(diagnostic_values: array) -> int:
            diagnostic_values_mode = mode(diagnostic_values, axis=0).mode[0]
            return int("".join([str(value) for value in diagnostic_values_mode]), 2)

        @staticmethod
        def oxygen_generator_rating(diagnostic_values: array) -> int:
            """To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, 
            and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 
            in the position being considered."""
            def trim_values(trimmed_values: array, column_index: int) -> array:
                if (trimmed_values == trimmed_values[0]).all():
                    return trimmed_values[0, :]
                else:
                    mode_analysis: ModeResult = mode(trimmed_values, axis=0)
                    trimmed_values_mode: array = mode_analysis.mode[0]
                    trimmed_values_count: array = mode_analysis.count[0]

                    if trimmed_values_count[column_index] == trimmed_values.shape[0]/2:
                        # Tie breaker
                        column_mode: int = 1
                    else:
                        column_mode: int = trimmed_values_mode[column_index]

                    return trim_values(trimmed_values=trimmed_values[trimmed_values[:, column_index] == column_mode], 
                                       column_index=column_index+1)
            solution_row: array = trim_values(trimmed_values=diagnostic_values, column_index=0)
            return int("".join([str(value) for value in solution_row]), 2)

        @staticmethod
        def CO2_scrubber_rating(diagnostic_values: array) -> int:
            """To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, 
            and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with
             a 0 in the position being considered."""
            def trim_values(trimmed_values: array, column_index: int) -> array:
                if (trimmed_values == trimmed_values[0]).all():
                    return trimmed_values[0, :]
                else:
                    mode_analysis: ModeResult = mode(trimmed_values, axis=0)
                    trimmed_values_mode: array = mode_analysis.mode[0]
                    trimmed_values_count: array = mode_analysis.count[0]

                    if trimmed_values_count[column_index] == trimmed_values.shape[0]/2:
                        # Tie breaker
                        column_mode: int = 0
                    else:
                        column_mode: int = int(inverse_binary_string(str(trimmed_values_mode[column_index])))

                    return trim_values(trimmed_values=trimmed_values[trimmed_values[:, column_index] == column_mode], 
                                       column_index=column_index+1)
            solution_row: array = trim_values(trimmed_values=diagnostic_values, column_index=0)
            return int("".join([str(value) for value in solution_row]), 2)

        @staticmethod
        def life_support_rating(CO2_scrubber_rating: int, oxygen_generator_rating: int) -> int:
            return CO2_scrubber_rating * oxygen_generator_rating

        @staticmethod
        def epsilon_rate(diagnostic_values: array) -> int:
            diagnostic_values_mode = mode(diagnostic_values, axis=0).mode[0]
            return int(inverse_binary_string("".join([str(value) for value in diagnostic_values_mode])), 2)

        @staticmethod
        def power_consumption(gamma_rate: int, epislon_rate: int) -> int:
            return gamma_rate * epislon_rate

    @staticmethod
    def load(diagnostirc_report_file_path: str) -> DiagnosticReport:
        assert isfile(diagnostirc_report_file_path), f"File not found: {diagnostirc_report_file_path}"
        diagnostic_values: List[array] = []

        with open(diagnostirc_report_file_path) as diagnostic_report_file:
            for file_line in diagnostic_report_file.readlines():
                report_line: array = array([int(value) for value in file_line if value != "\n"])
                diagnostic_values.append(report_line)

        return DiagnosticReport(diagnostic_values=array(diagnostic_values))


def inverse_binary_string(binary_string: str) -> str:
    inverse: str = ""

    for value in binary_string:
        if value == "0":
            inverse += "1"
        else:
            inverse += "0"

    return inverse

class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        diagnostic_report: DiagnosticReport = DiagnosticReport.load(diagnostirc_report_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(diagnostic_report.gamma_rate, 22)
        self.assertEqual(diagnostic_report.epsilon_rate, 9)
        self.assertEqual(diagnostic_report.power_consuption, 198)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        diagnostic_report: DiagnosticReport = DiagnosticReport.load(diagnostirc_report_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(diagnostic_report.oxygen_generator_rating, 23)
        self.assertEqual(diagnostic_report.CO2_scrubber_rating, 10)
        self.assertEqual(diagnostic_report.life_support_rating, 230)

        print(f"Unittest {Examples.test_part_two_example} was successful.")

class Solutions(TestCase):
    pass
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        diagnostic_report: DiagnosticReport = DiagnosticReport.load(diagnostirc_report_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part one solution calculated to be: {diagnostic_report.power_consuption}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        diagnostic_report: DiagnosticReport = DiagnosticReport.load(diagnostirc_report_file_path=join(dirname(__file__), "input.txt"))

        print(f"Part two solution calculated to be: {diagnostic_report.life_support_rating}.")

if __name__ == "__main__":
    main()
