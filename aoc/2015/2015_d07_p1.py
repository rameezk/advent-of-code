from aoc.helper import download_input, submit_answer

from collections import defaultdict
import re


def run(circuit, known_wires):
    still_operations_left = False
    next_circuit = []

    for c in circuit:
        print(c)
        signal, identifier = c.split(" -> ")
        if signal.isdigit():
            known_wires[identifier] = int(signal)
        else:
            o_s = signal.split(" ")
            print(o_s)
            if len(o_s) == 1:
                if o_s[0] in known_wires:
                    known_wires[identifier] = known_wires[o_s[0]]
                else:
                    next_circuit.append(c)
                    still_operations_left = True
            elif len(o_s) == 2:
                operator, operand = o_s
                if operand not in known_wires:
                    next_circuit.append(c)
                    still_operations_left = True
                else:
                    known_wires[identifier] = (1 << 16) - 1 - int(known_wires[operand])
            else:
                left_operand, operator, right_operand = o_s

                if (not left_operand.isdigit() and left_operand not in known_wires) or (
                    not right_operand.isdigit() and right_operand not in known_wires
                ):
                    next_circuit.append(c)
                    still_operations_left = True
                else:
                    if operator == "AND":
                        known_wires[identifier] = (
                            known_wires[left_operand] & known_wires[right_operand]
                        )
                    elif operator == "OR":
                        known_wires[identifier] = (
                            known_wires[left_operand] | known_wires[right_operand]
                        )
                    elif operator == "LSHIFT":
                        known_wires[identifier] = known_wires[left_operand] << int(
                            right_operand
                        )
                    else:
                        known_wires[identifier] = known_wires[left_operand] >> int(
                            right_operand
                        )

    if still_operations_left:
        return run(next_circuit, known_wires)
    else:
        return known_wires


if __name__ == "__main__":
    # download_input(2015, 7)

    with open("./2015_d07.txt") as f:
        circuit = f.read().strip().splitlines()

    #     circuit = """
    # 123 -> x
    # 456 -> y
    # x AND y -> d
    # x OR y -> e
    # x LSHIFT 2 -> f
    # y RSHIFT 2 -> g
    # NOT x -> h
    # NOT y -> i
    #     """.strip().splitlines()

    wires = {}
    run(circuit, wires)
    print(wires)
