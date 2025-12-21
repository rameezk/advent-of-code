from aoc.helper import AOC


@AOC.puzzle(2024, 24, 1)
def solve():
    data = AOC.get_data().strip().split("\n\n")

#     data = """x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1
#
# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj""".strip().split("\n\n")

    wires = {}
    gates = []

    for line in data[0].splitlines():
        wire, value = line.split(": ")
        wires[wire] = int(value)

    for line in data[1].splitlines():
        parts = line.split(" -> ")
        output = parts[1]
        operation_parts = parts[0].split()
        input1, op, input2 = operation_parts[0], operation_parts[1], operation_parts[2]
        gates.append((input1, op, input2, output))

    while gates:
        remaining_gates = []
        for input1, op, input2, output in gates:
            if input1 in wires and input2 in wires:
                val1 = wires[input1]
                val2 = wires[input2]

                if op == "AND":
                    result = val1 & val2
                elif op == "OR":
                    result = val1 | val2
                elif op == "XOR":
                    result = val1 ^ val2

                wires[output] = result
            else:
                remaining_gates.append((input1, op, input2, output))

        if len(remaining_gates) == len(gates):
            break
        gates = remaining_gates

    z_wires = sorted([(k, v) for k, v in wires.items() if k.startswith('z')])

    binary_str = ""
    for wire, value in z_wires:
        binary_str = str(value) + binary_str

    result = int(binary_str, 2)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
