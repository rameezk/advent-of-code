from aoc.helper import AOC

@AOC.puzzle(2021, 22, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """on x=-20..26,y=-36..17,z=-47..7
# on x=-20..33,y=-21..23,z=-26..28
# on x=-22..28,y=-29..23,z=-38..16
# on x=-46..7,y=-6..46,z=-50..-1
# on x=-49..1,y=-3..46,z=-24..28
# on x=2..47,y=-22..22,z=-23..27
# on x=-27..23,y=-28..26,z=-21..29
# on x=-39..5,y=-6..47,z=-3..44
# on x=-30..21,y=-8..43,z=-13..34
# on x=-22..26,y=-27..20,z=-29..19
# off x=-48..-32,y=26..41,z=-47..-37
# on x=-12..35,y=6..50,z=-50..-2
# off x=-48..-32,y=-32..-16,z=-15..-5
# on x=-18..26,y=-33..15,z=-7..46
# off x=-40..-22,y=-38..-28,z=23..41
# on x=-16..35,y=-41..10,z=-47..6
# off x=-32..-23,y=11..30,z=-14..3
# on x=-49..-5,y=-3..45,z=-29..18
# off x=18..30,y=-20..-8,z=-3..13
# on x=-41..9,y=-7..43,z=-33..15
# on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
# on x=967..23432,y=45373..81175,z=27513..53682""".splitlines()

    cubes = set()

    for line in data:
        parts = line.split()
        state = parts[0]
        coords = parts[1]

        x_part, y_part, z_part = coords.split(',')
        x_min, x_max = map(int, x_part[2:].split('..'))
        y_min, y_max = map(int, y_part[2:].split('..'))
        z_min, z_max = map(int, z_part[2:].split('..'))

        if x_max < -50 or x_min > 50 or y_max < -50 or y_min > 50 or z_max < -50 or z_min > 50:
            continue

        for x in range(max(-50, x_min), min(51, x_max + 1)):
            for y in range(max(-50, y_min), min(51, y_max + 1)):
                for z in range(max(-50, z_min), min(51, z_max + 1)):
                    if state == 'on':
                        cubes.add((x, y, z))
                    elif (x, y, z) in cubes:
                        cubes.remove((x, y, z))

    answer = len(cubes)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
