# https://adventofcode.com/2023/day/10


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

from enum import Enum

file = open("input.txt")
input = file.readlines()
file.close()


class PipeDirections(Enum):
    ABOVE = 2
    BELOW = 2
    LEFT = 3
    RIGHT = 4


class PipeChecker:
    global input
    check_coordinates = ()
    start_coordinates = ()
    pipe_network_coords: list[tuple] = []
    grid_length = -1
    grid_height = -1

    pipe_offset = {
        # what coordinate changes when going that path -> positive when down -> negative when up -> only on straight pipes
        "-": (1, 0),
        "|": (0, 1),
        "L": (1, 1),
        "J": (1, -1),
        "7": (-1, -1),
        "F": (1, -1),
    }

    pipe_dict = {
        # what a current pipe "accepts" as a connection in each direction
        "|": {
            PipeDirections.BELOW: ["L", "J", "|"],
            PipeDirections.ABOVE: ["7", "F", "|"],
            PipeDirections.RIGHT: [],
            PipeDirections.LEFT: [],
        },
        "-": {
            PipeDirections.BELOW: [],
            PipeDirections.ABOVE: [],
            PipeDirections.RIGHT: ["-", "J", "7"],
            PipeDirections.LEFT: ["-", "L", "F"],
        },
        "L": {
            PipeDirections.BELOW: [],
            PipeDirections.ABOVE: ["|", "7", "F"],
            PipeDirections.RIGHT: ["-", "J", "7"],
            PipeDirections.LEFT: [],
        },
        "J": {
            PipeDirections.BELOW: [],
            PipeDirections.ABOVE: ["7", "|", "F"],
            PipeDirections.RIGHT: [],
            PipeDirections.LEFT: ["L", "-", "F"],
        },
        "7": {
            PipeDirections.BELOW: ["|", "L", "J"],
            PipeDirections.ABOVE: [],
            PipeDirections.RIGHT: [],
            PipeDirections.LEFT: ["-", "L", "F"],
        },
        "F": {
            PipeDirections.BELOW: ["|", "L", "J"],
            PipeDirections.ABOVE: [],
            PipeDirections.RIGHT: ["-", "J", "7"],
            PipeDirections.LEFT: [],
        },
        "S": {
            PipeDirections.BELOW: ["|", "L", "J"],
            PipeDirections.ABOVE: ["|", "7", "F"],
            PipeDirections.RIGHT: ["-"],
            PipeDirections.LEFT: ["-"],
        },
    }

    direction_dict = {
        # all the possible pipes depending on where is currently checked
        PipeDirections.BELOW: {"|", "L", "J"},
        PipeDirections.ABOVE: {"|", "7", "F"},
        PipeDirections.RIGHT: {"-", "J", "7"},
        PipeDirections.LEFT: {"-", "L", "F"},
    }

    def __init__(self, max_x, max_y, start_coordinates):
        self.grid_length = max_x
        self.grid_height = max_y
        self.start_coordinates = start_coordinates

    def get_current_x_coordinate(self) -> int:
        return self.check_coordinates[0]

    def get_current_y_coordinate(self) -> int:
        return self.check_coordinates[1]

    def get_pipe_character(self, y, x) -> str:
        return input[y][x]

    def check_connection(self):
        if (
            self.get_current_y_coordinate()
            or self.get_current_y_coordinate() < 0
            or self.get_current_x_coordinate() < 0
            or self.get_current_x_coordinate() > self.grid_length
        ):
            # Invalid grid position
            return -1

        self.get_pipe_character()


# find start coords
start_coordinates = (0, 0)
for y in range(len(input)):
    x = input[y].find("S")
    if x != -1:
        start_coordinates = (x, y)
current_coordinates = start_coordinates
print(start_coordinates)

# create pipe class
pipe_checker = PipeChecker(len(input), len(input[y]), start_coordinates)


# follow directions
while True:
    # check above
    pipe_checker.check_coordinates = (
        current_coordinates[0],
        current_coordinates[1] - 1,
    )

    pipe_checker.check_connection()

    # check below
    pipe_checker.check_coordinates = (
        current_coordinates[0],
        current_coordinates[1] + 1,
    )

    # check left
    pipe_checker.check_coordinates = (
        current_coordinates[0] - 1,
        current_coordinates[1],
    )

    # check right
    pipe_checker.check_coordinates = (
        current_coordinates[0] + 1,
        current_coordinates[1],
    )
