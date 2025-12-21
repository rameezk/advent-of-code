from aoc.helper import AOC


@AOC.puzzle(2022, 7, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".strip().splitlines()

    dir_sizes = {}
    current_path = []

    for line in data:
        if line.startswith("$ cd"):
            target = line[5:]
            if target == "/":
                current_path = ["/"]
            elif target == "..":
                current_path.pop()
            else:
                current_path.append(target)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            parts = line.split()
            size = int(parts[0])

            for i in range(len(current_path)):
                path_key = "/".join(current_path[:i+1])
                if path_key not in dir_sizes:
                    dir_sizes[path_key] = 0
                dir_sizes[path_key] += size

    total_space = 70000000
    needed_space = 30000000
    used_space = dir_sizes["/"]
    free_space = total_space - used_space
    space_to_free = needed_space - free_space

    smallest_to_delete = min(size for size in dir_sizes.values() if size >= space_to_free)

    print(smallest_to_delete)
    AOC.submit_answer(smallest_to_delete)


if __name__ == "__main__":
    solve()
