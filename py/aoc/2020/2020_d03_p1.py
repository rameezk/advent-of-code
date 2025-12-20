from aoc.helper import AOC

@AOC.puzzle(2020, 3, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    sample_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

    # data = sample_data.strip().splitlines()

    trees = 0
    x = 0
    for y in range(len(data)):
        row = data[y]
        if row[x % len(row)] == '#':
            trees += 1
        x += 3

    print(trees)

if __name__ == "__main__":
    solve()
