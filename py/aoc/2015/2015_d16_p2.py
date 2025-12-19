from aoc.helper import AOC


@AOC.puzzle(2015, 16, 2)
def solve():
    data = AOC.get_data().strip()

    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for line in data.split('\n'):
        parts = line.split(': ', 1)
        sue_num = int(parts[0].split()[1])
        properties = parts[1]

        matches = True
        for prop in properties.split(', '):
            key, value = prop.split(': ')
            value = int(value)

            if key in ["cats", "trees"]:
                if value <= target[key]:
                    matches = False
                    break
            elif key in ["pomeranians", "goldfish"]:
                if value >= target[key]:
                    matches = False
                    break
            else:
                if target[key] != value:
                    matches = False
                    break

        if matches:
            AOC.submit_answer(sue_num)
            return


if __name__ == "__main__":
    solve()
