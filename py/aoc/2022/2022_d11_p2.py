from aoc.helper import AOC


@AOC.puzzle(2022, 11, 2)
def solve():
    data = AOC.get_data()

#     data = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
#
# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0
#
# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
#
# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""

    monkeys = []
    for monkey_block in data.strip().split('\n\n'):
        lines = monkey_block.strip().split('\n')

        items_line = lines[1].split(': ')[1]
        items = [int(x) for x in items_line.split(', ')]

        op_line = lines[2].split('= ')[1]

        divisor = int(lines[3].split('by ')[1])
        true_target = int(lines[4].split('monkey ')[1])
        false_target = int(lines[5].split('monkey ')[1])

        monkeys.append({
            'items': items,
            'operation': op_line,
            'divisor': divisor,
            'true_target': true_target,
            'false_target': false_target,
            'inspections': 0
        })

    lcm = 1
    for monkey in monkeys:
        lcm *= monkey['divisor']

    for round_num in range(10000):
        for monkey in monkeys:
            while monkey['items']:
                monkey['inspections'] += 1
                old = monkey['items'].pop(0)

                new = eval(monkey['operation'])
                new = new % lcm

                if new % monkey['divisor'] == 0:
                    monkeys[monkey['true_target']]['items'].append(new)
                else:
                    monkeys[monkey['false_target']]['items'].append(new)

    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    result = inspections[0] * inspections[1]

    print(result)


if __name__ == "__main__":
    solve()
