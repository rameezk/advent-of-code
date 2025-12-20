from aoc.helper import AOC

@AOC.puzzle(2021, 7, 2)
def solve():
    data = AOC.get_data().strip()

    positions = list(map(int, data.split(',')))

    def fuel_cost(positions, target):
        total = 0
        for pos in positions:
            n = abs(pos - target)
            total += n * (n + 1) // 2
        return total

    min_pos = min(positions)
    max_pos = max(positions)

    answer = min(fuel_cost(positions, target) for target in range(min_pos, max_pos + 1))

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
