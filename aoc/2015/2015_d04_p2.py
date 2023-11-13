from hashlib import md5

from aoc.helper import submit_answer

if __name__ == "__main__":
    data = "iwrupvqb"
    n = 1

    while True:
        h = md5(f"{data}{n}".encode()).hexdigest()
        c = h[0:6]

        if c == "000000":
            break

        n += 1

    print(n)
    submit_answer(2015, 4, 2, n)
