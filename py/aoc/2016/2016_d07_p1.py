from aoc.helper import AOC
import re


@AOC.puzzle(2016, 7, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """abba[mnop]qrst
# abcd[bddb]xyyx
# aaaa[qwer]tyui
# ioxxoj[asdfgh]zxcvbn""".strip().splitlines()

    def has_abba(s):
        for i in range(len(s) - 3):
            if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
                return True
        return False

    def supports_tls(ip):
        hypernet_sequences = re.findall(r'\[([^\]]+)\]', ip)
        supernet_sequences = re.split(r'\[[^\]]+\]', ip)

        for hypernet in hypernet_sequences:
            if has_abba(hypernet):
                return False

        for supernet in supernet_sequences:
            if has_abba(supernet):
                return True

        return False

    count = sum(1 for ip in data if supports_tls(ip))

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
