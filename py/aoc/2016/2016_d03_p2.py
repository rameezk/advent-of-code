from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2016, 3)

    with open("./2016_d03.txt") as f:
        rows = f.read().strip().splitlines()

    triangles = []
    _t = ([], [], [])
    for i in range(len(rows)):
        t1, t2, t3 = _t
        d1, d2, d3 = map(int, rows[i].split())
        t1.append(d1)
        t2.append(d2)
        t3.append(d3)
        if len(t1) == 3:
            triangles.extend([t1, t2, t3])
            _t = ([], [], [])

    valid = 0
    for triangle in triangles:
        sides = sorted(triangle)
        if sides[0] + sides[1] > sides[2]:
            valid += 1

    print(valid)
    assert valid == 1921
    # submit_answer(2016, 3, 2, valid)
