from aoc.helper import AOC

@AOC.puzzle(2020, 3, 2)
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

    def count_trees(data, right, down):
        trees = 0
        x = 0
        y = 0
        while y < len(data):
            row = data[y]
            if row[x % len(row)] == '#':
                trees += 1
            x += right
            y += down
        return trees

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for right, down in slopes:
        trees = count_trees(data, right, down)
        result *= trees

    print(result)

if __name__ == "__main__":
    solve()
