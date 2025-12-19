from aoc.helper import AOC


@AOC.puzzle(2015, 8, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    # data = r"""
    # ""
    # "abc"
    # "aaa\"aaa"
    # "\x27"
    # """.strip().splitlines()

    total_original = 0
    total_encoded = 0

    for line in data:
        original_length = len(line)
        total_original += original_length

        encoded = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        encoded_length = len(encoded)
        total_encoded += encoded_length

        print(f"{line} -> original: {original_length}, encoded: {encoded_length}, encoded_str: {encoded}")

    difference = total_encoded - total_original
    print(f"\nTotal original: {total_original}, Total encoded: {total_encoded}, Difference: {difference}")

    AOC.submit_answer(difference)


if __name__ == "__main__":
    solve()
