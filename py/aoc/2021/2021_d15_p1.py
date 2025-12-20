from aoc.helper import AOC
import heapq

@AOC.puzzle(2021, 15, 1)
def solve():
    data = AOC.get_data().strip().splitlines()



    grid = [[int(c) for c in line] for line in data]
    rows = len(grid)
    cols = len(grid[0])

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
