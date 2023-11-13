from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2015, 2)

    with open("./2015_d02.txt") as f:
        data = f.read().strip().splitlines()

    # data = ["2x3x4", "1x1x10"]

    tot = 0
    for line in data:
        ld = [int(n) for n in line.strip().split("x")]
        l, w, h = ld

        l1, l2 = sorted(ld)[:2]

        p = (2 * l1) + (2 * l2)
        a = l * w * h
        r = p + a
        tot += r

    print(tot)
    submit_answer(2015, 2, 2, tot)
