import re


file = open("input.txt")

input = file.readlines()

found_numbers = []
sum = 0

word_to_digit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in input:
    print(line, end="")

    # pattern  to find all digits represented as strings aswell as normal digits
    # ?= -> uses a positive lookahead -> findinng overlapping strings aswell
    # without finding overlapping strings -> r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d+)
    found_numbers = re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d+))", line
    )

    # converting texts representing numbers to actual numbers
    for i in range(len(found_numbers)):
        converted = word_to_digit.get(found_numbers[i], -1)
        if converted != -1:
            found_numbers[i] = converted

    print(found_numbers)

    digits = "".join(found_numbers)

    if len(digits) == 1:
        # single number in line
        print(int(digits[0] + digits[0]))
        sum += int(digits[0] + digits[0])
    elif len(digits) > 1:
        # multiple digits in line
        print(int(digits[0] + digits[len(digits) - 1]))
        sum += int(digits[0] + digits[len(digits) - 1])
    else:
        # no digit at all
        print("WHAT THE HEEELLLL -> No digit")

    print("------------------------------------------------------------------")


print("THE END RESULT IS: ", sum)
