import math
import re

from aoc.helper import AOC


@AOC.puzzle(2025, 10, 1)
def solve():
    data = AOC.get_data()

#     data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    total = 0
    for line in data.strip().splitlines():
        lights = re.search(r"\[([.#]+)]", line).group(1)
        buttons = re.findall(r"\(([0-9,]+)\)", line)
        target = get_binary_int(lights)
        button_masks = [get_bitmask(b) for b in buttons]
        presses = min_presses(target, button_masks)
        total += presses

    print(total)
    AOC.submit_answer(total)

def get_binary_int(s):
    m = 0
    for i, c in enumerate(s):
        if c == "#":
            m |= (1 << i)
    return m

def get_bitmask(s):
    m = 0
    for bit in s.split(","):
        m |= (1 << int(bit))
    return m

def min_presses(target, buttons):
    n = len(buttons)
    best = math.inf
    for mask in range(1 << n):
        xor = 0
        count = 0
        for i in range(n):
            if mask & (1 << i):
                xor ^= buttons[i]
                count += 1
        if xor == target:
            best = min(best, count)
    return best

if __name__ == "__main__":
    solve()
