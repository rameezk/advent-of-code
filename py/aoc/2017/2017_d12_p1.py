from aoc.helper import AOC

@AOC.puzzle(2017, 12, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5"""

    graph = {}
    for line in data.split('\n'):
        node, neighbors = line.split(' <-> ')
        node = int(node)
        neighbors = [int(n) for n in neighbors.split(', ')]
        graph[node] = neighbors

    visited = set()
    queue = [0]
    visited.add(0)

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    answer = len(visited)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
