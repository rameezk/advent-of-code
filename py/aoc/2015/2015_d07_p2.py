from aoc.helper import AOC


@AOC.puzzle(2015, 7, 2)
def solve():
    data = AOC.get_data()

    wires = {}
    for line in data.strip().splitlines():
        parts = line.split(" -> ")
        wire = parts[1]
        instruction = parts[0]
        wires[wire] = instruction

    # Override wire b with the signal from part 1
    wires["b"] = "3176"

    cache = {}

    def get_value(x):
        """Get the value of x, which can be a number or wire name."""
        if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
            return int(x)
        return evaluate(x)

    def evaluate(wire):
        """Evaluate and return the 16-bit signal on a wire."""
        if wire in cache:
            return cache[wire]

        instruction = wires[wire]
        parts = instruction.split()

        if len(parts) == 1:
            # Direct assignment: "123" or "x"
            result = get_value(parts[0])
        elif len(parts) == 2:
            # NOT gate: "NOT x"
            result = ~get_value(parts[1]) & 0xFFFF
        elif parts[1] == "AND":
            result = get_value(parts[0]) & get_value(parts[2])
        elif parts[1] == "OR":
            result = get_value(parts[0]) | get_value(parts[2])
        elif parts[1] == "LSHIFT":
            result = (get_value(parts[0]) << int(parts[2])) & 0xFFFF
        elif parts[1] == "RSHIFT":
            result = get_value(parts[0]) >> int(parts[2])
        else:
            raise ValueError(f"Unknown instruction: {instruction}")

        cache[wire] = result
        return result

    answer = evaluate("a")
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()