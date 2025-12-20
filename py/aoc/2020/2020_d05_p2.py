from aoc.helper import AOC

@AOC.puzzle(2020, 5, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    lines = data

    seat_ids = set()

    for line in lines:
        row_binary = line[:7].replace('F', '0').replace('B', '1')
        col_binary = line[7:].replace('L', '0').replace('R', '1')

        row = int(row_binary, 2)
        col = int(col_binary, 2)

        seat_id = row * 8 + col
        seat_ids.add(seat_id)

    min_seat = min(seat_ids)
    max_seat = max(seat_ids)

    for seat_id in range(min_seat, max_seat + 1):
        if seat_id not in seat_ids:
            if (seat_id - 1) in seat_ids and (seat_id + 1) in seat_ids:
                answer = seat_id
                break

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
