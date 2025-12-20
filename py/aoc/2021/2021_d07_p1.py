from aoc.helper import AOC

@AOC.puzzle(2021, 7, 1)
def solve():
    data = AOC.get_data().strip()

    positions = list(map(int, data.split(',')))

    positions.sort()

    median = positions[len(positions) // 2]

    answer = sum(abs(pos - median) for pos in positions)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
