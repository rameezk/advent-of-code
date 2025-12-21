from aoc.helper import AOC


@AOC.puzzle(2022, 9, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".strip().splitlines()

    head = [0, 0]
    tail = [0, 0]
    visited = {(0, 0)}

    for line in data:
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1

            dx = head[0] - tail[0]
            dy = head[1] - tail[1]

            if abs(dx) > 1 or abs(dy) > 1:
                if dx != 0:
                    tail[0] += 1 if dx > 0 else -1
                if dy != 0:
                    tail[1] += 1 if dy > 0 else -1

            visited.add((tail[0], tail[1]))

    print(len(visited))
    AOC.submit_answer(len(visited))


if __name__ == "__main__":
    solve()
