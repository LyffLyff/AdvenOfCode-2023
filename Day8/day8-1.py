# --- Day 8: Haunted Wasteland ---
# https://adventofcode.com/2023/day/8

# If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL -> RLRLRLRLRLRL

from enum import IntEnum


file = open("input.txt")
input = file.readlines()
file.close()

# get right and left instructions at the start
directional_instructions = input.pop(0)

nodes: dict = {
    # start node = [rightPath, leftPath]
}

# format input
for line in input:
    if line == "\n":
        continue
    temp = line.replace("\n", "").replace(")", "").replace("(", "").split(" = ")
    nodes[temp[0]] = temp[1].split(", ")

print(directional_instructions)
print(nodes)


class Path(IntEnum):
    LEFT_PATH = 0
    RIGHT_PATH = 1


# find path to ZZZ
found_path = False
step_counter = 0
current_node: str = "AAA"
while not found_path:
    # retry until at ZZZ
    for direction in directional_instructions:
        if direction == "L":
            current_node = nodes[current_node][Path.LEFT_PATH]
        elif direction == "R":
            current_node = nodes[current_node][Path.RIGHT_PATH]
        else:
            print("HUH?")
            break
        step_counter += 1

    # check if at ZZZ
    if current_node == "ZZZ":
        found_path = True

print("REQUIRED STEPS:", step_counter)
