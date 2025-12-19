from aoc.helper import AOC

@AOC.puzzle(2017, 13, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """0: 3
# 1: 2
# 4: 4
# 6: 4"""

    layers = {}
    for line in data.split('\n'):
        depth, range_val = line.split(': ')
        layers[int(depth)] = int(range_val)

    severity = 0
    for depth, range_val in layers.items():
        if depth % (2 * (range_val - 1)) == 0:
            severity += depth * range_val

    AOC.submit_answer(severity)

if __name__ == "__main__":
    solve()
