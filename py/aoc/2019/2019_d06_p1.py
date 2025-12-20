from aoc.helper import AOC


@AOC.puzzle(2019, 6, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    # data = """COM)B
    # B)C
    # C)D
    # D)E
    # E)F
    # B)G
    # G)H
    # D)I
    # E)J
    # J)K
    # K)L""".strip().splitlines()

    orbits = {}
    for line in data:
        center, orbiter = line.split(')')
        orbits[orbiter] = center

    total = 0
    for obj in orbits:
        current = obj
        while current in orbits:
            total += 1
            current = orbits[current]

    answer = total
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
