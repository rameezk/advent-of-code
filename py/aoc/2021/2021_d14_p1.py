from aoc.helper import AOC
from collections import Counter

@AOC.puzzle(2021, 14, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

    lines = data.split('\n')
    template = lines[0]

    rules = {}
    for line in lines[2:]:
        pair, insert = line.split(' -> ')
        rules[pair] = insert

    polymer = template
    for step in range(10):
        new_polymer = []
        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            new_polymer.append(polymer[i])
            if pair in rules:
                new_polymer.append(rules[pair])
        new_polymer.append(polymer[-1])
        polymer = ''.join(new_polymer)

    counts = Counter(polymer)
    most_common = counts.most_common(1)[0][1]
    least_common = counts.most_common()[-1][1]
    answer = most_common - least_common

    print(f"Part 1: {answer}")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
