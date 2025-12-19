from aoc.helper import AOC

@AOC.puzzle(2017, 5, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """0
# 3
# 0
# 1
# -3"""

    jumps = list(map(int, data.split('\n')))

    position = 0
    steps = 0

    while 0 <= position < len(jumps):
        offset = jumps[position]
        if offset >= 3:
            jumps[position] -= 1
        else:
            jumps[position] += 1
        position += offset
        steps += 1

    answer = steps
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
