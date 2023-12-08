from aoc.helper import submit_answer

if __name__ == "__main__":
    # download_input(year=2017, day=1)

    with open("./2017_d01.txt") as f:
        data = f.read()

    lst = [int(n) for n in data.strip()]

    r = 0
    s = len(lst)
    h = s // 2

    for current in range(s):
        next_ = (current + h) % s
        if lst[current] == lst[next_]:
            r += lst[current]

    print(r)
    submit_answer(2017, 1, 2, r)
