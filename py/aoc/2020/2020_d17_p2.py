from aoc.helper import AOC

@AOC.puzzle(2020, 17, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """.#.
# ..#
# ###""".splitlines()

    active = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                active.add((x, y, 0, 0))

    def get_neighbors(x, y, z, w):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        neighbors.append((x + dx, y + dy, z + dz, w + dw))
        return neighbors

    for cycle in range(6):
        candidates = set()
        for (x, y, z, w) in active:
            candidates.add((x, y, z, w))
            for neighbor in get_neighbors(x, y, z, w):
                candidates.add(neighbor)

        new_active = set()
        for (x, y, z, w) in candidates:
            neighbor_count = 0
            for neighbor in get_neighbors(x, y, z, w):
                if neighbor in active:
                    neighbor_count += 1

            if (x, y, z, w) in active:
                if neighbor_count == 2 or neighbor_count == 3:
                    new_active.add((x, y, z, w))
            else:
                if neighbor_count == 3:
                    new_active.add((x, y, z, w))

        active = new_active

    answer = len(active)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
