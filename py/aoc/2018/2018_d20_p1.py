from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2018, 20, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """^WNE$"""
#     data = """^ENWWW(NEEE|SSE(EE|N))$"""
#     data = """^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"""
#     data = """^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""
#     data = """^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""

    directions = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    doors = set()
    stack = []
    x, y = 0, 0
    stack_positions = [(x, y)]

    for char in data[1:-1]:
        if char in directions:
            dx, dy = directions[char]
            nx, ny = x + dx, y + dy
            doors.add(((x, y), (nx, ny)))
            doors.add(((nx, ny), (x, y)))
            x, y = nx, ny
        elif char == '(':
            stack.append((x, y))
        elif char == ')':
            x, y = stack.pop()
        elif char == '|':
            x, y = stack[-1]

    distances = {(0, 0): 0}
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if ((x, y), (nx, ny)) in doors and (nx, ny) not in distances:
                distances[(nx, ny)] = dist + 1
                queue.append((nx, ny, dist + 1))

    max_dist = max(distances.values())
    print(max_dist)
    AOC.submit_answer(max_dist)


if __name__ == "__main__":
    solve()
