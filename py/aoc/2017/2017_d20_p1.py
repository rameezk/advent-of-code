from aoc.helper import AOC
import re

@AOC.puzzle(2017, 20, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
# p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""

    particles = []
    for line in data.split('\n'):
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        p = numbers[0:3]
        v = numbers[3:6]
        a = numbers[6:9]
        particles.append((p, v, a))

    def manhattan(coords):
        return sum(abs(x) for x in coords)

    min_accel = float('inf')
    min_vel = float('inf')
    min_pos = float('inf')
    result = -1

    for i, (p, v, a) in enumerate(particles):
        accel_mag = manhattan(a)
        vel_mag = manhattan(v)
        pos_mag = manhattan(p)

        if accel_mag < min_accel:
            min_accel = accel_mag
            min_vel = vel_mag
            min_pos = pos_mag
            result = i
        elif accel_mag == min_accel:
            if vel_mag < min_vel:
                min_vel = vel_mag
                min_pos = pos_mag
                result = i
            elif vel_mag == min_vel:
                if pos_mag < min_pos:
                    min_pos = pos_mag
                    result = i

    answer = result
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
