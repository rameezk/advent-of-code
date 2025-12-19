from aoc.helper import AOC

@AOC.puzzle(2017, 10, 1)
def solve():
    data = AOC.get_data().strip()

    lengths = [int(x) for x in data.split(',')]

    list_size = 256
    numbers = list(range(list_size))
    current_pos = 0
    skip_size = 0

    for length in lengths:
        indices = [(current_pos + i) % list_size for i in range(length)]
        values = [numbers[idx] for idx in indices]
        values.reverse()
        for i, idx in enumerate(indices):
            numbers[idx] = values[i]

        current_pos = (current_pos + length + skip_size) % list_size
        skip_size += 1

    answer = numbers[0] * numbers[1]
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
