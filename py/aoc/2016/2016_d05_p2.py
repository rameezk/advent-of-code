from aoc.helper import AOC
import hashlib


@AOC.puzzle(2016, 5, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """abc"""

    door_id = data
    password = ['_'] * 8
    found_positions = set()
    index = 0

    while len(found_positions) < 8:
        hash_input = f"{door_id}{index}"
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            position_char = hash_result[5]
            if position_char.isdigit():
                position = int(position_char)
                if 0 <= position <= 7 and position not in found_positions:
                    character = hash_result[6]
                    password[position] = character
                    found_positions.add(position)
                    print(f"Found position {position}: {character} at index {index} -> {''.join(password)}")

        index += 1

    result = ''.join(password)
    print(f"Password: {result}")
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
