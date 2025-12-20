from aoc.helper import AOC
import heapq


@AOC.puzzle(2018, 22, 2)
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

    def get_region_type(x, y):
        return get_erosion_level(x, y) % 3

    ROCKY = 0
    WET = 1
    NARROW = 2

    TORCH = 0
    CLIMBING_GEAR = 1
    NEITHER = 2

    valid_tools = {
        ROCKY: [CLIMBING_GEAR, TORCH],
        WET: [CLIMBING_GEAR, NEITHER],
        NARROW: [TORCH, NEITHER],
    }

    pq = [(0, 0, 0, TORCH)]
    visited = {}

    while pq:
        time, x, y, tool = heapq.heappop(pq)

        if (x, y) == target and tool == TORCH:
            print(time)
            AOC.submit_answer(time)
            return

        state = (x, y, tool)
        if state in visited and visited[state] <= time:
            continue
        visited[state] = time

        region_type = get_region_type(x, y)

        for next_tool in valid_tools[region_type]:
            if next_tool != tool:
                heapq.heappush(pq, (time + 7, x, y, next_tool))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0:
                next_region_type = get_region_type(nx, ny)
                if tool in valid_tools[next_region_type]:
                    heapq.heappush(pq, (time + 1, nx, ny, tool))


if __name__ == "__main__":
    solve()
