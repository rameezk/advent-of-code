from aoc.helper import AOC


@AOC.puzzle(2022, 18, 1)
def solve():
    data = AOC.get_data()

#     data = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5"""

    cubes = set()
    for line in data.strip().splitlines():
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    surface_area = 0
    for x, y, z in cubes:
        neighbors = [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]

        for neighbor in neighbors:
            if neighbor not in cubes:
                surface_area += 1

    print(surface_area)
    AOC.submit_answer(surface_area)


if __name__ == "__main__":
    solve()
