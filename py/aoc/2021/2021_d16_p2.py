from aoc.helper import AOC
from functools import reduce
from operator import mul

@AOC.puzzle(2021, 16, 2)
def solve():
    data = AOC.get_data().strip()

#     test_cases = [
#         ("C200B40A82", 3),
#         ("04005AC33890", 54),
#         ("880086C3E88112", 7),
#         ("CE00C43D881120", 9),
#         ("D8005AC2A8F0", 1),
#         ("F600BC2D8F", 0),
#         ("9C005AC2F8F0", 0),
#         ("9C0141080250320F1802104A08", 1),
#     ]

    def hex_to_bin(hex_str):
        return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

    def parse_packet(bits, pos):
        version = int(bits[pos:pos+3], 2)
        type_id = int(bits[pos+3:pos+6], 2)
        pos += 6

        if type_id == 4:
            value_bits = ""
            while bits[pos] == '1':
                value_bits += bits[pos+1:pos+5]
                pos += 5
            value_bits += bits[pos+1:pos+5]
            pos += 5
            value = int(value_bits, 2)
        else:
            length_type_id = bits[pos]
            pos += 1
            sub_values = []

            if length_type_id == '0':
                total_length = int(bits[pos:pos+15], 2)
                pos += 15
                end_pos = pos + total_length

                while pos < end_pos:
                    sub_value, pos = parse_packet(bits, pos)
                    sub_values.append(sub_value)
            else:
                num_packets = int(bits[pos:pos+11], 2)
                pos += 11

                for _ in range(num_packets):
                    sub_value, pos = parse_packet(bits, pos)
                    sub_values.append(sub_value)

            if type_id == 0:
                value = sum(sub_values)
            elif type_id == 1:
                value = reduce(mul, sub_values, 1)
            elif type_id == 2:
                value = min(sub_values)
            elif type_id == 3:
                value = max(sub_values)
            elif type_id == 5:
                value = 1 if sub_values[0] > sub_values[1] else 0
            elif type_id == 6:
                value = 1 if sub_values[0] < sub_values[1] else 0
            elif type_id == 7:
                value = 1 if sub_values[0] == sub_values[1] else 0

        return value, pos

#     for test_hex, expected in test_cases:
#         binary = hex_to_bin(test_hex)
#         result, _ = parse_packet(binary, 0)
#         print(f"{test_hex}: expected {expected}, got {result}")
#         assert result == expected, f"Test failed for {test_hex}"

    binary = hex_to_bin(data)
    answer, _ = parse_packet(binary, 0)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
