from aoc.helper import AOC
import heapq

@AOC.puzzle(2021, 15, 2)
def solve():
    data = AOC.get_data().strip().splitlines()



    original_grid = [[int(c) for c in line] for line in data]
    orig_rows = len(original_grid)
    orig_cols = len(original_grid[0])

    rows = orig_rows * 5
    cols = orig_cols * 5
    grid = [[0] * cols for _ in range(rows)]

    for tile_r in range(5):
        for tile_c in range(5):
            for r in range(orig_rows):
                for c in range(orig_cols):
                    new_val = original_grid[r][c] + tile_r + tile_c
                    if new_val > 9:
                        new_val = (new_val - 1) % 9 + 1
                    grid[tile_r * orig_rows + r][tile_c * orig_cols + c] = new_val

    pq = [(0, 0, 0)]
    visited = set()

    while pq:
        risk, r, c = heapq.heappop(pq)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if r == rows - 1 and c == cols - 1:
            answer = risk
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                heapq.heappush(pq, (risk + grid[nr][nc], nr, nc))

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
