from aoc.helper import AOC

@AOC.puzzle(2017, 13, 2)
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

    delay = 0
    while True:
        caught = False
        for depth, range_val in layers.items():
            if (delay + depth) % (2 * (range_val - 1)) == 0:
                caught = True
                break
        if not caught:
            AOC.submit_answer(delay)
            break
        delay += 1

if __name__ == "__main__":
    solve()
