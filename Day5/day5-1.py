# https://adventofcode.com/2023/day/5
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

import re

file = open("input.txt")
input = file.readlines()
file.close()

map_keys: list[str] = []

seeds: list[str] = []
src_2_dst_correlation: {str: str} = {
    # src : dst
}


class CategoryRange:
    # simple range class
    min: int = 0
    max: int = 0
    offset: int = 0

    def __init__(self, min, max, offset):
        self.min = min
        self.max = max
        self.offset = offset

    def is_in_range(self, number: int) -> bool:
        return number in range(self.min, self.max + 1)

    def get_dst(self, number: int) -> int:
        return number + self.offset


class CategoryType:
    mapper_title: str = ""  # e.g. soil or humidity
    ranges: list[CategoryRange] = []

    def __init__(self, title: str):
        self.ranges = (
            []
        )  # TOP TIP: If you do not initialize a variable like this within the init function it causes it to take values from other previous instances of this class
        self.mapper_title = title

    def add_range(self, range_map: CategoryRange) -> None:
        self.ranges.append(range_map)
        print(self.ranges[0])

    def get_destination_number(
        self, source_title: str, source_number: int
    ) -> [str, int]:
        # checks a source category and maps it to a new category with a specific number
        for range in self.ranges:
            if CategoryRange.is_in_range(range, source_number):
                print(source_title)
                return ["", CategoryRange.get_dst(range, source_number)]
        # if not within any range source number equals destination number
        return ["", source_number]


def init_maps():
    # create map of all -> source and destination maps with their ranges

    # seeds
    global seeds
    seeds = re.findall(r"\d+", input.pop(0))
    # seeds = [int(seed) for seed in seeds]
    print(seeds)

    current_source = ""
    current_destination = ""

    # source and destination maps
    for line in input:
        idx = line.find(":")
        if idx != -1:
            x = line.split("-")
            map_keys.append(x[0])

            # adding ne mapping from one to another type of need for plants
            # "temperature-humidity"
            start_dst_key = line[0:idx].replace("-to-", "-").replace(" map", "")
            [current_source, current_destination] = start_dst_key.split("-")
            src_2_dst_correlation[current_source] = current_destination
            category_maps[current_source] = CategoryType(current_source)
            category_maps[current_destination] = CategoryType(current_destination)
        elif len(line) - 1 > 0:
            # initialize ranges of maps
            [dst_range_start, src_range_start, range_length] = re.findall(r"\d+", line)
            [dst_range_start, src_range_start, range_length] = [
                int(dst_range_start),
                int(src_range_start),
                int(range_length),
            ]

            # set updated range from source and destination category
            print(current_source)
            print(
                category_maps[current_source].mapper_title,
                "MIN:" + str(src_range_start),
                "MAX:" + str(src_range_start + range_length - 1),
            )
            category_maps[current_source].add_range(
                CategoryRange(
                    src_range_start,
                    src_range_start + range_length - 1,
                    dst_range_start - src_range_start,
                ),
            )


def get_seed_locations() -> list[int]:
    locations: list[int] = []
    current_src: str
    number = 0
    current_dst = ""

    for seed in seeds:
        current_src = "seed"
        if current_dst == "":
            # get relating destination from source
            number = int(seed)
            current_dst = "seed"
        while True:
            # loop until at location
            print(number)
            print(category_maps[current_dst].mapper_title)
            [title, number] = CategoryType.get_destination_number(
                category_maps[current_dst], current_src, number
            )
            current_src = current_dst
            if current_src == "location":
                # location of seed found -> find the next
                locations.append(number)
                current_dst = ""
                break
            current_dst = src_2_dst_correlation[current_src]

    return locations


category_maps: [str, CategoryType] = {}

# organize seeds into usable classes
init_maps()

print(category_maps["soil"].ranges[0])

# find corresponding location for seeds
locations = get_seed_locations()

print("SEED LOCATIONS: ", locations)
print("LOWEST LOCATION NUMBER:", min(locations))
