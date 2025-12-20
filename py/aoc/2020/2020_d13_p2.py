from aoc.helper import AOC

@AOC.puzzle(2020, 13, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """939
# 7,13,x,x,59,x,31,19""".splitlines()

    buses_str = data[1].split(',')
    buses = []
    for i, bus in enumerate(buses_str):
        if bus != 'x':
            buses.append((int(bus), i))

    t = 0
    step = 1

    for bus_id, offset in buses:
        while (t + offset) % bus_id != 0:
            t += step
        step *= bus_id

    answer = t

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
