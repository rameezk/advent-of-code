from aoc.helper import AOC

from aoc.util import adj


@AOC.puzzle(year=2024, day=12, part=2)
def solve():
    data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
    data = """AAAA
BBCD
BBCC
EEEC"""
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

            region, plant = find_contiguous_region(garden_plot, pos, seen)

            area = len(region)
            sides = calculate_number_of_sides(region)

            price = area * sides

            total_price += price

    print(total_price)
    assert total_price == 858684
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

    return region, plant


def calculate_number_of_sides(region):
    edges = get_edges(region)

    sides = 0
    seen = set()
    for edge, direction in edges.items():
        if edge in seen:
            continue

        seen.add(edge)

        sides += 1

        e_r, e_c = edge

        if e_r.is_integer():
            for d_r in [-1, 1]:
                c_r = e_r + d_r
                while edges.get((c_r, e_c)) == direction:
                    seen.add((c_r, e_c))
                    c_r += d_r
        else:
            for d_c in [-1, 1]:
                c_c = e_c + d_c
                while edges.get((e_r, c_c)) == direction:
                    seen.add((e_r, c_c))
                    c_c += d_c
    return sides


def get_edges(region):
    edges = {}
    for r, c in region:
        for n_r, n_c in adj((r, c), diagonal=False):
            if (n_r, n_c) in region:
                continue

            e_r = (r + n_r) / 2
            e_c = (c + n_c) / 2

            edges[(e_r, e_c)] = (e_r - r, e_c - c)
    return edges


if __name__ == "__main__":
    solve()
