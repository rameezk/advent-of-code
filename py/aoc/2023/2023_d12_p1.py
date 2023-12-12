from aoc.helper import download_input, submit_answer

from itertools import product

import re


def get_positions_of_unknowns(record: str) -> list[int]:
    positions = []
    for i in range(len(record)):
        if record[i] == "?":
            positions.append(i)
    return positions


def generate_combinations(unknowns: list[int]) -> list:
    s = [".", "#"]
    p = product(s, repeat=len(unknowns))
    a = [list(zip(unknowns, c)) for c in p]
    return a


def replace_record(record: str, combination: list[tuple[int, str]]) -> str:
    for idx, s in combination:
        record = record[:idx] + s + record[idx + 1 :]
    return record


def generate_regex_pattern(check: list[int]) -> re.Pattern:
    # ^\.*(#{1})\.+(#{1})\.+(#{3})\.*$
    g = [f"(#{'{' + str(num) + '}'})" for num in check]
    inner = r"\.+".join(g)
    r = r"^\.*" + inner + r"\.*$"
    return re.compile(r)


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
    #     """.strip().splitlines()

    records = []
    for line in raw_records:
        record, check = line.split()
        check = list(map(int, check.split(",")))
        records.append((record, check))

    C = 0
    L = len(records)
    for record_number, (record, check) in enumerate(records, start=1):
        print(f"Checking record {record_number} of {L}")
        r_pattern = generate_regex_pattern(check)
        unknowns = get_positions_of_unknowns(record)
        combinations = generate_combinations(unknowns)
        for combination in combinations:
            r = replace_record(record, combination)
            if re.match(r_pattern, r):
                C += 1
        # _ = input("Continue?")

    print(C)
    # submit_answer(2023, 12, 1, C)
