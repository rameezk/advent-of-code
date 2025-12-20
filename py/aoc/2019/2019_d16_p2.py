from aoc.helper import AOC


@AOC.puzzle(2019, 16, 2)
def solve():
    data = AOC.get_data().strip()

    offset = int(data[:7])
    signal = [int(c) for c in data] * 10000

    signal = signal[offset:]

    for phase in range(100):
        for i in range(len(signal) - 2, -1, -1):
            signal[i] = (signal[i] + signal[i + 1]) % 10

    answer = ''.join(str(d) for d in signal[:8])
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
