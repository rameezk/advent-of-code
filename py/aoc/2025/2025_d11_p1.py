from aoc.helper import AOC


@AOC.puzzle(2025, 11, 1)
def solve():
    data = AOC.get_data()

#     data = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""

    device_outputs = {}
    for line in data.strip().splitlines():
        device, outputs = line.split(":")
        outputs = outputs.strip().split()
        device_outputs[device] = outputs

    total = count_paths("you", device_outputs)
    print(total)
    AOC.submit_answer(total)

def count_paths(node, device_outputs):
    if node == "out":
        return 1
    if node not in device_outputs:
        return 0
    return sum(count_paths(child, device_outputs) for child in device_outputs[node])

if __name__ == "__main__":
    solve()
