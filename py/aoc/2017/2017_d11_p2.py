from aoc.helper import AOC

@AOC.puzzle(2017, 11, 2)
def solve():
    data = AOC.get_data().strip()

    x, y, z = 0, 0, 0
    max_distance = 0

    for direction in data.split(','):
        if direction == 'n':
            y += 1
            z -= 1
        elif direction == 's':
            y -= 1
            z += 1
        elif direction == 'ne':
            x += 1
            z -= 1
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'se':
            x += 1
            y -= 1
        elif direction == 'sw':
            x -= 1
            z += 1

        distance = (abs(x) + abs(y) + abs(z)) // 2
        max_distance = max(max_distance, distance)

    answer = max_distance
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
