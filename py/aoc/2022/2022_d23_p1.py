from aoc.helper import AOC


@AOC.puzzle(2022, 23, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#..""".splitlines()

    elves = set()
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == '#':
                elves.add((r, c))

    directions = [
        ('N', [(-1, -1), (-1, 0), (-1, 1)]),
        ('S', [(1, -1), (1, 0), (1, 1)]),
        ('W', [(-1, -1), (0, -1), (1, -1)]),
        ('E', [(-1, 1), (0, 1), (1, 1)])
    ]

    direction_moves = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    all_neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for round_num in range(10):
        proposals = {}
        proposal_counts = {}

        for r, c in elves:
            has_neighbor = False
            for dr, dc in all_neighbors:
                if (r + dr, c + dc) in elves:
                    has_neighbor = True
                    break

            if not has_neighbor:
                continue

            for direction, checks in directions:
                can_move = True
                for dr, dc in checks:
                    if (r + dr, c + dc) in elves:
                        can_move = False
                        break

                if can_move:
                    dr, dc = direction_moves[direction]
                    new_pos = (r + dr, c + dc)
                    proposals[(r, c)] = new_pos
                    proposal_counts[new_pos] = proposal_counts.get(new_pos, 0) + 1
                    break

        new_elves = set()
        for r, c in elves:
            if (r, c) in proposals:
                proposed = proposals[(r, c)]
                if proposal_counts[proposed] == 1:
                    new_elves.add(proposed)
                else:
                    new_elves.add((r, c))
            else:
                new_elves.add((r, c))

        elves = new_elves
        directions.append(directions.pop(0))

    min_r = min(r for r, c in elves)
    max_r = max(r for r, c in elves)
    min_c = min(c for r, c in elves)
    max_c = max(c for r, c in elves)

    area = (max_r - min_r + 1) * (max_c - min_c + 1)
    empty = area - len(elves)

    print(empty)
    AOC.submit_answer(empty)


if __name__ == "__main__":
    solve()
