# https://adventofcode.com/2023/day/5
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.


# reversing the process from part 1 -> check every single location from zero until an existing seed is found
# if a seed is found -> check if location even in the "humidity-to-location-map" -> else try next

import re

file = open("input.txt")
input = file.readlines()
file.close()

map_keys: list[str] = []

seeds: list[str] = []
ranges_seeds: list = []
dst_2_src_correlation: {str: str} = {
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
        # this is 50% of the magic trick and i do not know why
        return number in range(self.min + self.offset, self.max + 1 + self.offset)

    def get_src(self, number: int) -> int:
        print("OFFSET:", self.offset)
        return number - self.offset


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
        # print(self.ranges[0])

    def get_previous_destination_number(
        self, source_title: str, dst_number: int
    ) -> int:
        # checks a source category and maps it to a new category with a specific number
        for range in self.ranges:
            # print(dst_number)
            if CategoryRange.is_in_range(range, dst_number):
                # number found in previous maps range -> return that range
                return CategoryRange.get_src(range, dst_number)
        # if number not in the previous one -> return the same number
        return dst_number

    def get_ranges(self):
        return ["Min: " + str(i.min) + " Max: " + str(i.max) for i in self.ranges]

    def get_minimum_ranges(self) -> list:
        minimums: list = []
        for i in self.ranges:
            minimums.append(i.min)
        minimums.sort()
        return minimums

    def get_lowest_range(self):
        lowest = ()
        for i in self.ranges:
            if lowest == () or i.min < lowest[0]:
                lowest = (i.min, i.max)
        return lowest


def init_maps():
    # create map of all -> source and destination maps with their ranges

    # seeds
    global ranges_seeds
    global seeds
    seed_ranges = input.pop(0).split(" ")
    ranges_seeds = []
    for i in range(1, len(seed_ranges), 2):
        # from 1 -> skipping "seeds:"
        ranges_seeds.append(
            (int(seed_ranges[i]), int(seed_ranges[i]) + int(seed_ranges[i + 1]))
        )

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
            dst_2_src_correlation[current_destination] = current_source
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
            category_maps[current_source].add_range(
                CategoryRange(
                    src_range_start,
                    src_range_start + range_length - 1,
                    dst_range_start - src_range_start,
                ),
            )


def get_lowest_location() -> None:
    current_src: str = "location"
    current_dst = ""
    location_number = 45

    while True:
        print("Checking Location Number:", location_number)

        # starting at humidity -> location the end result of the humidity-map
        if current_dst == "":
            # get relating destination from source
            number = location_number
            current_src = "location"
            current_dst = "humidity"

        # working up from location until seeds
        while True:
            # loop until at seeds
            number = CategoryType.get_previous_destination_number(
                category_maps[current_dst], current_src, number
            )
            current_src = current_dst
            current_dst = dst_2_src_correlation[current_dst]
            if current_dst == "seed":
                # location of seed found -> find the next
                for seed_range in ranges_seeds:
                    if number >= seed_range[0] and number <= seed_range[1]:
                        print("VALID LOCATION: ", location_number)
                        return location_number
                current_dst = ""
                break

        # find next location number in range to check corresponding seed
        while True:
            location_number += 1
            break


category_maps: [str, CategoryType] = {}

# organize seeds into usable classes
init_maps()

print(dst_2_src_correlation)

print("LOWEST LOCATION NUMBER: ", get_lowest_location())

# print("SEED LOCATIONS: ", locations)
# print("LOWEST LOCATION NUMBER:", min(locations))
