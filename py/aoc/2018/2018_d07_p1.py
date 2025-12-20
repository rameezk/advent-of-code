from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2018, 7, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.""".splitlines()

    dependencies = defaultdict(set)
    all_steps = set()

    for line in data:
        parts = line.split()
        prerequisite = parts[1]
        step = parts[7]
        dependencies[step].add(prerequisite)
        all_steps.add(prerequisite)
        all_steps.add(step)

    completed = []

    while len(completed) < len(all_steps):
        available = []
        for step in all_steps:
            if step not in completed:
                if all(dep in completed for dep in dependencies[step]):
                    available.append(step)

        available.sort()
        next_step = available[0]
        completed.append(next_step)

    result = ''.join(completed)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
