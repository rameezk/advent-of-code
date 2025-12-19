from aoc.helper import AOC


@AOC.puzzle(2016, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2""".splitlines()

    bots = {}
    outputs = {}
    instructions = {}

    for line in data:
        if line.startswith("value"):
            parts = line.split()
            value = int(parts[1])
            bot_num = int(parts[5])
            if bot_num not in bots:
                bots[bot_num] = []
            bots[bot_num].append(value)
        else:
            parts = line.split()
            bot_num = int(parts[1])
            low_type = parts[5]
            low_dest = int(parts[6])
            high_type = parts[10]
            high_dest = int(parts[11])
            instructions[bot_num] = (low_type, low_dest, high_type, high_dest)

    target_bot = None

    while True:
        ready_bot = None
        for bot_num, chips in bots.items():
            if len(chips) == 2:
                ready_bot = bot_num
                break

        if ready_bot is None:
            break

        chips = bots[ready_bot]
        low_val = min(chips)
        high_val = max(chips)

        if (low_val == 17 and high_val == 61):
            target_bot = ready_bot

        bots[ready_bot] = []

        low_type, low_dest, high_type, high_dest = instructions[ready_bot]

        if low_type == "bot":
            if low_dest not in bots:
                bots[low_dest] = []
            bots[low_dest].append(low_val)
        else:
            if low_dest not in outputs:
                outputs[low_dest] = []
            outputs[low_dest].append(low_val)

        if high_type == "bot":
            if high_dest not in bots:
                bots[high_dest] = []
            bots[high_dest].append(high_val)
        else:
            if high_dest not in outputs:
                outputs[high_dest] = []
            outputs[high_dest].append(high_val)

    print(target_bot)
    AOC.submit_answer(target_bot)


if __name__ == "__main__":
    solve()
