from aoc.helper import AOC
import re
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result


@AOC.puzzle(2019, 12, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    initial_positions = []
    for line in data:
        x, y, z = map(int, re.findall(r'-?\d+', line))
        initial_positions.append([x, y, z])

    cycles = []

    for axis in range(3):
        positions = [moon[axis] for moon in initial_positions]
        velocities = [0] * len(positions)
        initial_state = (tuple(positions), tuple(velocities))

        steps = 0
        while True:
            for i in range(len(positions)):
                for j in range(len(positions)):
                    if i != j:
                        if positions[i] < positions[j]:
                            velocities[i] += 1
                        elif positions[i] > positions[j]:
                            velocities[i] -= 1

            for i in range(len(positions)):
                positions[i] += velocities[i]

            steps += 1

            current_state = (tuple(positions), tuple(velocities))
            if current_state == initial_state:
                cycles.append(steps)
                break

    answer = lcm_multiple(cycles)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
