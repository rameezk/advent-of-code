from aoc.helper import AOC

@AOC.puzzle(2020, 7, 2)
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

    def count_bags(bag_color):
        total = 0
        if bag_color not in graph:
            return 0

        for count, color in graph[bag_color]:
            total += count
            total += count * count_bags(color)

        return total

    answer = count_bags("shiny gold")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
