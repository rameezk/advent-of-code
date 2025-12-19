from aoc.helper import AOC

@AOC.puzzle(2017, 21, 1)
def solve():
    data = AOC.get_data().strip()

    sample = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

    def parse_rules(text):
        rules = {}
        for line in text.strip().split('\n'):
            pattern, output = line.split(' => ')
            rules[pattern] = output
        return rules

    def pattern_to_grid(pattern):
        return [list(row) for row in pattern.split('/')]

    def grid_to_pattern(grid):
        return '/'.join([''.join(row) for row in grid])

    def rotate_90(grid):
        n = len(grid)
        return [[grid[n-1-j][i] for j in range(n)] for i in range(n)]

    def flip_horizontal(grid):
        return [row[::-1] for row in grid]

    def get_all_variants(pattern):
        variants = set()
        grid = pattern_to_grid(pattern)

        for _ in range(4):
            variants.add(grid_to_pattern(grid))
            variants.add(grid_to_pattern(flip_horizontal(grid)))
            grid = rotate_90(grid)

        return variants

    def build_rule_dict(rules):
        full_rules = {}
        for pattern, output in rules.items():
            for variant in get_all_variants(pattern):
                full_rules[variant] = output
        return full_rules

    def split_grid(grid, size):
        n = len(grid)
        blocks = []
        for i in range(0, n, size):
            for j in range(0, n, size):
                block = []
                for di in range(size):
                    block.append(grid[i+di][j:j+size])
                blocks.append(block)
        return blocks

    def join_blocks(blocks, old_size):
        n = len(blocks)
        blocks_per_side = int(n ** 0.5)
        new_size = len(blocks[0])
        total_size = blocks_per_side * new_size

        grid = [['' for _ in range(total_size)] for _ in range(total_size)]

        for block_idx, block in enumerate(blocks):
            block_row = block_idx // blocks_per_side
            block_col = block_idx % blocks_per_side

            for i in range(new_size):
                for j in range(new_size):
                    grid[block_row * new_size + i][block_col * new_size + j] = block[i][j]

        return grid

    def enhance(grid, rules):
        size = len(grid)

        if size % 2 == 0:
            block_size = 2
        else:
            block_size = 3

        blocks = split_grid(grid, block_size)
        enhanced_blocks = []

        for block in blocks:
            pattern = grid_to_pattern(block)
            if pattern in rules:
                enhanced_pattern = rules[pattern]
                enhanced_blocks.append(pattern_to_grid(enhanced_pattern))

        return join_blocks(enhanced_blocks, block_size)

    def count_on(grid):
        return sum(row.count('#') for row in grid)

    rules = parse_rules(data)
    full_rules = build_rule_dict(rules)

    grid = pattern_to_grid('.#./..#/###')

    for iteration in range(5):
        grid = enhance(grid, full_rules)

    answer = count_on(grid)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
