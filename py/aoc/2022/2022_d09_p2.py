from aoc.helper import AOC


@AOC.puzzle(2022, 9, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".strip().splitlines()

    rope = [[0, 0] for _ in range(10)]
    visited = {(0, 0)}

    for line in data:
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1

            for i in range(1, 10):
                dx = rope[i-1][0] - rope[i][0]
                dy = rope[i-1][1] - rope[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    if dx != 0:
                        rope[i][0] += 1 if dx > 0 else -1
                    if dy != 0:
                        rope[i][1] += 1 if dy > 0 else -1

            visited.add((rope[9][0], rope[9][1]))

    print(len(visited))
    AOC.submit_answer(len(visited))


if __name__ == "__main__":
    solve()
