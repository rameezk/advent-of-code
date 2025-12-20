from aoc.helper import AOC

@AOC.puzzle(2021, 1, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    measurements = [int(x) for x in data]

    window_sums = []
    for i in range(len(measurements) - 2):
        window_sum = measurements[i] + measurements[i+1] + measurements[i+2]
        window_sums.append(window_sum)

    count = 0
    for i in range(1, len(window_sums)):
        if window_sums[i] > window_sums[i-1]:
            count += 1

    answer = count

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
