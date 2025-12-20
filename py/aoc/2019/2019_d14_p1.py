from aoc.helper import AOC
from collections import defaultdict
import math


@AOC.puzzle(2019, 14, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    reactions = {}
    for line in data:
        if not line:
            continue
        inputs, output = line.split(' => ')
        output_qty, output_chem = output.split()
        output_qty = int(output_qty)

        input_list = []
        for inp in inputs.split(', '):
            qty, chem = inp.split()
            input_list.append((int(qty), chem))

        reactions[output_chem] = (output_qty, input_list)

    def calculate_ore(fuel_amount):
        needed = defaultdict(int)
        needed['FUEL'] = fuel_amount
        leftover = defaultdict(int)

        while True:
            to_produce = None
            for chem in needed:
                if chem != 'ORE' and needed[chem] > 0:
                    to_produce = chem
                    break

            if to_produce is None:
                break

            amount_needed = needed[to_produce]
            needed[to_produce] = 0

            if leftover[to_produce] >= amount_needed:
                leftover[to_produce] -= amount_needed
                continue

            amount_needed -= leftover[to_produce]
            leftover[to_produce] = 0

            output_qty, inputs = reactions[to_produce]
            times = math.ceil(amount_needed / output_qty)
            produced = times * output_qty
            leftover[to_produce] += produced - amount_needed

            for qty, chem in inputs:
                needed[chem] += qty * times

        return needed['ORE']

    answer = calculate_ore(1)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
