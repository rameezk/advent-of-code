from aoc.helper import AOC

@AOC.puzzle(2021, 4, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""

    sections = data.split('\n\n')
    numbers = list(map(int, sections[0].split(',')))

    boards = []
    for section in sections[1:]:
        board = []
        for line in section.strip().split('\n'):
            row = list(map(int, line.split()))
            board.append(row)
        boards.append(board)

    marked = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]
    won = [False] * len(boards)

    def check_win(board_idx):
        for i in range(5):
            if all(marked[board_idx][i][j] for j in range(5)):
                return True
            if all(marked[board_idx][j][i] for j in range(5)):
                return True
        return False

    def calculate_score(board_idx, last_number):
        total = 0
        for i in range(5):
            for j in range(5):
                if not marked[board_idx][i][j]:
                    total += boards[board_idx][i][j]
        return total * last_number

    last_winning_score = None

    for num in numbers:
        for b_idx, board in enumerate(boards):
            if won[b_idx]:
                continue
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        marked[b_idx][i][j] = True

        for b_idx in range(len(boards)):
            if not won[b_idx] and check_win(b_idx):
                won[b_idx] = True
                last_winning_score = calculate_score(b_idx, num)

    answer = last_winning_score
    print(f"Last winning score: {answer}")
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
