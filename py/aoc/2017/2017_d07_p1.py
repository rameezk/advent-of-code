from aoc.helper import AOC

@AOC.puzzle(2017, 7, 1)
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

    all_programs = set()
    held_programs = set()

    for line in data.split('\n'):
        parts = line.split()
        program_name = parts[0]
        all_programs.add(program_name)

        if '->' in line:
            arrow_idx = parts.index('->')
            children = ''.join(parts[arrow_idx + 1:]).split(',')
            for child in children:
                held_programs.add(child)

    bottom = list(all_programs - held_programs)[0]
    AOC.submit_answer(bottom)

if __name__ == "__main__":
    solve()
