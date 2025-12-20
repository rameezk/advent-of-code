from aoc.helper import AOC
from collections import deque
from heapq import heappush, heappop


@AOC.puzzle(2019, 18, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    grid = [list(line) for line in data]
    rows, cols = len(grid), len(grid[0])

    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                start = (r, c)
                break
        if start:
            break

    sr, sc = start
    grid[sr][sc] = '#'
    grid[sr-1][sc] = '#'
    grid[sr+1][sc] = '#'
    grid[sr][sc-1] = '#'
    grid[sr][sc+1] = '#'
    grid[sr-1][sc-1] = '@'
    grid[sr-1][sc+1] = '@'
    grid[sr+1][sc-1] = '@'
    grid[sr+1][sc+1] = '@'

    starts = []
    keys = {}
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == '@':
                starts.append((r, c))
                grid[r][c] = '.'
            elif cell.islower():
                keys[(r, c)] = cell

    all_keys = set(keys.values())
    num_keys = len(all_keys)

    def bfs_from(start_pos):
        reachable = {}
        queue = deque([(start_pos, 0, set())])
        visited = {start_pos}

        while queue:
            (r, c), dist, doors = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        cell = grid[nr][nc]
                        new_doors = doors.copy()

                        if cell.isupper():
                            new_doors.add(cell.lower())

                        if cell.islower() and (nr, nc) != start_pos:
                            reachable[cell] = (dist + 1, frozenset(new_doors))
                        else:
                            queue.append(((nr, nc), dist + 1, new_doors))

        return reachable

    graph = {}
    for i, start_pos in enumerate(starts):
        graph[f'@{i}'] = bfs_from(start_pos)
    for key_pos, key_char in keys.items():
        graph[key_char] = bfs_from(key_pos)

    initial_positions = tuple(f'@{i}' for i in range(len(starts)))
    pq = [(0, initial_positions, frozenset())]
    visited = {}

    while pq:
        dist, positions, collected = heappop(pq)

        if len(collected) == num_keys:
            answer = dist
            print(answer)
            AOC.submit_answer(answer)
            return

        state = (positions, collected)
        if state in visited:
            continue
        visited[state] = dist

        for robot_idx, pos in enumerate(positions):
            for next_key, (key_dist, doors_needed) in graph[pos].items():
                if doors_needed.issubset(collected):
                    new_dist = dist + key_dist
                    new_collected = collected | {next_key}
                    new_positions = tuple(
                        next_key if i == robot_idx else positions[i]
                        for i in range(len(positions))
                    )
                    new_state = (new_positions, new_collected)
                    if new_state not in visited:
                        heappush(pq, (new_dist, new_positions, new_collected))

    print("No solution found - search exhausted")


if __name__ == "__main__":
    solve()
