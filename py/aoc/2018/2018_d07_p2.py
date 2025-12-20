from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2018, 7, 2)
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

    num_workers = 5
    base_time = 60

#     num_workers = 2
#     base_time = 0

    workers = [None] * num_workers
    worker_time_left = [0] * num_workers
    completed = []
    in_progress = set()
    time = 0

    while len(completed) < len(all_steps):
        for i in range(num_workers):
            if worker_time_left[i] == 0 and workers[i] is not None:
                completed.append(workers[i])
                workers[i] = None

        available = []
        for step in all_steps:
            if step not in completed and step not in in_progress:
                if all(dep in completed for dep in dependencies[step]):
                    available.append(step)

        available.sort()

        for i in range(num_workers):
            if workers[i] is None and available:
                next_step = available.pop(0)
                workers[i] = next_step
                worker_time_left[i] = base_time + ord(next_step) - ord('A') + 1
                in_progress.add(next_step)

        if any(w is not None for w in workers):
            time += 1
            for i in range(num_workers):
                if workers[i] is not None:
                    worker_time_left[i] -= 1

    print(time)
    AOC.submit_answer(time)


if __name__ == "__main__":
    solve()
