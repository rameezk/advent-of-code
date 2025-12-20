from aoc.helper import AOC


@AOC.puzzle(2018, 25, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """ 0,0,0,0
#  3,0,0,0
#  0,3,0,0
#  0,0,3,0
#  0,0,0,3
#  0,0,0,6
#  9,0,0,0
# 12,0,0,0""".strip().splitlines()

#     data = """-1,2,2,0
# 0,0,2,-2
# 0,0,0,-2
# -1,2,0,0
# -2,-2,-2,2
# 3,0,2,-1
# -1,3,2,2
# -1,0,-1,0
# 0,2,1,-2
# 3,0,0,0""".strip().splitlines()

#     data = """1,-1,0,1
# 2,0,-1,0
# 3,2,-1,0
# 0,0,3,1
# 0,0,-1,-1
# 2,3,-2,0
# -2,2,0,0
# 2,-2,0,-1
# 1,-1,0,-1
# 3,2,0,2""".strip().splitlines()

#     data = """1,-1,-1,-2
# -2,-2,0,1
# 0,2,1,3
# -2,3,-2,1
# 0,2,3,-2
# -1,-1,1,-2
# 0,-2,-1,0
# -2,2,3,-1
# 1,2,2,0
# -1,-2,0,-2""".strip().splitlines()

    points = []
    for line in data:
        coords = tuple(map(int, line.strip().split(',')))
        points.append(coords)

    def manhattan_distance(p1, p2):
        return sum(abs(a - b) for a, b in zip(p1, p2))

    n = len(points)
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for i in range(n):
        for j in range(i + 1, n):
            if manhattan_distance(points[i], points[j]) <= 3:
                union(i, j)

    constellations = len(set(find(i) for i in range(n)))

    print(constellations)
    AOC.submit_answer(constellations)


if __name__ == "__main__":
    solve()
