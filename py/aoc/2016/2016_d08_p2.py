from aoc.helper import AOC


@AOC.puzzle(2016, 8, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1""".splitlines()

    width = 50
    height = 6
#     width = 7
#     height = 3
    screen = [[False] * width for _ in range(height)]

    for line in data:
        if line.startswith("rect"):
            parts = line.split()[1].split("x")
            w, h = int(parts[0]), int(parts[1])
            for y in range(h):
                for x in range(w):
                    screen[y][x] = True
        elif line.startswith("rotate row"):
            parts = line.split()
            row = int(parts[2].split("=")[1])
            shift = int(parts[4])
            old_row = screen[row][:]
            for x in range(width):
                screen[row][(x + shift) % width] = old_row[x]
        elif line.startswith("rotate column"):
            parts = line.split()
            col = int(parts[2].split("=")[1])
            shift = int(parts[4])
            old_col = [screen[y][col] for y in range(height)]
            for y in range(height):
                screen[(y + shift) % height][col] = old_col[y]

    for row in screen:
        print("".join("#" if pixel else "." for pixel in row))

    answer = input("Enter the letters you see: ").strip()
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
