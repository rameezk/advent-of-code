from aoc.helper import AOC


@AOC.puzzle(2024, 24, 2)
def solve():
    data = AOC.get_data().strip().split("\n\n")

#     data = """x00: 0
# x01: 1
# x02: 0
# x03: 1
# x04: 0
# x05: 1
# y00: 0
# y01: 0
# y02: 1
# y03: 1
# y04: 0
# y05: 1
#
# x00 AND y00 -> z05
# x01 AND y01 -> z02
# x02 AND y02 -> z01
# x03 AND y03 -> z03
# x04 AND y04 -> z04
# x05 AND y05 -> z00""".strip().split("\n\n")

    gates = {}
    for line in data[1].splitlines():
        parts = line.split(" -> ")
        output = parts[1]
        operation_parts = parts[0].split()
        input1, op, input2 = operation_parts[0], operation_parts[1], operation_parts[2]
        gates[output] = (input1, op, input2)

    def find_gate(i1, op, i2):
        for output, (in1, operation, in2) in gates.items():
            if operation == op and {in1, in2} == {i1, i2}:
                return output
        return None

    def get_op(wire):
        if wire in gates:
            return gates[wire][1]
        return None

    wrong = set()

    for output, (in1, op, in2) in gates.items():
        if output[0] == 'z' and op != 'XOR' and output != 'z45':
            wrong.add(output)

        if op == 'XOR' and output[0] not in ['x', 'y', 'z'] and in1[0] not in ['x', 'y', 'z'] and in2[0] not in ['x', 'y', 'z']:
            wrong.add(output)

        if op == 'AND' and 'x00' not in [in1, in2]:
            for sub_out, (sub_in1, sub_op, sub_in2) in gates.items():
                if (output == sub_in1 or output == sub_in2) and sub_op != 'OR':
                    wrong.add(output)

        if op == 'XOR':
            for sub_out, (sub_in1, sub_op, sub_in2) in gates.items():
                if (output == sub_in1 or output == sub_in2) and sub_op == 'OR':
                    wrong.add(output)

    result = ",".join(sorted(wrong))
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
