from aoc.helper import AOC


@AOC.puzzle(2024, 14, 2)
def solve():
    data = AOC.get_data()

    width = 101
    height = 103

    robots = []
    for line in data.strip().splitlines():
        parts = line.split()
        pos = parts[0].split("=")[1].split(",")
        vel = parts[1].split("=")[1].split(",")
        px, py = int(pos[0]), int(pos[1])
        vx, vy = int(vel[0]), int(vel[1])
        robots.append((px, py, vx, vy))

    def get_positions(seconds):
        positions = set()
        for px, py, vx, vy in robots:
            final_x = (px + vx * seconds) % width
            final_y = (py + vy * seconds) % height
            positions.add((final_x, final_y))
        return positions

    def visualize(positions):
        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                if (x, y) in positions:
                    row.append('#')
                else:
                    row.append('.')
            grid.append(''.join(row))
        return '\n'.join(grid)

    def has_tree_pattern(positions):
        max_consecutive = 0
        for y in range(height):
            consecutive = 0
            for x in range(width):
                if (x, y) in positions:
                    consecutive += 1
                    max_consecutive = max(max_consecutive, consecutive)
                else:
                    consecutive = 0
        return max_consecutive >= 10

    for seconds in range(1, 10000):
        positions = get_positions(seconds)

        if has_tree_pattern(positions):
            print(f"\nSecond {seconds}:")
            print(visualize(positions))
            print(f"\nAnswer: {seconds}")
            AOC.submit_answer(seconds)
            break


if __name__ == "__main__":
    solve()
