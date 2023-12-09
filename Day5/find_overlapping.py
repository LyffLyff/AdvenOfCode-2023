def find_overlapping_ranges(ranges):
    # Sort the ranges by their start values
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    # Initialize a merged range list with the first range
    merged_ranges = [sorted_ranges[0]]

    # Merge overlapping ranges
    for current_start, current_end in sorted_ranges[1:]:
        previous_start, previous_end = merged_ranges[-1]

        if current_start <= previous_end:  # Check for overlap
            merged_ranges[-1] = (previous_start, max(previous_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges


def extract_unique_numbers(ranges):
    unique_numbers = set()

    for start, end in ranges:
        unique_numbers.update(range(start, end + 1))

    return sorted(list(unique_numbers))


# Example array of ranges
ranges = [(1, 5), (3, 900), (12, 18), (15, 20)]

# Find overlapping ranges
overlapping_ranges = find_overlapping_ranges(ranges)
print("Overlapping Ranges:", overlapping_ranges)

# Extract unique numbers from overlapping ranges
unique_numbers = extract_unique_numbers(overlapping_ranges)
print("Unique Numbers from Overlapping Ranges:", unique_numbers)
