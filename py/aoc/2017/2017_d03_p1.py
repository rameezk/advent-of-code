from aoc.helper import AOC

@AOC.puzzle(2017, 3, 1)
def solve():
    data = AOC.get_data().strip()

    n = int(data)

    if n == 1:
        AOC.submit_answer(0)
        return

    layer = 0
    max_in_layer = 1
    while max_in_layer < n:
        layer += 1
        max_in_layer = (2 * layer + 1) ** 2

    side_length = 2 * layer + 1
    min_in_layer = (2 * (layer - 1) + 1) ** 2 + 1

    pos_in_layer = n - min_in_layer
    side_pos = pos_in_layer % (side_length - 1)

    offset_from_middle = abs(side_pos - (layer - 1))

    answer = layer + offset_from_middle

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
