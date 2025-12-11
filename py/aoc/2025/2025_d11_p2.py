from functools import lru_cache
from aoc.helper import AOC


@AOC.puzzle(2025, 11, 2)
def solve():
    data = AOC.get_data()

#     data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""

    device_outputs = []
    for line in data.strip().splitlines():
        device, output = line.split(":")
        device_outputs.append((device, tuple(output.strip().split())))
    device_outputs = tuple(device_outputs)

    total = count_paths("svr", device_outputs, False, False)
    print(total)
    AOC.submit_answer(total)


@lru_cache(maxsize=None)
def count_paths(node, device_outputs, has_dac, has_fft):
    device_outputs_lookup = dict(device_outputs)

    if node == "dac":
        has_dac = True
    if node == "fft":
        has_fft = True

    if node == "out":
        return 1 if (has_dac and has_fft) else 0
    if node not in device_outputs_lookup:
        return 0
    return sum(
        count_paths(child, device_outputs, has_dac, has_fft)
        for child in device_outputs_lookup[node]
    )


if __name__ == "__main__":
    solve()
