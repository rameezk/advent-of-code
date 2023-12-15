from aoc.helper import download_input, submit_answer
import re
from collections import defaultdict


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

    boxes = defaultdict(lambda: [])
    for step in seq:
        label = re.split(r"[=\-]", step)[0]
        box = calculate_hash(label)
        if "=" in step:
            focal_length = int(re.findall(r"\d+", step)[0])
            for i in range(len(boxes[box])):
                lense_label, _ = boxes[box][i]
                if lense_label == label:
                    boxes[box][i] = (label, focal_length)
                    break
            else:
                boxes[box].append((label, focal_length))
        if "-" in step:
            boxes[box] = [b for b in boxes[box] if b[0] != label]

    power = {}
    for box_number, lenses in boxes.items():
        for lense_position, (lense_label, lense_focal_length) in enumerate(
            lenses, start=1
        ):
            p = (1 + box_number) * lense_position * lense_focal_length
            power[lense_label] = p

    S = sum(power.values())
    print(S)

    # submit_answer(2023, 15, 2, S)


if __name__ == "__main__":
    run()
