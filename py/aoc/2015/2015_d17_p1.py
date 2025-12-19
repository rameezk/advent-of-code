from aoc.helper import AOC
from itertools import combinations


@AOC.puzzle(2015, 17, 1)
def solve():
    #sample_data = """20
#15
#10
#5
#5"""

    data = AOC.get_data().strip()
    #data = sample_data

    containers = list(map(int, data.split('\n')))
    target = 150

    count = 0
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                count += 1

    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
