# https://adventofcode.com/2023/day/6
import numpy
import re

file = open("input.txt")
input = file.readlines()
file.close()

times = []
records = []

for line in range(0, len(input), 2):
    # find different races, times and the corresponding record
    times = re.findall(r"\d+", input[line])
    records = re.findall(r"\d+", input[line + 1])

    # convert to integers
    times = [int(numeric_string) for numeric_string in times]
    records = [int(numeric_string) for numeric_string in records]

print("TIMES: ", times)
print("RECORDS: ", records)

ways_to_win: list[int] = [0] * len(times)

SPEED_PER_HOLD_TIME: int = 1  # millimeter per millisecond

for i in range(len(times)):
    corresponding_record = records[i]
    for hold_time in range(times[i]):
        # calculating the range of the boat for every hold time
        rest_time = times[i] - hold_time
        length = (hold_time * SPEED_PER_HOLD_TIME) * rest_time
        print(corresponding_record)
        if length > corresponding_record:
            ways_to_win[i] += 1

print("WAYS TO WIN:", ways_to_win)
print("MUlTIPLIED WAYS:", numpy.prod(ways_to_win))
