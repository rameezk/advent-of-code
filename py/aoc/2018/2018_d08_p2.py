from aoc.helper import AOC


@AOC.puzzle(2018, 8, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

    numbers = list(map(int, data.split()))

    def parse_node(idx):
        num_children = numbers[idx]
        num_metadata = numbers[idx + 1]
        idx += 2

        child_values = []
        for _ in range(num_children):
            idx, child_value = parse_node(idx)
            child_values.append(child_value)

        metadata = []
        for _ in range(num_metadata):
            metadata.append(numbers[idx])
            idx += 1

        if num_children == 0:
            node_value = sum(metadata)
        else:
            node_value = 0
            for meta in metadata:
                if 1 <= meta <= len(child_values):
                    node_value += child_values[meta - 1]

        return idx, node_value

    _, root_value = parse_node(0)
    print(root_value)
    AOC.submit_answer(root_value)


if __name__ == "__main__":
    solve()
