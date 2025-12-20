from aoc.helper import AOC
from collections import Counter

@AOC.puzzle(2021, 14, 2)
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

    pair_counts = Counter()
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pair_counts[pair] += 1

    for step in range(40):
        new_pair_counts = Counter()
        for pair, count in pair_counts.items():
            if pair in rules:
                insert = rules[pair]
                new_pair_counts[pair[0] + insert] += count
                new_pair_counts[insert + pair[1]] += count
            else:
                new_pair_counts[pair] += count
        pair_counts = new_pair_counts

    char_counts = Counter()
    for pair, count in pair_counts.items():
        char_counts[pair[0]] += count
        char_counts[pair[1]] += count

    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1

    for char in char_counts:
        char_counts[char] //= 2

    most_common = char_counts.most_common(1)[0][1]
    least_common = char_counts.most_common()[-1][1]
    answer = most_common - least_common

    print(f"Part 2: {answer}")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
