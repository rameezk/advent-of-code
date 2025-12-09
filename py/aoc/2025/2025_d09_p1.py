from aoc.helper import AOC


@AOC.puzzle(2025, 9, 1)
def solve():
    data = AOC.get_data()

#     data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

    red_tiles = []
    for line in data.strip().splitlines():
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))

    areas = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            c1 = red_tiles[i]
            c2 = red_tiles[j]
            a = area(c1, c2)
            areas.append(a)

    M = max(areas)
    print(M)
    AOC.submit_answer(M)

def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


if __name__ == "__main__":
    solve()
