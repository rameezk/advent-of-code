from aoc.helper import AOC


@AOC.puzzle(2022, 2, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """A Y
# B X
# C Z"""

    total_score = 0
    for line in data.strip().splitlines():
        opponent, outcome = line.split()

        if outcome == 'X':
            shape_score = {'A': 3, 'B': 1, 'C': 2}[opponent]
            outcome_score = 0
        elif outcome == 'Y':
            shape_score = {'A': 1, 'B': 2, 'C': 3}[opponent]
            outcome_score = 3
        else:
            shape_score = {'A': 2, 'B': 3, 'C': 1}[opponent]
            outcome_score = 6

        total_score += shape_score + outcome_score

    print(total_score)
    AOC.submit_answer(total_score)


if __name__ == "__main__":
    solve()
