from aoc.helper import AOC


@AOC.puzzle(2019, 6, 2)
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
    # K)L
    # K)YOU
    # I)SAN""".strip().splitlines()

    orbits = {}
    for line in data:
        center, orbiter = line.split(')')
        orbits[orbiter] = center

    def get_path_to_com(obj):
        path = []
        current = obj
        while current in orbits:
            current = orbits[current]
            path.append(current)
        return path

    you_path = get_path_to_com('YOU')
    san_path = get_path_to_com('SAN')

    you_set = set(you_path)
    san_set = set(san_path)

    common = you_set & san_set

    min_transfers = float('inf')
    for ancestor in common:
        transfers = you_path.index(ancestor) + san_path.index(ancestor)
        min_transfers = min(min_transfers, transfers)

    answer = min_transfers
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
