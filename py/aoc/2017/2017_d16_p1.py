from aoc.helper import AOC

@AOC.puzzle(2017, 16, 1)
def solve():
    data = AOC.get_data().strip()

    programs = list("abcdefghijklmnop")

    moves = data.split(',')

    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]
        elif move[0] == 'x':
            parts = move[1:].split('/')
            a, b = int(parts[0]), int(parts[1])
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'p':
            parts = move[1:].split('/')
            prog_a, prog_b = parts[0], parts[1]
            idx_a = programs.index(prog_a)
            idx_b = programs.index(prog_b)
            programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]

    answer = ''.join(programs)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
