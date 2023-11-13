from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2015, 2)

    with open("./2015_d02.txt") as f:
        data = f.read().strip().splitlines()

    # data = "1x1x10"

    tot = 0
    for line in data:
        ld = [int(n) for n in line.strip().split("x")]
        l, w, h = ld
        t = (2 * l * w) + (2 * w * h) + (2 * h * l)
        e1, e2 = sorted(ld)[:2]
        r = t + (e1 * e2)
        tot += r

    print(tot)
    submit_answer(2015, 2, 1, tot)
