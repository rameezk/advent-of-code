from aoc.helper import AOC


@AOC.puzzle(2019, 16, 1)
def solve():
    data = AOC.get_data().strip()

    signal = [int(c) for c in data]
    base_pattern = [0, 1, 0, -1]

    for phase in range(100):
        new_signal = []
        for i in range(len(signal)):
            pattern = []
            for p in base_pattern:
                pattern.extend([p] * (i + 1))

            value = 0
            for j, digit in enumerate(signal):
                pattern_index = (j + 1) % len(pattern)
                value += digit * pattern[pattern_index]

            new_signal.append(abs(value) % 10)
        signal = new_signal

    answer = ''.join(str(d) for d in signal[:8])
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
