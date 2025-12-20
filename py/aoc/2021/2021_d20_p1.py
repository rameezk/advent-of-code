from aoc.helper import AOC

@AOC.puzzle(2021, 20, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
##..#.
##....
###..#
#..#..
#..###"""

    lines = data.split('\n')
    algorithm = lines[0]

    image_lines = [line for line in lines[2:] if line.strip()]
    image = set()
    for y, line in enumerate(image_lines):
        for x, char in enumerate(line):
            if char == '#':
                image.add((x, y))

    def get_bounds(image):
        if not image:
            return 0, 0, 0, 0
        xs = [x for x, y in image]
        ys = [y for x, y in image]
        return min(xs), max(xs), min(ys), max(ys)

    def enhance(image, algorithm, default_lit):
        min_x, max_x, min_y, max_y = get_bounds(image)

        new_image = set()

        for y in range(min_y - 2, max_y + 3):
            for x in range(min_x - 2, max_x + 3):
                binary = ""
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy

                        if min_x <= nx <= max_x and min_y <= ny <= max_y:
                            is_lit = (nx, ny) in image
                        else:
                            is_lit = default_lit

                        binary += '1' if is_lit else '0'

                index = int(binary, 2)
                if algorithm[index] == '#':
                    new_image.add((x, y))

        return new_image

    current_image = image
    default_lit = False

    for i in range(2):
        current_image = enhance(current_image, algorithm, default_lit)

        if algorithm[0] == '#':
            default_lit = not default_lit

    answer = len(current_image)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
