from aoc.helper import AOC


@AOC.puzzle(2016, 18, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """.^^.^.^^^^"""

    def is_trap(left, center, right):
        if left == '^' and center == '^' and right == '.':
            return True
        if left == '.' and center == '^' and right == '^':
            return True
        if left == '^' and center == '.' and right == '.':
            return True
        if left == '.' and center == '.' and right == '^':
            return True
        return False

    rows = 40
    current_row = data
    safe_count = current_row.count('.')

    for _ in range(rows - 1):
        next_row = []
        for i in range(len(current_row)):
            left = current_row[i - 1] if i > 0 else '.'
            center = current_row[i]
            right = current_row[i + 1] if i < len(current_row) - 1 else '.'

            if is_trap(left, center, right):
                next_row.append('^')
            else:
                next_row.append('.')
                safe_count += 1

        current_row = ''.join(next_row)

    print(safe_count)
    AOC.submit_answer(safe_count)


if __name__ == "__main__":
    solve()
