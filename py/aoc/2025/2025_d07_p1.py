from aoc.helper import AOC


@AOC.puzzle(2025, 7, 1)
def solve():
    data = AOC.get_data()

#     data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

    splitters = set()
    start = None
    for r, row in enumerate(data.strip().splitlines()):
        for c, char in enumerate(row):
            if char == 'S':
                start = (c, r)

            if char == '^':
                splitters.add((c, r))

    max_depth = r

    S = {start}

    C = 0
    while S:
        n_S = set()
        for c, r in S:
            next_pos = (c, r + 1)
            if next_pos in splitters:
                C += 1
                n_S.add((c - 1, r + 1))
                n_S.add((c + 1, r + 1))
            elif r + 1 <= max_depth:
                n_S.add(next_pos)
        S = n_S

    print(C)
    AOC.submit_answer(C)

if __name__ == "__main__":
    solve()
