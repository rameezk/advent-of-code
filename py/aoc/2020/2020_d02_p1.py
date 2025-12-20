from aoc.helper import AOC

@AOC.puzzle(2020, 2, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    valid_count = 0

    for line in data:
        policy, password = line.split(": ")
        range_part, letter = policy.split(" ")
        min_count, max_count = map(int, range_part.split("-"))

        letter_count = password.count(letter)

        if min_count <= letter_count <= max_count:
            valid_count += 1

    answer = valid_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
