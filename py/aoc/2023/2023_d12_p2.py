from aoc.helper import download_input, submit_answer

from itertools import product

from functools import cache


import re


def get_positions_of_unknowns(record: str) -> list[int]:
    positions = []
    for i in range(len(record)):
        if record[i] == "?":
            positions.append(i)
    return positions


def generate_combinations(unknowns: list[int]) -> list:
    s = [".", "#"]
    for c in product(s, repeat=len(unknowns)):
        yield list(zip(unknowns, c))


def replace_record(record: str, combination: list[tuple[int, str]]) -> str:
    record_list = list(record)
    for idx, s in combination:
        record_list[idx] = s
    return "".join(record_list)


def expand_record(record: str, multiplier: int) -> str:
    a = [record]
    nr = "?".join(a * multiplier)
    return nr


def expand_check(check: list[int], multipler: int) -> list[int]:
    return check * multipler


def generate_regex_pattern(check: list[int]) -> re.Pattern:
    # ^\.*(#{1})\.+(#{1})\.+(#{3})\.*$
    g = [f"(#{'{' + str(num) + '}'})" for num in check]
    inner = r"\.+".join(g)
    r = r"^\.*" + inner + r"\.*$"
    return re.compile(r)


# Not my solution (I gave up)
@cache
def count_possibilities(record: str, check: tuple) -> int:
    if record == "":
        return 1 if not len(check) else 0

    if not len(check):
        return 0 if "#" in record else 1

    c = 0

    if record[0] in ".?":
        c += count_possibilities(record[1:], check)

    if record[0] in "#?":
        if (
            check[0] <= len(record)
            and "." not in record[: check[0]]
            and (check[0] == len(record) or record[check[0]] != "#")
        ):
            c += count_possibilities(record[check[0] + 1 :], check[1:])

    return c


if __name__ == "__main__":
    download_input(2023, 12)

    with open("./2023_d12.txt") as f:
        raw_records = f.read().strip().splitlines()

    #     raw_records = """
    # ???.### 1,1,3
    # .??..??...?##. 1,1,3
    # ?#?#?#?#?#?#?#? 1,3,1,6
    # ????.#...#... 4,1,1
    # ????.######..#####. 1,6,5
    # ?###???????? 3,2,1
    #         """.strip().splitlines()

    records = []
    for line in raw_records:
        record, check = line.split()
        check = list(map(int, check.split(",")))
        expanded_record = expand_record(record, 5)
        expanded_check = expand_check(check, 5)
        records.append((expanded_record, expanded_check))

    C = []
    L = len(records)
    for record_number, (record, check) in enumerate(records, start=1):
        print(f"Checking record {record_number} of {L}")
        c = count_possibilities(record, tuple(check))
        C.append(c)

    print(C)
    T = sum(C)
    print(T)
    assert T == 1493340882140
    # submit_answer(2023, 12, 2, T)
