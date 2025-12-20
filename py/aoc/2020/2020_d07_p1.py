from aoc.helper import AOC

@AOC.puzzle(2020, 7, 1)
def solve():
    data = AOC.get_data().strip().splitlines()



    graph = {}

    for line in data:
        parts = line.split(" bags contain ")
        container = parts[0]

        if "no other bags" in parts[1]:
            graph[container] = []
        else:
            contents = []
            for item in parts[1].split(", "):
                item = item.replace(" bags", "").replace(" bag", "").replace(".", "")
                count_and_color = item.split(" ", 1)
                count = int(count_and_color[0])
                color = count_and_color[1]
                contents.append((count, color))
            graph[container] = contents

    reverse_graph = {}
    for container, contents in graph.items():
        for count, color in contents:
            if color not in reverse_graph:
                reverse_graph[color] = []
            reverse_graph[color].append(container)

    def find_containers(bag_color):
        result = set()
        if bag_color not in reverse_graph:
            return result

        for container in reverse_graph[bag_color]:
            result.add(container)
            result.update(find_containers(container))

        return result

    containers = find_containers("shiny gold")
    answer = len(containers)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
