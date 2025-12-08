import math

from aoc.helper import AOC


@AOC.puzzle(2025, 8, 2)
def solve():
    data = AOC.get_data()

#     data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

    boxes = []
    for line in data.strip().splitlines():
        x, y, z = map(int, line.split(","))
        boxes.append((x, y, z))

    distances = dict()
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            c1 = boxes[i]
            c2 = boxes[j]
            d = distance(c1, c2)
            distances[(i, j)] = d

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    circuits = []
    last_pair = None
    for (n1, n2), _ in sorted_distances:
        c1 = c2 = None
        for c in circuits:
            if n1 in c:
                c1 = c
            if n2 in c:
                c2 = c

        merged = False
        if not c1 and not c2:
            circuits.append({n1, n2})
            merged = True
        elif not c1:
            c2.add(n1)
            merged = True
        elif not c2:
            c1.add(n2)
            merged = True
        elif c1 is not c2:
            c1.update(c2)
            circuits.remove(c2)
            merged = True

        if merged:
            last_pair = (n1, n2)

        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            break

    n1, n2 = last_pair
    x1, x2 = boxes[n1][0], boxes[n2][0]
    result = x1 * x2
    print(result)
    AOC.submit_answer(result)

def distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


if __name__ == "__main__":
    solve()
