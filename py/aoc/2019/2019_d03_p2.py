from aoc.helper import AOC


@AOC.puzzle(2019, 3, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """R8,U5,L5,D3
# U7,R6,D4,L4""".splitlines()

#     data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83""".splitlines()

#     data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""".splitlines()

    wire1 = data[0].split(',')
    wire2 = data[1].split(',')

    def trace_wire_with_steps(wire):
        positions = {}
        x, y = 0, 0
        steps = 0
        for move in wire:
            direction = move[0]
            distance = int(move[1:])
            for _ in range(distance):
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                steps += 1
                if (x, y) not in positions:
                    positions[(x, y)] = steps
        return positions

    positions1 = trace_wire_with_steps(wire1)
    positions2 = trace_wire_with_steps(wire2)

    intersections = set(positions1.keys()) & set(positions2.keys())

    answer = min(positions1[pos] + positions2[pos] for pos in intersections)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
