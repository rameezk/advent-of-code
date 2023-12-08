from aoc.helper import download_input, submit_answer

from aoc.util import sliding_window, batch


def contains_pair(s: str) -> bool:
    for i in range(len(s)):
        n = i + 1
        c = s[i : n + 1]
        if len(c) < 2:
            break
        c1 = s[:i]
        c2 = s[n + 1 :]
        x = c1.count(c) + c2.count(c)
        if x >= 1:
            return True

    return False


def is_sandwiched(s: str) -> bool:
    ws = list(sliding_window(s, 3))

    for n1, n2, n3 in ws:
        if n1 == n3:
            return True

    return False


def is_nice(s: str) -> bool:
    return contains_pair(s) and is_sandwiched(s)


if __name__ == "__main__":
    with open("./2015_d05.txt") as f:
        data = f.read().strip().splitlines()

    # data = [
    #     # "aaa",
    #     "qjhvhtzxzqqjkmpb",
    #     "xxyxx",
    #     "uurcxstgmygtbstg",
    #     "ieodomkazucvgmuy",
    # ]

    t = 0
    for line in data:
        if is_nice(line):
            t += 1

    print(t)
    # submit_answer(2015, 5, 2, t)
