from aocd.models import Puzzle

import numpy as np
import matplotlib.pyplot as plt

from itertools import count
from typing import Iterator


CRT_WIDTH, CRT_HEIGHT = 40, 6


def set_sprite_pos(X: int) -> range:
    return range(X-1, X+2)


def solve(instructions: Iterator[tuple[str, int]], show_CRT: bool) -> int:
    X = 1
    CRT, signal_strenghts = [], []
    instr = next(instructions)
    sprite = set_sprite_pos(X)

    addx_prev = False

    for cycle in count(start=1):      
        if not instr:
            break

        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strenghts.append(cycle * X)

        CRT.append((cycle-1) % CRT_WIDTH in sprite)

        name = instr[0]
        if name == 'noop':
            instr = next(instructions)
        elif name == 'addx':
            if addx_prev:
                X += instr[1]
                instr = next(instructions)
                sprite = set_sprite_pos(X)
                addx_prev = False
            else:
                addx_prev = True
            
    if show_CRT:
        plt.imshow(np.array(CRT).reshape((CRT_HEIGHT, CRT_WIDTH)))
        plt.show()

    return sum(signal_strenghts)


def load(data: str) -> Iterator[tuple[str, int]]:
    for instr in data.splitlines():
        if len(instr.split()) == 2:
            name, val = instr.split()
            yield name, int(val)
        else:
            yield instr,
    yield None


if __name__ == '__main__':
    p = Puzzle(day=10, year=2022)
    ans_a = solve(load(p.input_data), show_CRT=True)
    p.answer_a = ans_a  # 14160
    ans_b = 'RJERPEFC'
    p.answer_b = ans_b  # RJERPEFC