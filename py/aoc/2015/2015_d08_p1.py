from aoc.helper import AOC


@AOC.puzzle(2015, 8, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    # data = r"""
    # ""
    # "abc"
    # "aaa\"aaa"
    # "\x27"
    # """.strip().splitlines()

    total_code = 0
    total_memory = 0

    for line in data:
        code_length = len(line)
        total_code += code_length

        memory_string = eval(line)
        memory_length = len(memory_string)
        total_memory += memory_length

        print(f"{line} -> code: {code_length}, memory: {memory_length}")

    difference = total_code - total_memory
    print(f"\nTotal code: {total_code}, Total memory: {total_memory}, Difference: {difference}")

    AOC.submit_answer(difference)


if __name__ == "__main__":
    solve()
