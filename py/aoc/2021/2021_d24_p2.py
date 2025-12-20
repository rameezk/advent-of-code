from aoc.helper import AOC

@AOC.puzzle(2021, 24, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    blocks = []
    for i in range(0, len(data), 18):
        block = data[i:i+18]
        div_z = int(block[4].split()[-1])
        add_x = int(block[5].split()[-1])
        add_y = int(block[15].split()[-1])
        blocks.append((div_z, add_x, add_y))

    stack = []
    constraints = []

    for i, (div_z, add_x, add_y) in enumerate(blocks):
        if div_z == 1:
            stack.append((i, add_y))
        else:
            j, prev_add_y = stack.pop()
            constraints.append((j, i, prev_add_y + add_x))

    digits = [0] * 14

    for i, j, offset in constraints:
        for d1 in range(1, 10):
            d2 = d1 + offset
            if 1 <= d2 <= 9:
                digits[i] = d1
                digits[j] = d2
                break

    answer = ''.join(map(str, digits))
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
