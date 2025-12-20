from aoc.helper import AOC

@AOC.puzzle(2021, 2, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     sample_data = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""
#
#     data = sample_data.splitlines()

    horizontal = 0
    depth = 0

    for line in data:
        command, value = line.split()
        value = int(value)

        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

    answer = horizontal * depth

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
