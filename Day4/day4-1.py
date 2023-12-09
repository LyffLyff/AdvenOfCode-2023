# https://adventofcode.com/2023/day/4

import re

file = open("input.txt")
input = file.readlines()
file.close()

total_sum = 0

for line in input:
    # cutting the "Game X:" from the "single game"
    line = line[line.find(": ") + 1:-1]

    [winning_numbers, real_numbers] = line.split("|")

    # convert numbers to array -> each index a number string
    winning_numbers = re.findall(r"\d+", winning_numbers)
    real_numbers = re.findall(r"\d+", real_numbers)

    # calculate points of a single scratchcard
    game_sum = 0
    for winning_num in winning_numbers:
        if winning_num in real_numbers:
            if game_sum == 0:
                # one point on first match
                game_sum = 1
            else:
                # doubling with every extra match
                game_sum *= 2
    total_sum += game_sum

print("SCRATCHCARD SUM: ", total_sum)