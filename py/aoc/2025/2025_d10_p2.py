import re

import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

from aoc.helper import AOC


@AOC.puzzle(2025, 10, 2)
def solve():
    data = AOC.get_data()

#     data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    total = 0
    for line in data.strip().splitlines():
        joltage = re.search(r"\{([0-9,]+)\}", line).group(1)
        buttons = re.findall(r"\(([0-9,]+)\)", line)
        target = [int(x) for x in joltage.split(",")]
        button_indices = [[int(x) for x in b.split(",")] for b in buttons]
        presses = min_presses(target, button_indices)
        total += presses

    print(total)
    AOC.submit_answer(total)

def min_presses(target, buttons):
    n_buttons = len(buttons)
    n_counters = len(target)

    A = np.zeros((n_counters, n_buttons))
    for i, btn in enumerate(buttons):
        for j in btn:
            A[j][i] = 1

    c = np.ones(n_buttons)

    constraints = LinearConstraint(A, target, target)

    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)  # all variables are integers

    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    return int(round(result.fun))

if __name__ == "__main__":
    solve()
