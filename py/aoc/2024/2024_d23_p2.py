from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2024, 23, 2)
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

    def bron_kerbosch(r, p, x, cliques):
        if not p and not x:
            cliques.append(r)
            return

        for v in list(p):
            bron_kerbosch(
                r | {v},
                p & graph[v],
                x & graph[v],
                cliques
            )
            p.remove(v)
            x.add(v)

    cliques = []
    all_nodes = set(graph.keys())
    bron_kerbosch(set(), all_nodes, set(), cliques)

    max_clique = max(cliques, key=len)
    password = ','.join(sorted(max_clique))

    print(password)
    AOC.submit_answer(password)


if __name__ == "__main__":
    solve()
