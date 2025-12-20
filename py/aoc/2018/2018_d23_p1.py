from aoc.helper import AOC


@AOC.puzzle(2018, 23, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """pos=<0,0,0>, r=4
# pos=<1,0,0>, r=1
# pos=<4,0,0>, r=3
# pos=<0,2,0>, r=1
# pos=<0,5,0>, r=3
# pos=<0,0,3>, r=1
# pos=<1,1,1>, r=1
# pos=<1,1,2>, r=1
# pos=<1,3,1>, r=1""".strip().splitlines()

    nanobots = []
    for line in data:
        parts = line.split(", ")
        pos_str = parts[0].split("=")[1]
        x, y, z = map(int, pos_str[1:-1].split(","))
        r = int(parts[1].split("=")[1])
        nanobots.append((x, y, z, r))

    strongest = max(nanobots, key=lambda n: n[3])
    sx, sy, sz, sr = strongest

    count = 0
    for x, y, z, r in nanobots:
        distance = abs(x - sx) + abs(y - sy) + abs(z - sz)
        if distance <= sr:
            count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
