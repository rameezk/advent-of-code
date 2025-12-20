from aoc.helper import AOC


@AOC.puzzle(2018, 8, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

    numbers = list(map(int, data.split()))

    def parse_node(idx):
        num_children = numbers[idx]
        num_metadata = numbers[idx + 1]
        idx += 2

        metadata_sum = 0

        for _ in range(num_children):
            idx, child_sum = parse_node(idx)
            metadata_sum += child_sum

        for _ in range(num_metadata):
            metadata_sum += numbers[idx]
            idx += 1

        return idx, metadata_sum

    _, total = parse_node(0)
    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
