from aoc.helper import AOC
import hashlib
from collections import deque


@AOC.puzzle(2016, 17, 2)
def solve():
    data = AOC.get_data().strip()
    passcode = data

    def is_open(char):
        return char in 'bcdef'

    def get_open_doors(path):
        hash_input = passcode + path
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()
        doors = []
        if is_open(hash_result[0]):
            doors.append('U')
        if is_open(hash_result[1]):
            doors.append('D')
        if is_open(hash_result[2]):
            doors.append('L')
        if is_open(hash_result[3]):
            doors.append('R')
        return doors

    def find_longest():
        queue = deque([(0, 0, '')])
        longest_path_length = 0

        while queue:
            x, y, path = queue.popleft()

            if x == 3 and y == 3:
                longest_path_length = max(longest_path_length, len(path))
                continue

            open_doors = get_open_doors(path)

            for door in open_doors:
                nx, ny = x, y
                if door == 'U' and y > 0:
                    ny -= 1
                    new_path = path + 'U'
                elif door == 'D' and y < 3:
                    ny += 1
                    new_path = path + 'D'
                elif door == 'L' and x > 0:
                    nx -= 1
                    new_path = path + 'L'
                elif door == 'R' and x < 3:
                    nx += 1
                    new_path = path + 'R'
                else:
                    continue

                queue.append((nx, ny, new_path))

        return longest_path_length

    answer = find_longest()
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
