from aoc.helper import AOC
import json
import math

@AOC.puzzle(2021, 18, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()

    def explode(num):
        s = json.dumps(num)
        depth = 0
        for i, c in enumerate(s):
            if c == '[':
                depth += 1
                if depth > 4:
                    j = i
                    while s[j] != ']':
                        j += 1
                    pair = json.loads(s[i:j+1])
                    left_val, right_val = pair[0], pair[1]

                    left_part = s[:i]
                    right_part = s[j+1:]

                    left_num_pos = -1
                    for k in range(len(left_part)-1, -1, -1):
                        if left_part[k].isdigit():
                            end = k + 1
                            start = k
                            while start > 0 and left_part[start-1].isdigit():
                                start -= 1
                            left_num = int(left_part[start:end])
                            left_part = left_part[:start] + str(left_num + left_val) + left_part[end:]
                            break

                    right_num_pos = -1
                    for k in range(len(right_part)):
                        if right_part[k].isdigit():
                            start = k
                            end = k + 1
                            while end < len(right_part) and right_part[end].isdigit():
                                end += 1
                            right_num = int(right_part[start:end])
                            right_part = right_part[:start] + str(right_num + right_val) + right_part[end:]
                            break

                    s = left_part + '0' + right_part
                    return json.loads(s), True
            elif c == ']':
                depth -= 1
        return num, False

    def split(num):
        s = json.dumps(num)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                n = int(s[i:j])
                if n >= 10:
                    left = n // 2
                    right = math.ceil(n / 2)
                    s = s[:i] + f'[{left},{right}]' + s[j:]
                    return json.loads(s), True
                i = j
            else:
                i += 1
        return num, False

    def reduce(num):
        while True:
            num, exploded = explode(num)
            if exploded:
                continue
            num, splitted = split(num)
            if not splitted:
                break
        return num

    def add(a, b):
        return reduce([a, b])

    def magnitude(num):
        if isinstance(num, int):
            return num
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

    numbers = [json.loads(line) for line in data]
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = add(result, numbers[i])

    answer = magnitude(result)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
