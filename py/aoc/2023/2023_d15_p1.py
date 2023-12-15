from aoc.helper import download_input, submit_answer


def calculate_hash(s: str) -> int:
    c = 0
    for ch in s:
        c += +ord(ch)
        c *= 17
        _, c = divmod(c, 256)
    return c


def run():
    download_input(2023, 15)

    seq = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """.strip().split(
        ","
    )

    with open("2023_d15.txt") as f:
        seq = f.read().strip().split(",")

    S = 0
    for step in seq:
        h = calculate_hash(step)
        S += h

    print(S)
    # submit_answer(2023, 15, 1, S)


if __name__ == "__main__":
    run()
