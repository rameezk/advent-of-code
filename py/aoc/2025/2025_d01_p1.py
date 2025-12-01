from aoc.helper import AOC


@AOC.puzzle(2025, 1, 1)
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
# L82"""

    num = 50
    zero_count = 0
    for line in data:
        rotation = line[0]
        by = int(line[1:])

        if rotation == "R":
            num += by
        else:
            num -= by

        num = num % 100

        print(rotation, by, num)

        if num == 0:
            zero_count += 1

    print(zero_count)
    AOC.submit_answer(zero_count)


if __name__ == "__main__":
    solve()
