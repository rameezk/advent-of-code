from aoc.helper import AOC

@AOC.puzzle(2021, 1, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    measurements = [int(x) for x in data]

    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            count += 1

    answer = count

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
