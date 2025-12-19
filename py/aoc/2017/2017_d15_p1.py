from aoc.helper import AOC

@AOC.puzzle(2017, 15, 1)
def solve():
    data = AOC.get_data().strip()

    lines = data.strip().split('\n')
    gen_a_start = int(lines[0].split()[-1])
    gen_b_start = int(lines[1].split()[-1])

    factor_a = 16807
    factor_b = 48271
    divisor = 2147483647

    gen_a = gen_a_start
    gen_b = gen_b_start

    matches = 0
    pairs = 40_000_000

    for _ in range(pairs):
        gen_a = (gen_a * factor_a) % divisor
        gen_b = (gen_b * factor_b) % divisor

        if gen_a & 0xFFFF == gen_b & 0xFFFF:
            matches += 1

    answer = matches
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
