from aoc.helper import AOC
from collections import defaultdict

@AOC.puzzle(2021, 12, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()

    graph = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, visited, path):
        if node == 'end':
            return 1

        count = 0
        for neighbor in graph[node]:
            if neighbor.isupper() or neighbor not in visited:
                new_visited = visited.copy()
                if neighbor.islower():
                    new_visited.add(neighbor)
                count += dfs(neighbor, new_visited, path + [neighbor])

        return count

    answer = dfs('start', {'start'}, ['start'])

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
