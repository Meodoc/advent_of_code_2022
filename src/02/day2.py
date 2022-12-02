from aocd.models import Puzzle

ROCK = 1
PAPER = 2
SISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

scores_a = {
    ('A', 'X'): ROCK + DRAW,
    ('A', 'Y'): PAPER + WIN,
    ('A', 'Z'): SISSORS + LOSE,
    ('B', 'X'): ROCK + LOSE,
    ('B', 'Y'): PAPER + DRAW,
    ('B', 'Z'): SISSORS + WIN,
    ('C', 'X'): ROCK + WIN,
    ('C', 'Y'): PAPER + LOSE,
    ('C', 'Z'): SISSORS + DRAW,
}

scores_b = {
    ('A', 'X'): LOSE + SISSORS,
    ('A', 'Y'): DRAW + ROCK,
    ('A', 'Z'): WIN + PAPER,
    ('B', 'X'): LOSE + ROCK,
    ('B', 'Y'): DRAW + PAPER,
    ('B', 'Z'): WIN + SISSORS,
    ('C', 'X'): LOSE + PAPER,
    ('C', 'Y'): DRAW + SISSORS,
    ('C', 'Z'): WIN + ROCK,
}


def part_a(rounds):
    return sum(scores_a[round] for round in rounds)

def part_b(rounds):
    return sum(scores_b[round] for round in rounds)


def load(data):
    return [tuple(round.split()) for round in data.splitlines()]


if __name__ == '__main__':
    p = Puzzle(day=2, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 8890
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 10238
