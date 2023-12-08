from aoc.helper import download_input, submit_answer

from itertools import combinations

if __name__ == "__main__":
    # download_input(2018, 2)

    with open("./2018_d02.txt") as f:
        data = f.read().strip().splitlines()

    # data = [
    #     "abcde",
    #     "fghij",
    #     "klmno",
    #     "pqrst",
    #     "fguij",
    #     "axcye",
    #     "wvxyz",
    # ]

    C = combinations(data, r=2)

    common_letters = None
    for c1, c2 in C:
        assert len(c1) == len(c2)
        if len(set(c1) - set(c2)) == 1:
            differ_count = 0
            differ_idx = -1
            for i in range(len(c1)):
                if differ_count > 1:
                    break
                if c1[i] != c2[i]:
                    differ_count += 1
                    differ_idx = i
            if differ_count == 1:
                common_letters = c1.replace(c1[differ_idx], "")

    print(common_letters)
    submit_answer(2018, 2, 2, common_letters)
