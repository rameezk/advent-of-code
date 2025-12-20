from aoc.helper import AOC

@AOC.puzzle(2020, 17, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """.#.
# ..#
# ###""".splitlines()

    active = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                active.add((x, y, 0))

    def get_neighbors(x, y, z):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    neighbors.append((x + dx, y + dy, z + dz))
        return neighbors

    for cycle in range(6):
        candidates = set()
        for (x, y, z) in active:
            candidates.add((x, y, z))
            for neighbor in get_neighbors(x, y, z):
                candidates.add(neighbor)

        new_active = set()
        for (x, y, z) in candidates:
            neighbor_count = 0
            for neighbor in get_neighbors(x, y, z):
                if neighbor in active:
                    neighbor_count += 1

            if (x, y, z) in active:
                if neighbor_count == 2 or neighbor_count == 3:
                    new_active.add((x, y, z))
            else:
                if neighbor_count == 3:
                    new_active.add((x, y, z))

        active = new_active

    answer = len(active)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
