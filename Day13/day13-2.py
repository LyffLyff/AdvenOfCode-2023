# --- Day 13: Point of Incidence ---
# -> # = Stone
# -> . = Ash

file = open("input.txt")
input = file.readlines()
file.close()

blocks = []
block_counter = 0

# divide into diffenrent blocks
for line in input:
    # new block
    if len(blocks) <= block_counter:
        blocks.append([])

    # check line
    if line == "\n":
        # new block
        block_counter += 1
        continue

    # add line
    blocks[block_counter].append(line)


print(blocks)


def check_valid_horizontal_reflection(block: list, index: int):
    # get block and potential index
    reflection_offset = 0
    while True:
        upper_limit = index + reflection_offset + 1
        lower_limit = index - reflection_offset

        if lower_limit < 0 or upper_limit > len(block) - 1:
            # all reflections are valid and the block runs out of data to check -> index is a reflection
            return True

        if block[lower_limit] == block[upper_limit]:
            # checking if the right and left side of the mirror are the same -> check next -> increment offset from mirror
            reflection_offset += 1
        else:
            return False


# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection;
# to that, also add 100 multiplied by the number of rows above each horizontal line of reflection.
sum = 0
counter = 0

for block_index in range(len(blocks)):
    found = False
    counter += 1
    # check horizontally
    current_block = blocks[block_index]

    block_height = len(current_block)
    block_length = len(current_block[0]) - 1

    # rows
    for y in range(block_height - 1):
        if current_block[y] == current_block[y + 1]:
            if check_valid_horizontal_reflection(current_block, y) == True:
                print(current_block[y], current_block[y + 1])
                print("HORIZONTAL BETWEEN:", y + 1, y + 2)
                sum += 100 * (y + 1)
                found = True
                break

    # columns
    # "turning" the 2d-Array so the columns and rows are switched
    transposed_block = [
        [current_block[j][i] for j in range(len(current_block))]
        for i in range(len(current_block[0]))
    ]

    # removing line of \n
    transposed_block.pop(-1)

    # now the same process as with horizontal checking thanks to the  transposed block
    # block length and height must be switched though
    for y in range(len(transposed_block) - 1):
        if transposed_block[y] == transposed_block[y + 1]:
            if check_valid_horizontal_reflection(transposed_block, y, True) == True:
                print(transposed_block[y], transposed_block[y + 1])
                print("VERTICAL BETWEEN:", y + 1, y + 2)
                sum += y + 1
                break

    print("-----------------------NEXT BLOCK----------------------------------")

print("SUM:", sum)
