from aoc.helper import AOC

@AOC.puzzle(2020, 6, 2)
def solve():
    data = AOC.get_data().strip()

    groups = data.split('\n\n')

    total = 0
    for group in groups:
        people = group.split('\n')
        common = set(people[0])
        for person in people[1:]:
            common = common.intersection(set(person))
        total += len(common)

    AOC.submit_answer(total)

if __name__ == "__main__":
    solve()
