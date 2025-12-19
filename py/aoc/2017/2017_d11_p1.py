from aoc.helper import AOC

@AOC.puzzle(2017, 11, 1)
def solve():
    data = AOC.get_data().strip()

    x, y, z = 0, 0, 0

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

    answer = (abs(x) + abs(y) + abs(z)) // 2
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
