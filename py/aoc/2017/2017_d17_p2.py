from aoc.helper import AOC

@AOC.puzzle(2017, 17, 2)
def solve():
    data = AOC.get_data().strip()

    steps = int(data)

    pos = 0
    value_after_zero = 0

    for i in range(1, 50000001):
        pos = (pos + steps) % i + 1
        if pos == 1:
            value_after_zero = i

    answer = value_after_zero

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
