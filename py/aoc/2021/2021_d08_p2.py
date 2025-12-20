from aoc.helper import AOC

@AOC.puzzle(2021, 8, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     sample_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

#     data = sample_data.splitlines()

    def decode_line(line):
        parts = line.split(" | ")
        patterns = parts[0].split()
        output_values = parts[1].split()

        patterns_by_len = {}
        for p in patterns:
            length = len(p)
            if length not in patterns_by_len:
                patterns_by_len[length] = []
            patterns_by_len[length].append(set(p))

        one = patterns_by_len[2][0]
        four = patterns_by_len[4][0]
        seven = patterns_by_len[3][0]
        eight = patterns_by_len[7][0]

        len6 = patterns_by_len[6]
        zero = None
        six = None
        nine = None
        for p in len6:
            if not one.issubset(p):
                six = p
            elif four.issubset(p):
                nine = p
            else:
                zero = p

        len5 = patterns_by_len[5]
        two = None
        three = None
        five = None
        for p in len5:
            if one.issubset(p):
                three = p
            elif p.issubset(six):
                five = p
            else:
                two = p

        digit_map = {
            frozenset(zero): '0',
            frozenset(one): '1',
            frozenset(two): '2',
            frozenset(three): '3',
            frozenset(four): '4',
            frozenset(five): '5',
            frozenset(six): '6',
            frozenset(seven): '7',
            frozenset(eight): '8',
            frozenset(nine): '9'
        }

        result = ''
        for output in output_values:
            result += digit_map[frozenset(output)]

        return int(result)

    total = sum(decode_line(line) for line in data)

    answer = total
    print(f"Answer: {answer}")

if __name__ == "__main__":
    solve()
