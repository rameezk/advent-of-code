from aoc.helper import AOC


@AOC.puzzle(2022, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    x = 1
    cycle = 0
    signal_strengths = []

    for line in data:
        parts = line.split()
        instruction = parts[0]

        if instruction == "noop":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strengths.append(cycle * x)
        else:
            value = int(parts[1])
            for _ in range(2):
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    signal_strengths.append(cycle * x)
            x += value

    result = sum(signal_strengths)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
