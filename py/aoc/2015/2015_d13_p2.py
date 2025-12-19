from aoc.helper import AOC
from itertools import permutations
import re


@AOC.puzzle(2015, 13, 2)
def solve():
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

    me = "Me"
    for person in list(people):
        happiness[(me, person)] = 0
        happiness[(person, me)] = 0
    people.add(me)

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
