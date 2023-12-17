# --- Day 17: Clumsy Crucible ---


file = open("input.txt")
input = file.readlines()
file.close()

int_array = [[int(char) for char in string.rstrip()] for string in input]

for i in int_array:
    print(i)
