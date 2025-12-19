from aoc.helper import AOC
import hashlib


@AOC.puzzle(2016, 5, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """abc"""

    door_id = data
    password = []
    index = 0

    while len(password) < 8:
        hash_input = f"{door_id}{index}"
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            password.append(hash_result[5])
            print(f"Found character {len(password)}: {hash_result[5]} at index {index}")

        index += 1

    result = ''.join(password)
    print(f"Password: {result}")
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
