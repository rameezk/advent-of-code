import math

from aoc.helper import AOC


@AOC.puzzle(2025, 8, 1)
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

    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

    take = 1000
    i = 0
    circuits = []
    for k, v in sorted_distances.items():
        n1, n2 = k

        c1 = c2 = None
        for c in circuits:
            if n1 in c:
                c1 = c
            if n2 in c:
                c2 = c

        if not c1 and not c2:
            circuits.append({n1, n2})
        elif not c1:
            c2.add(n1)
        elif not c2:
            c1.add(n2)
        elif c1 is not c2:
            c1.update(c2)
            circuits.remove(c2)

        i += 1
        if i >= take:
            break

    len_circuits = map(len, circuits)
    len_circuits_sorted = sorted(len_circuits, reverse=True)
    S = math.prod(len_circuits_sorted[:3])
    print(S)
    AOC.submit_answer(S)

def distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


if __name__ == "__main__":
    solve()
