from aoc.helper import AOC
from itertools import permutations


@AOC.puzzle(2015, 9, 2)
def solve():
    # data = """London to Dublin = 464
    # London to Belfast = 518
    # Dublin to Belfast = 141""".strip().splitlines()

    data = AOC.get_data().strip().splitlines()

    distances = {}
    cities = set()

    for line in data:
        parts = line.split(" = ")
        distance = int(parts[1])
        locations = parts[0].split(" to ")
        city1, city2 = locations[0], locations[1]

        cities.add(city1)
        cities.add(city2)

        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance

    max_distance = 0

    for route in permutations(cities):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += distances[(route[i], route[i + 1])]

        if total_distance > max_distance:
            max_distance = total_distance

    AOC.submit_answer(max_distance)


if __name__ == "__main__":
    solve()
