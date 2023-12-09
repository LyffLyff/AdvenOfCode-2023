# --- Day 8: Haunted Wasteland ---
# https://adventofcode.com/2023/day/8

# If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL -> RLRLRLRLRLRL

# Here, there are two starting nodes, 11A and 22A (because they both end with A).
# As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on.
# Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.)

# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

from enum import IntEnum
import numpy as np


file = open("input.txt")
input = file.readlines()
file.close()

# get right and left instructions at the start
directional_instructions = input.pop(0).replace("\n", "")

nodes: {int: list} = {
    # start node = [rightPath, leftPath]
}


# format input
current_nodes: list[str] = []

for line in input:
    if line == "\n":
        continue
    temp = line.replace("\n", "").replace(")", "").replace("(", "").split(" = ")
    paths = temp[1].split(", ")

    if temp[0].endswith("A"):
        current_nodes.append(temp[0])

    nodes[temp[0]] = paths


print(directional_instructions)
print(nodes)
print(current_nodes)


class Path(IntEnum):
    LEFT_PATH = 0
    RIGHT_PATH = 1


# find path to where all end in Z
node_counters: list[int] = []
for current_node in current_nodes:
    step_counter = 0
    found_path = False
    while not found_path:
        # retry until at ZZZ
        for direction in directional_instructions:
            if direction == "L":
                current_node = nodes[current_node][Path.LEFT_PATH]
            elif direction == "R":
                current_node = nodes[current_node][Path.RIGHT_PATH]

            else:
                print("WRONG DIRECTION: ", direction)
                break
            step_counter += 1

            # check if at XXZ
            if current_node.endswith("Z"):
                found_path = True
                break
    node_counters.append(step_counter)

print("REQUIRED STEPS FOR EACH A-Node:", node_counters)

required_steps: int


# ok, so the number of required steps for every "instance"? duplicate? of the ghosts is equal to the lowest common multiple (LCM) of each "A"-Node reaching a "Z"-Node
# -> THE NUMPY np.lcm.reduce(array) DOES NOT WORK for some ungodly reason
def find_lcm(num1, num2):
    # stolen from: https://www.geeksforgeeks.org/lcm-of-given-array-elements/
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


for i in range(0, len(node_counters)):
    if i == 0:
        lcm = node_counters[0]
    lcm = find_lcm(lcm, node_counters[i])

print("LOWEST COMMON MULTIPLE:", lcm)
