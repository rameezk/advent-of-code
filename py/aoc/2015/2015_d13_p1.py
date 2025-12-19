from aoc.helper import AOC
from itertools import permutations
import re


@AOC.puzzle(2015, 13, 1)
def solve():
    # data = """Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol."""

    data = AOC.get_data().strip()

    happiness = {}
    people = set()

    for line in data.strip().split('\n'):
        match = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.', line)
        person1 = match.group(1)
        action = match.group(2)
        value = int(match.group(3))
        person2 = match.group(4)

        if action == 'lose':
            value = -value

        happiness[(person1, person2)] = value
        people.add(person1)
        people.add(person2)

    people = list(people)
    max_happiness = float('-inf')

    for perm in permutations(people):
        total = 0
        for i in range(len(perm)):
            person1 = perm[i]
            person2 = perm[(i + 1) % len(perm)]
            total += happiness[(person1, person2)]
            total += happiness[(person2, person1)]
        max_happiness = max(max_happiness, total)

    AOC.submit_answer(max_happiness)


if __name__ == "__main__":
    solve()
