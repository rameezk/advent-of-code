from aoc.helper import AOC
from itertools import combinations
from functools import reduce
import operator


@AOC.puzzle(2015, 24, 1)
def solve():
    data = AOC.get_data().strip()

    packages = list(map(int, data.split('\n')))

    total_weight = sum(packages)
    target_weight = total_weight // 3

    def quantum_entanglement(group):
        return reduce(operator.mul, group, 1)

    def can_split_remaining(remaining, num_groups):
        if num_groups == 1:
            return sum(remaining) == target_weight
        if num_groups == 2:
            for i in range(1, len(remaining)):
                for combo in combinations(remaining, i):
                    if sum(combo) == target_weight:
                        return True
            return False
        return False

    for group_size in range(1, len(packages)):
        min_qe = None
        for combo in combinations(packages, group_size):
            if sum(combo) == target_weight:
                remaining = [p for p in packages if p not in combo]
                if can_split_remaining(remaining, 2):
                    qe = quantum_entanglement(combo)
                    if min_qe is None or qe < min_qe:
                        min_qe = qe

        if min_qe is not None:
            AOC.submit_answer(min_qe)
            return


if __name__ == "__main__":
    solve()
