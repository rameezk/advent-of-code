from aoc.helper import download_input, submit_answer
import itertools

if __name__ == "__main__":
    with open("./2017_d02.txt") as f:
        data = f.read()

    checksum = 0
    for line in data.strip().splitlines():
        row = [int(n) for n in line.strip().split()]
        for combination in itertools.permutations(row, 2):
            n1, n2 = sorted(combination)
            quotient, remainder = divmod(n2, n1)
            if remainder == 0:
                checksum += quotient
                break

    print(checksum)
    # submit_answer(2017, 2, 2, checksum)
