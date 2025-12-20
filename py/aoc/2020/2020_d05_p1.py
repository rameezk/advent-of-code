from aoc.helper import AOC

@AOC.puzzle(2020, 5, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    lines = data

    max_seat_id = 0

    for line in lines:
        row_binary = line[:7].replace('F', '0').replace('B', '1')
        col_binary = line[7:].replace('L', '0').replace('R', '1')

        row = int(row_binary, 2)
        col = int(col_binary, 2)

        seat_id = row * 8 + col
        max_seat_id = max(max_seat_id, seat_id)

    answer = max_seat_id

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
