from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2019, 24, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    initial_bugs = set()
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == '#':
                initial_bugs.add((r, c))

    bugs = {0: initial_bugs}

    def get_neighbors(level, r, c):
        neighbors = []

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if nr == 2 and nc == 2:
                if dr == -1:
                    for i in range(5):
                        neighbors.append((level + 1, 4, i))
                elif dr == 1:
                    for i in range(5):
                        neighbors.append((level + 1, 0, i))
                elif dc == -1:
                    for i in range(5):
                        neighbors.append((level + 1, i, 4))
                elif dc == 1:
                    for i in range(5):
                        neighbors.append((level + 1, i, 0))
            elif 0 <= nr < 5 and 0 <= nc < 5:
                neighbors.append((level, nr, nc))
            else:
                if nr < 0:
                    neighbors.append((level - 1, 1, 2))
                elif nr >= 5:
                    neighbors.append((level - 1, 3, 2))
                elif nc < 0:
                    neighbors.append((level - 1, 2, 1))
                elif nc >= 5:
                    neighbors.append((level - 1, 2, 3))

        return neighbors

    for _ in range(200):
        min_level = min(bugs.keys()) - 1
        max_level = max(bugs.keys()) + 1

        new_bugs = {}

        for level in range(min_level, max_level + 1):
            current_bugs = bugs.get(level, set())
            next_bugs = set()

            for r in range(5):
                for c in range(5):
                    if r == 2 and c == 2:
                        continue

                    neighbors = get_neighbors(level, r, c)
                    adjacent_bugs = sum(
                        1 for nl, nr, nc in neighbors if nl in bugs and (nr, nc) in bugs[nl]
                    )

                    if (r, c) in current_bugs:
                        if adjacent_bugs == 1:
                            next_bugs.add((r, c))
                    else:
                        if adjacent_bugs in [1, 2]:
                            next_bugs.add((r, c))

            if next_bugs:
                new_bugs[level] = next_bugs

        bugs = new_bugs

    answer = sum(len(b) for b in bugs.values())
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
