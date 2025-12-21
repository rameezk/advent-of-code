from aoc.helper import AOC


@AOC.puzzle(2022, 10, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    x = 1
    cycle = 0
    crt = []

    for line in data:
        parts = line.split()
        instruction = parts[0]

        if instruction == "noop":
            crt_pos = cycle % 40
            if abs(x - crt_pos) <= 1:
                crt.append('#')
            else:
                crt.append('.')
            cycle += 1
        else:
            value = int(parts[1])
            for _ in range(2):
                crt_pos = cycle % 40
                if abs(x - crt_pos) <= 1:
                    crt.append('#')
                else:
                    crt.append('.')
                cycle += 1
            x += value

    result = []
    for i in range(6):
        line = ''.join(crt[i*40:(i+1)*40])
        print(line)
        result.append(line)

    AOC.submit_answer('\n'.join(result))


if __name__ == "__main__":
    solve()
