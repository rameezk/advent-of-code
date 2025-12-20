from aoc.helper import AOC
from collections import defaultdict

@AOC.puzzle(2021, 12, 2)
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

    def dfs(node, visited, small_visited_twice):
        if node == 'end':
            return 1

        count = 0
        for neighbor in graph[node]:
            if neighbor == 'start':
                continue

            if neighbor.isupper():
                count += dfs(neighbor, visited.copy(), small_visited_twice)
            elif neighbor not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbor)
                count += dfs(neighbor, new_visited, small_visited_twice)
            elif not small_visited_twice:
                count += dfs(neighbor, visited.copy(), True)

        return count

    answer = dfs('start', {'start'}, False)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
