# https://adventofcode.com/2023/day/3
import re
from itertools import zip_longest

file = open("input.txt")

input = file.readlines()

file.close()

shematic_length = len(input[0])


def find_symbols(text) -> list[int]:
    indeces = []
    for index, char in enumerate(text):
        if not (char.isdigit() or char == "." or char == "\n"):
            indeces.append(index)
    return (
        indeces  # returning indeces of every character that is neither a number or "."
    )


part_numbers: list[str] = []

for line in range(len(input)):
    # symbols indices
    upper_line_symbols = find_symbols(input[line - 1]) if line - 1 >= 0 else []
    line_symbols = find_symbols(input[line])
    below_line_symbols = find_symbols(input[line + 1]) if line + 1 < len(input) else []

    # find matching parts
    for match in re.finditer(r"\d+", input[line]):
        print("Check Number: " + match.group())
        for upper_symbol_index, inline_symbol_index, below_symbol_index in zip_longest(
            upper_line_symbols,
            line_symbols,
            below_line_symbols,
        ):
            check_range = range(match.start() - 1, match.end() + 1)

            # check if numbers matches any symbol above
            if upper_symbol_index in check_range:
                print("ABOVE")
                part_numbers.append(match.group())
                break  # break out of symbol check loop

            # check if numbers matches any symbol in line
            if inline_symbol_index in check_range:
                print("INLINE")
                part_numbers.append(match.group())
                break

            # check if numbers matches any symbol below line
            if below_symbol_index in check_range:
                print("BELOW")
                part_numbers.append(match.group())
                break

print("SUM OF ALL PARTS:", sum([int(x) for x in part_numbers]))
