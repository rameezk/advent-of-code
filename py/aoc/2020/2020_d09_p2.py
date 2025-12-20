from aoc.helper import AOC

@AOC.puzzle(2020, 9, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576""".splitlines()

    numbers = [int(line) for line in data]
    preamble_size = 25

    def is_valid(target, preamble):
        for i in range(len(preamble)):
            for j in range(i + 1, len(preamble)):
                if preamble[i] + preamble[j] == target:
                    return True
        return False

    invalid_number = None
    for i in range(preamble_size, len(numbers)):
        target = numbers[i]
        preamble = numbers[i - preamble_size:i]

        if not is_valid(target, preamble):
            invalid_number = target
            break

    def find_contiguous_sum(numbers, target):
        for i in range(len(numbers)):
            current_sum = numbers[i]
            for j in range(i + 1, len(numbers)):
                current_sum += numbers[j]
                if current_sum == target:
                    contiguous_range = numbers[i:j+1]
                    return min(contiguous_range) + max(contiguous_range)
                elif current_sum > target:
                    break
        return None

    answer = find_contiguous_sum(numbers, invalid_number)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
