from aoc.helper import AOC

@AOC.puzzle(2017, 6, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """0 2 7 0"""

    banks = list(map(int, data.split()))
    seen = {}
    cycles = 0

    while True:
        state = tuple(banks)
        if state in seen:
            answer = cycles - seen[state]
            break
        seen[state] = cycles

        max_blocks = max(banks)
        max_idx = banks.index(max_blocks)

        banks[max_idx] = 0
        idx = (max_idx + 1) % len(banks)

        for _ in range(max_blocks):
            banks[idx] += 1
            idx = (idx + 1) % len(banks)

        cycles += 1

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
