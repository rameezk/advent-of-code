from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    with open("./2017_d02.txt") as f:
        data = f.read()

    checksum = 0
    for line in data.strip().splitlines():
        min_, *_, max_ = sorted([int(n) for n in line.strip().split()])
        checksum += max_ - min_

    print(checksum)
    # submit_answer(2017, 2, 1, checksum)
