from aoc.helper import AOC
import random


@AOC.puzzle(2015, 19, 2)
def solve():
    sample_data = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""

    data = AOC.get_data().strip()

    lines = data.split('\n')

    replacements = []
    molecule = ""

    for line in lines:
        if '=>' in line:
            parts = line.split(' => ')
            replacements.append((parts[0], parts[1]))
        elif line.strip():
            molecule = line.strip()

    reverse_replacements = [(target, source) for source, target in replacements]
    reverse_replacements.sort(key=lambda x: len(x[0]), reverse=True)

    target = molecule
    steps = 0

    while target != 'e':
        original_target = target
        for source, replacement in reverse_replacements:
            if source in target:
                target = target.replace(source, replacement, 1)
                steps += 1
                break

        if target == original_target:
            target = molecule
            steps = 0
            random.shuffle(reverse_replacements)

    result = steps
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
