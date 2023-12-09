# https://adventofcode.com/2023/day/4

import re

file = open("input.txt")
input = file.readlines()
file.close()

total_scratchcards = 0
card_copies = {
    0 : 1
    # card_number - 1 / index : extra copies (not including the one already there)
}

for card_number in range(len(input)):
    # cutting the "Game X:" from the "single game"
    line = input[card_number]
    line = line[line.find(": ") + 1:-1]

    [winning_numbers, real_numbers] = line.split("|")

    # convert numbers to array -> each index a number string
    winning_numbers = re.findall(r"\d+", winning_numbers)
    real_numbers = re.findall(r"\d+", real_numbers)

    # calculate matches
    if not (card_number in card_copies):
        card_copies[card_number] = 1
    matches = 0
    for winning_num in winning_numbers:
        if winning_num in real_numbers:
            # adding the copies to the dictionary -> keeping count of the extra copies gathered
            matches += 1 
            card_copies[card_number + matches] = card_copies.get(card_number + matches, 1) + (1 * card_copies.get(card_number, 1))

print(card_copies)
total_scratchcards = sum(card_copies.values())

print("AMOUNT OF SCRATCHCARDS: ", total_scratchcards)