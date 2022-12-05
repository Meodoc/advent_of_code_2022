from aocd.models import Puzzle

import re
from collections import namedtuple


Move = namedtuple('Move', ('n', 'fr', 'to'))


def part_a(stacks: dict[int, list[str]], moves: list[Move]):
    for move in moves:
        for _ in range(move.n):
            stacks[move.to].append(stacks[move.fr].pop())

    return ''.join(stack[-1] for stack in stacks.values())


def part_b(stacks: dict[int, list[str]], moves: list[Move]):
    for move in moves:
        stacks[move.to].extend(stacks[move.fr][-move.n:])
        del stacks[move.fr][-move.n:]
    
    return ''.join(stack[-1] for stack in stacks.values())


def load(data: str) -> tuple[dict[int, list[str]], list[Move]]:
    crates, moves = data.split('\n\n')

    crate_rows = crates.splitlines()
    width, height, step = len(crate_rows[0]), len(crate_rows) - 1, 4

    stacks = {}
    for i, w in enumerate(range(1, width, step), 1):
        stack = [crate_rows[h][w] for h in reversed(range(height)) if crate_rows[h][w] != ' ']
        stacks[i] = stack

    moves_ = []
    for move in moves.splitlines():
        n, fr, to = re.findall('move (\d+) from (\d+) to (\d+)', move)[0]
        moves_.append(Move(int(n), int(fr), int(to)))

    return stacks, moves_

if __name__ == '__main__':
    p = Puzzle(day=5, year=2022)
    ans_a = part_a(*load(p.input_data))
    p.answer_a = ans_a  # VJSFHWGFT
    ans_b = part_b(*load(p.input_data))
    p.answer_b = ans_b  # LCTQFBVZV
