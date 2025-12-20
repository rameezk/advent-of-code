from aoc.helper import AOC

@AOC.puzzle(2020, 13, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """939
# 7,13,x,x,59,x,31,19""".splitlines()

    earliest = int(data[0])
    buses = [int(x) for x in data[1].split(',') if x != 'x']

    min_wait = float('inf')
    best_bus = None

    for bus in buses:
        remainder = earliest % bus
        if remainder == 0:
            wait = 0
        else:
            wait = bus - remainder
        if wait < min_wait:
            min_wait = wait
            best_bus = bus

    answer = best_bus * min_wait

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
