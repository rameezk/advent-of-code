from aoc.helper import AOC

@AOC.puzzle(2020, 6, 1)
def solve():
    data = AOC.get_data().strip()

    groups = data.split('\n\n')

    total = 0
    for group in groups:
        questions = set()
        for person in group.split('\n'):
            for char in person:
                questions.add(char)
        total += len(questions)

    AOC.submit_answer(total)

if __name__ == "__main__":
    solve()
