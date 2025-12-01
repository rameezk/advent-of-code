from aoc.helper import AOC


@AOC.puzzle(2025, 1, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".strip().splitlines()
#
    num = 50
    zero_count = 0

    for line in data:
        rotation = line[0]
        by = int(line[1:])

        if rotation == "R":
            rotations = (num + by) // 100
            num = (num + by) % 100
        else:
            if num == 0:
                rotations = by // 100
            elif by >= num:
                rotations = (by - num) // 100 + 1
            else:
                rotations = 0
            num = (num - by) % 100

        zero_count += rotations

    print(zero_count)
    AOC.submit_answer(zero_count)


if __name__ == "__main__":
    solve()
