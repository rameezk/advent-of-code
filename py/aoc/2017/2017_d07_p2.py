from aoc.helper import AOC
from collections import defaultdict

@AOC.puzzle(2017, 7, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)"""

    weights = {}
    children = {}

    for line in data.split('\n'):
        parts = line.split()
        program_name = parts[0]
        weight = int(parts[1].strip('()'))
        weights[program_name] = weight

        if '->' in line:
            arrow_idx = parts.index('->')
            child_list = ''.join(parts[arrow_idx + 1:]).split(',')
            children[program_name] = child_list
        else:
            children[program_name] = []

    def total_weight(node):
        return weights[node] + sum(total_weight(child) for child in children[node])

    def find_unbalanced(node):
        if not children[node]:
            return None

        child_weights = [(child, total_weight(child)) for child in children[node]]

        weight_counts = defaultdict(list)
        for child, weight in child_weights:
            weight_counts[weight].append(child)

        if len(weight_counts) == 1:
            return None

        wrong_weight = None
        correct_weight = None
        for weight, nodes in weight_counts.items():
            if len(nodes) == 1:
                wrong_weight = weight
                wrong_node = nodes[0]
            else:
                correct_weight = weight

        result = find_unbalanced(wrong_node)
        if result is not None:
            return result

        diff = correct_weight - wrong_weight
        return weights[wrong_node] + diff

    all_programs = set(weights.keys())
    held_programs = set()
    for child_list in children.values():
        held_programs.update(child_list)
    root = list(all_programs - held_programs)[0]

    answer = find_unbalanced(root)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
