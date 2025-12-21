from aoc.helper import AOC


@AOC.puzzle(2022, 2, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """A Y
# B X
# C Z"""

    total_score = 0
    for line in data.strip().splitlines():
        opponent, me = line.split()

        shape_score = {'X': 1, 'Y': 2, 'Z': 3}[me]

        outcome_score = 0
        if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
            outcome_score = 3
        elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
            outcome_score = 6
        else:
            outcome_score = 0

        total_score += shape_score + outcome_score

    print(total_score)
    AOC.submit_answer(total_score)


if __name__ == "__main__":
    solve()
