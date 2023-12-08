from aoc.helper import download_input, submit_answer

from collections import defaultdict
import re


if __name__ == "__main__":
    # download_input(2015, 6)

    with open("./2015_d06.txt") as f:
        instructions = f.read().strip().splitlines()

    #     instructions = """
    # turn on 0,0 through 999,999
    # toggle 0,0 through 999,0
    # turn off 499,499 through 500,500
    #            """
    #     instructions = instructions.strip().splitlines()

    lights = defaultdict(lambda: 0)

    for instruction in instructions:
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", instruction))

        if "turn on" in instruction:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[f"{x},{y}"] = 1

        elif "turn off" in instruction:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[f"{x},{y}"] = 0
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[f"{x},{y}"] = 0 if lights[f"{x},{y}"] == 1 else 1

    lit_count = sum(lights.values())
    print(lit_count)

    assert lit_count == 377891

    # submit_answer(2015, 6, 1, lit_count)
