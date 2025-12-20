from aoc.helper import AOC

@AOC.puzzle(2021, 16, 1)
def solve():
    data = AOC.get_data().strip()

#     test_cases = [
#         ("8A004A801A8002F478", 16),
#         ("620080001611562C8802118E34", 12),
#         ("C0015000016115A2E0802F182340", 23),
#         ("A0016C880162017C3686B18A3D4780", 31),
#     ]

    def hex_to_bin(hex_str):
        return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

    def parse_packet(bits, pos):
        version = int(bits[pos:pos+3], 2)
        type_id = int(bits[pos+3:pos+6], 2)
        pos += 6

        version_sum = version

        if type_id == 4:
            while bits[pos] == '1':
                pos += 5
            pos += 5
        else:
            length_type_id = bits[pos]
            pos += 1

            if length_type_id == '0':
                total_length = int(bits[pos:pos+15], 2)
                pos += 15
                end_pos = pos + total_length

                while pos < end_pos:
                    sub_version_sum, pos = parse_packet(bits, pos)
                    version_sum += sub_version_sum
            else:
                num_packets = int(bits[pos:pos+11], 2)
                pos += 11

                for _ in range(num_packets):
                    sub_version_sum, pos = parse_packet(bits, pos)
                    version_sum += sub_version_sum

        return version_sum, pos

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
