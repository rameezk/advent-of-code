from aoc.helper import AOC
import re
from collections import defaultdict

@AOC.puzzle(2017, 20, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""

    particles = []
    for line in data.split('\n'):
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        p = numbers[0:3]
        v = numbers[3:6]
        a = numbers[6:9]
        particles.append([p, v, a])

    no_collision_ticks = 0
    while no_collision_ticks < 100:
        for i in range(len(particles)):
            p, v, a = particles[i]
            for j in range(3):
                v[j] += a[j]
                p[j] += v[j]

        positions = defaultdict(list)
        for i, (p, v, a) in enumerate(particles):
            positions[tuple(p)].append(i)

        to_remove = set()
        for pos, indices in positions.items():
            if len(indices) > 1:
                to_remove.update(indices)

        if to_remove:
            particles = [p for i, p in enumerate(particles) if i not in to_remove]
            no_collision_ticks = 0
        else:
            no_collision_ticks += 1

    answer = len(particles)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
