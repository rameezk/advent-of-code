from aoc.helper import AOC


@AOC.puzzle(2024, 19, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """r, wr, b, g, bwu, rb, gb, br
#
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

    parts = data.split('\n\n')
    patterns = [p.strip() for p in parts[0].split(',')]
    designs = parts[1].strip().splitlines()

    def can_make(design, memo=None):
        if memo is None:
            memo = {}

        if design in memo:
            return memo[design]

        if design == "":
            return True

        for pattern in patterns:
            if design.startswith(pattern):
                if can_make(design[len(pattern):], memo):
                    memo[design] = True
                    return True

        memo[design] = False
        return False

    possible_count = 0
    for design in designs:
        if can_make(design):
            possible_count += 1

    print(possible_count)
    AOC.submit_answer(possible_count)


if __name__ == "__main__":
    solve()
