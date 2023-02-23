from aocd.models import Puzzle

trans = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

trans_rev = {
    4: '-',
    3: '=',
    2: '2',
    1: '1',
    0: '0'
}


def snafu_to_decimal(snafu: str) -> int:
    decimal = 0
    for pow, d in enumerate(reversed(snafu)):
        decimal += 5**pow * trans[d]
    return decimal


def decimal_to_snafu(decimal: int) -> str:
    snafu = ''
    while decimal > 0:
        rem, decimal = decimal % 5, round(decimal / 5)
        snafu += trans_rev[rem]
    return snafu[::-1]


def part_a(snafu: list[str]) -> int:
    decimal_sum = sum(snafu_to_decimal(s) for s in snafu)
    return decimal_to_snafu(decimal_sum)


def load(data: str) -> list[str]:
    return data.splitlines()

if __name__ == '__main__':
    p = Puzzle(day=25, year=2022)
    p.answer_a = part_a(load(p.input_data))  # 20-==01-2-=1-2---1-0
