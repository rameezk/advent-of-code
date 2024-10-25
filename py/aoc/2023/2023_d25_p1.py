from aoc.helper import download_input, submit_answer
from aoc.util import benchmark
from collections import defaultdict


@benchmark
def run():
    download_input(2023, 25)

    diagram = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
    """.strip().splitlines()

    W = defaultdict(lambda: set())
    for line in diagram:
        left, right = line.split(":")
        right = right.split()
        W[left].update(right)

        for r in right:
            W[r].add(left)

    print(W["pzl"])


if __name__ == "__main__":
    run()
