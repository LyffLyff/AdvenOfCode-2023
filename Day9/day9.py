# --- Day 9: Mirage Maintenance ---

import re

file = open("input.txt")
input = file.readlines()
file.close()


# extract numbers from every history
histories: list[list[int]] = []

for line in input:
    histories.append(
        # new regex -> old could not extract negative numbers
        [int(numeric_string) for numeric_string in re.findall(r"-?\d+", line)]
    )

print(histories)


def calculate_differences(history) -> list:
    diffs = []
    for i in range(len(history) - 1):
        diffs.append(abs(history[i + 1] - history[i]))
    return diffs


def is_all_zeros(array) -> bool:
    for i in array:
        if i != 0:
            return False
    return True


# calculate next value for every history
sum = 0
difference_layers = []
for value_history in histories:
    # calculate difference "pyramid"
    difference_layers = []
    difference_layers.append(value_history)
    while True:
        difference_layers.append(calculate_differences(difference_layers[-1]))
        if is_all_zeros(difference_layers[-1]):
            # check if calculated differences is all ZERO
            difference_layers[-1]
            break

    # extrapolate next value
    if difference_layers[-1] == []:
        # if the last difference layer is not all zeros but empty
        difference_layers.pop(-1)
    extrapolated_value = difference_layers[-1][-1]
    for i in range(len(difference_layers) - 1, 0, -1):
        extrapolated_value = difference_layers[i - 1][-1] + extrapolated_value

    print("EXTRAPOLATED VALUE", extrapolated_value)
    print("----------------------------------")
    sum += extrapolated_value


print("SUM OF EXTRAPOLATED VALUES:", sum)
