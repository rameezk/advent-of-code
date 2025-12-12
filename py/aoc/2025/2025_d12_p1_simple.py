from dataclasses import dataclass

from aoc.helper import AOC


@dataclass
class Region:
    width: int
    height: int
    quantities: list[int]


def parse_shape_area(lines):
    return sum(line.count("#") for line in lines)


def parse_input(data):
    sections = data.strip().split("\n\n")

    shape_areas = {}
    for section in sections[:-1]:
        lines = section.strip().splitlines()
        index = int(lines[0].rstrip(":"))
        shape_areas[index] = parse_shape_area(lines[1:])

    regions = []
    for line in sections[-1].strip().splitlines():
        size_part, quantities_part = line.split(":")
        width, height = map(int, size_part.split("x"))
        quantities = list(map(int, quantities_part.strip().split()))
        regions.append(Region(width, height, quantities))

    return shape_areas, regions


def can_fit(shape_areas, region):
    total_shape_area = sum(
        shape_areas[idx] * qty for idx, qty in enumerate(region.quantities)
    )
    region_area = region.width * region.height
    return total_shape_area <= region_area


@AOC.puzzle(2025, 12, 1)
def solve():
    data = AOC.get_data()

    shape_areas, regions = parse_input(data)
    valid_count = sum(1 for region in regions if can_fit(shape_areas, region))

    print(valid_count)
    AOC.submit_answer(valid_count)


if __name__ == "__main__":
    solve()
