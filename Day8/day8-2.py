# --- Day 8: Haunted Wasteland ---
# https://adventofcode.com/2023/day/8

# If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL -> RLRLRLRLRLRL

# Here, there are two starting nodes, 11A and 22A (because they both end with A).
# As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on.
# Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.)

# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

from enum import IntEnum


file = open("input.txt")
input = file.readlines()
file.close()

# get right and left instructions at the start
directional_instructions = input.pop(0).replace("\n", "")

nodes: {int: list} = {
    # start node = [rightPath, leftPath]
}


# format input
z_nodes = {
    # number : original_string
}
current_nodes: list[int] = []

hash_counter = 0
hash_map: dict = {
    # original string : number
}


def hash_string(input_string: str) -> int:
    global hash_counter, hash_map, z_nodes

    # already hashed
    if hash_map.get(input_string, -1) != -1:
        return hash_map.get(input_string)

    # new hash
    hash_counter += 1
    if input_string[2] == "A":
        # finding current nodes
        current_nodes.append(hash_counter)
    elif input_string[2] == "Z":
        # adding to the map to match numbers to if they're where ending with a Z
        z_nodes[hash_counter] = input_string

    hash_map[input_string] = hash_counter

    return hash_counter


for line in input:
    if line == "\n":
        continue
    temp = line.replace("\n", "").replace(")", "").replace("(", "").split(" = ")
    paths = temp[1].split(", ")
    for i in range(2):
        paths[i] = hash_string(paths[i])

    node_number = hash_string(temp[0])

    nodes[node_number] = paths

print(directional_instructions)
print(nodes)
print("Z-Nodes:", z_nodes)
print(current_nodes)


class Path(IntEnum):
    LEFT_PATH = 0
    RIGHT_PATH = 1


found_path = False
step_counter = 0

# find path to where all end in Z
while not found_path:
    # retry until at ZZZ
    for direction in directional_instructions:
        # print(current_nodes)
        if direction == "L":
            counter = 0
            for num in current_nodes:
                current_nodes[counter] = nodes[num][Path.LEFT_PATH]
                counter += 1
        elif direction == "R":
            counter = 0
            for num in current_nodes:
                current_nodes[counter] = nodes[num][Path.RIGHT_PATH]
                counter += 1

        else:
            print("WRONG DIRECTION: ", direction)
            break
        step_counter += 1

    # check if at ZZZ
    for current_node in current_nodes:
        if z_nodes.get(current_node, -1) == -1:
            break
    else:
        # every node ends with Z
        found_path = True

print("REQUIRED STEPS:", step_counter)
