from aoc.helper import AOC

from aoc.util import adj


@AOC.puzzle(year=2024, day=12, part=1)
def solve():
    data = """AAAA
BBCD
BBCC
EEEC"""
    data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
    data = AOC.get_data()

    garden_plot = [row for row in data.strip().splitlines()]

    max_r, max_c = len(garden_plot), len(garden_plot[0])

    seen = set()
    total_price = 0

    for r in range(max_r):
        for c in range(max_c):
            pos = (r, c)
            if pos in seen:
                continue

            region = find_contiguous_region(garden_plot, pos, seen)

            area = len(region)
            perimeter = calculate_perimeter(region)

            price = area * perimeter

            total_price += price

    print(total_price)
    AOC.submit_answer(total_price)


def find_contiguous_region(garden_plot, starting_position, seen):
    plant = garden_plot[starting_position[0]][starting_position[1]]
    max_r, max_c = len(garden_plot), len(garden_plot[0])
    stack = [starting_position]
    region = []

    while stack:
        r, c = stack.pop()

        if (r, c) in seen:
            continue

        seen.add((r, c))
        region.append((r, c))

        for n_r, n_c in adj((r, c), diagonal=False):
            if (
                0 <= n_r < max_r
                and 0 <= n_c < max_c
                and garden_plot[n_r][n_c] == plant
                and (n_r, n_c) not in seen
            ):
                stack.append((n_r, n_c))

    return region


def calculate_perimeter(region):
    perimeter = 0

    for r, c in region:
        for n_r, n_c in adj((r, c), diagonal=False):
            if (n_r, n_c) not in region:
                perimeter += 1

    return perimeter


if __name__ == "__main__":
    solve()
