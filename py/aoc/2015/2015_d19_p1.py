from aoc.helper import AOC


@AOC.puzzle(2015, 19, 1)
def solve():
    sample_data = """H => HO
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

    distinct_molecules = set()

    for source, target in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(source)] == source:
                new_molecule = molecule[:i] + target + molecule[i+len(source):]
                distinct_molecules.add(new_molecule)

    result = len(distinct_molecules)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
