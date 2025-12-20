from aoc.helper import AOC

@AOC.puzzle(2020, 2, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    valid_count = 0

    for line in data:
        policy, password = line.split(": ")
        range_part, letter = policy.split(" ")
        pos1, pos2 = map(int, range_part.split("-"))

        char_at_pos1 = password[pos1 - 1] if pos1 <= len(password) else None
        char_at_pos2 = password[pos2 - 1] if pos2 <= len(password) else None

        if (char_at_pos1 == letter) != (char_at_pos2 == letter):
            valid_count += 1

    answer = valid_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
