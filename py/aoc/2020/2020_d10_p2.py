from aoc.helper import AOC
from functools import lru_cache

@AOC.puzzle(2020, 10, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".splitlines()

    adapters = [int(x) for x in data]
    adapters.sort()

    adapters = [0] + adapters + [adapters[-1] + 3]

    @lru_cache(maxsize=None)
    def count_paths(index):
        if index == len(adapters) - 1:
            return 1

        total = 0
        for next_index in range(index + 1, len(adapters)):
            if adapters[next_index] - adapters[index] <= 3:
                total += count_paths(next_index)
            else:
                break

        return total

    answer = count_paths(0)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
