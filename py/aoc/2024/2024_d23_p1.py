from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2024, 23, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn""".strip().splitlines()

    graph = defaultdict(set)
    for line in data:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for n1 in neighbors:
            for n2 in neighbors:
                if n1 != n2 and n2 in graph[n1]:
                    triangle = tuple(sorted([node, n1, n2]))
                    triangles.add(triangle)

    count = 0
    for triangle in triangles:
        if any(node.startswith('t') for node in triangle):
            count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
