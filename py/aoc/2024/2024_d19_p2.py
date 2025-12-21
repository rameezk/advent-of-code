from aoc.helper import AOC


@AOC.puzzle(2024, 19, 2)
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

    def count_ways(design, memo=None):
        if memo is None:
            memo = {}

        if design in memo:
            return memo[design]

        if design == "":
            return 1

        total = 0
        for pattern in patterns:
            if design.startswith(pattern):
                total += count_ways(design[len(pattern):], memo)

        memo[design] = total
        return total

    total_ways = 0
    for design in designs:
        ways = count_ways(design)
        total_ways += ways

    print(total_ways)
    AOC.submit_answer(total_ways)


if __name__ == "__main__":
    solve()
