from aoc.helper import AOC


@AOC.puzzle(2018, 22, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """depth: 510
# target: 10,10"""

    depth = None
    target = None

    for line in data:
        if line.startswith("depth:"):
            depth = int(line.split(": ")[1])
        elif line.startswith("target:"):
            coords = line.split(": ")[1].split(",")
            target = (int(coords[0]), int(coords[1]))

    target_x, target_y = target

    erosion_levels = {}

    def get_erosion_level(x, y):
        if (x, y) in erosion_levels:
            return erosion_levels[(x, y)]

        if (x, y) == (0, 0):
            geologic_index = 0
        elif (x, y) == target:
            geologic_index = 0
        elif y == 0:
            geologic_index = x * 16807
        elif x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = get_erosion_level(x - 1, y) * get_erosion_level(x, y - 1)

        erosion_level = (geologic_index + depth) % 20183
        erosion_levels[(x, y)] = erosion_level
        return erosion_level

    total_risk = 0
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            erosion = get_erosion_level(x, y)
            region_type = erosion % 3
            total_risk += region_type

    print(total_risk)
    AOC.submit_answer(total_risk)


if __name__ == "__main__":
    solve()
