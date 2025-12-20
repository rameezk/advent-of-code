from aoc.helper import AOC
import re


@AOC.puzzle(2019, 12, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    moons = []
    for line in data:
        x, y, z = map(int, re.findall(r'-?\d+', line))
        moons.append({'pos': [x, y, z], 'vel': [0, 0, 0]})

    for _ in range(1000):
        for i in range(len(moons)):
            for j in range(len(moons)):
                if i != j:
                    for axis in range(3):
                        if moons[i]['pos'][axis] < moons[j]['pos'][axis]:
                            moons[i]['vel'][axis] += 1
                        elif moons[i]['pos'][axis] > moons[j]['pos'][axis]:
                            moons[i]['vel'][axis] -= 1

        for moon in moons:
            for axis in range(3):
                moon['pos'][axis] += moon['vel'][axis]

    total_energy = 0
    for moon in moons:
        pot = sum(abs(p) for p in moon['pos'])
        kin = sum(abs(v) for v in moon['vel'])
        total_energy += pot * kin

    answer = total_energy
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
