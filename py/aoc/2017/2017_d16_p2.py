from aoc.helper import AOC

@AOC.puzzle(2017, 16, 2)
def solve():
    data = AOC.get_data().strip()

    programs = list("abcdefghijklmnop")
    initial = programs[:]

    moves = data.split(',')

    def dance(programs):
        programs = programs[:]
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
        return programs

    seen = {}
    iteration = 0
    target = 1000000000

    while iteration < target:
        state = ''.join(programs)
        if state in seen:
            cycle_length = iteration - seen[state]
            remaining = target - iteration
            remainder = remaining % cycle_length
            for _ in range(remainder):
                programs = dance(programs)
            break
        seen[state] = iteration
        programs = dance(programs)
        iteration += 1

    answer = ''.join(programs)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
