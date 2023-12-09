# https://adventofcode.com/2023/day/3
import re
from itertools import zip_longest

file = open("input.txt")

input = file.readlines()

file.close()


def find_gears(text) -> list[int]:
    indeces = []
    for index, char in enumerate(text):
        if char == "*":
            indeces.append(index)
    return indeces  # returning indeces of every gear -> "*"


def find_number(line_idx, digit_idx) -> int:
    line = input[line_idx]
    for match in re.finditer(r"\d+", line):
        if digit_idx in range(match.start(), match.end()):
            # if the digit that was found next to a gear is within the mateched number the part_number is "found" and returned
            return match.group()
    return -1


sum_of_gear_ratios: int = 0

for line in range(len(input)):
    for match in re.finditer(r"\*", input[line]):
        found_numbers = []
        line_idx = line
        shematic_line = input[line]

        # find gear
        gear_position = match.start()

        # check in line
        for i in [-1, +1]:
            if shematic_line[gear_position + i].isdigit():
                # if left of the gear
                found_numbers.append(find_number(line_idx, gear_position + i))

        # check in above
        line_idx = line - 1

        # undivided number handles the cases where two part numbers are in the exact same line but separated within a point
        separatedNumber = True

        if line - 1 >= 0:
            shematic_line = input[line - 1]
            for i in range(-1, 2, 1):
                if shematic_line[gear_position + i] == ".":
                    # reset separated numbers -> allow for multiple number in one line
                    separatedNumber = True

                # if the character is a digit and the previous characters was not a digit aswell
                if shematic_line[gear_position + i].isdigit() and not separatedNumber:
                    # if left of the gear
                    separatedNumber = False
                    found_numbers.append(find_number(line_idx, gear_position + i))

        # check in below
        if line + 1 >= len(input):
            break
        line_idx = line + 1
        shematic_line = input[line + 1]
        separatedNumber = True
        for i in range(-1, 2, 1):
            if shematic_line[gear_position + i] == ".":
                separatedNumber = True
            if shematic_line[gear_position + i].isdigit() and separatedNumber:
                # if left of the gear
                separatedNumber = False
                found_numbers.append(find_number(line_idx, gear_position + i))

        # add up
        print("LINE: ", line)
        print("CHAR IDX: ", match.start())
        print(len(found_numbers))
        print(found_numbers)
        print("----------------------------------------")
        if len(found_numbers) == 2:
            sum_of_gear_ratios += int(found_numbers[0]) * int(found_numbers[1])


print(sum_of_gear_ratios)
