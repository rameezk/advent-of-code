from aoc.helper import AOC
import re
from collections import deque


@AOC.puzzle(2016, 22, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """root@ebhq-gridcenter# df -h
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%""".splitlines()

    nodes = {}
    max_x = 0
    max_y = 0

    for line in data:
        if line.startswith('/dev/grid/node'):
            match = re.search(r'node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T', line)
            if match:
                x, y, size, used, avail = map(int, match.groups())
                nodes[(x, y)] = {'size': size, 'used': used, 'avail': avail}
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    empty_pos = None
    for pos, node in nodes.items():
        if node['used'] == 0:
            empty_pos = pos
            break

    goal_pos = (max_x, 0)
    target_pos = (0, 0)

    walls = set()
    for pos, node in nodes.items():
        if node['size'] > 100:
            walls.add(pos)

    def bfs_to_goal():
        queue = deque([(empty_pos, goal_pos, 0)])
        visited = {(empty_pos, goal_pos)}

        while queue:
            state_tuple = queue.popleft()
            empty = state_tuple[0]
            goal = state_tuple[1]
            steps = state_tuple[2]

            if goal == target_pos:
                return steps

            ex, ey = empty
            gx, gy = goal

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_ex, new_ey = ex + dx, ey + dy

                if (new_ex, new_ey) not in nodes:
                    continue
                if (new_ex, new_ey) in walls:
                    continue

                if (new_ex, new_ey) == (gx, gy):
                    new_goal = (ex, ey)
                    state = ((new_ex, new_ey), new_goal)
                    if state not in visited:
                        visited.add(state)
                        queue.append(((new_ex, new_ey), new_goal, steps + 1))
                else:
                    state = ((new_ex, new_ey), (gx, gy))
                    if state not in visited:
                        visited.add(state)
                        queue.append(((new_ex, new_ey), (gx, gy), steps + 1))

        return -1

    steps = bfs_to_goal()

    print(steps)
    AOC.submit_answer(steps)


if __name__ == "__main__":
    solve()
