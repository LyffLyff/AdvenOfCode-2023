# https://adventofcode.com/2023/day/6
import numpy
import re

file = open("input.txt")
input = file.readlines()
file.close()

times = []
records = []

for line in range(0, len(input), 2):
    # removing spaces between numbers before using regex -> one single number
    times = re.findall(r"\d+", input[line].replace(" ", ""))
    records = re.findall(r"\d+", input[line + 1].replace(" ", ""))

    # convert to integers
    times = [int(numeric_string) for numeric_string in times]
    records = [int(numeric_string) for numeric_string in records]

print("TIMES: ", times)
print("RECORDS: ", records)

ways_to_win: list[int] = [0] * len(times)

SPEED_PER_HOLD_TIME: int = 1  # millimeter per millisecond

for i in range(len(times)):
    corresponding_record = records[i]
    print("RECORD TO BEAT:", corresponding_record)
    for hold_time in range(times[i]):
        # calculating the range of the boat for every hold time
        rest_time = times[i] - hold_time
        length = (hold_time * SPEED_PER_HOLD_TIME) * rest_time
        if length > corresponding_record:
            ways_to_win[i] += 1

print("WAYS TO WIN:", ways_to_win)
print("MUlTIPLIED WAYS:", numpy.prod(ways_to_win))
