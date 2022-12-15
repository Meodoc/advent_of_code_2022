from aocd.models import Puzzle

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


SAND_SPAWN = (500, 0)


def step(spos: tuple[int, int], occ: set[tuple[int, int]]) -> tuple[int, int]:
    xs, ys = spos
    mov_seq = [(xs, ys+1), (xs-1, ys+1), (xs+1, ys+1)]
    return next(((x, y) for x, y in mov_seq if (x, y) not in occ), spos)


def simulate(occ: set[tuple[int, int]], stop: Callable[[int, int], bool]) -> set[tuple[int, int]]:
    while True:
        spos = SAND_SPAWN
        while True:
            nxt = step(spos, occ)
            if stop(nxt):
                return occ
            if nxt == spos:
                break
            spos = nxt
        occ.add(spos)


def solve(rocks: set[tuple[int, int]], stop: Callable[[int, int], bool], add_bottom=False, plot=False):
    if add_bottom:
        # add 'infinite' bottom
        inf = 200
        by = max(y for _, y in rocks) + 2
        bxs = range(min(x for x, _ in rocks) - inf, max(x for x, _ in rocks) + inf)
        bys = [by] * len(bxs)
        rocks.update(zip(bxs, bys))

    occ = simulate(occ=rocks.copy(), stop=stop)
    sand = occ - rocks
    if plot:
        plot_cave(rocks, sand)
    return len(sand)


def part_a(rocks: set[tuple[int, int]]) -> int:
    max_y = max(y for _, y in rocks)
    return solve(rocks, stop=lambda spos: spos[1] >= max_y)


def part_b(rocks: set[tuple[int, int]]) -> int:
    return solve(rocks, stop=lambda spos: spos == SAND_SPAWN, add_bottom=True) + 1


def load(data: str) -> set[tuple[int, int]]:
    rocks = set()
    for path in data.splitlines():
        lps = path.split(' -> ')
        for p1, p2 in zip(lps, lps[1:]):
            x1, y1, x2, y2 = [int(p) for p in p1.split(',') + p2.split(',')]
            if x1 == x2:
                ys = range(min(y1,y2), max(y1,y2) + 1)
                xs = [x1] * len(ys)
            else:
                xs = range(min(x1,x2), max(x1,x2) + 1)
                ys = [y1] * len(xs)
            rocks.update(zip(xs, ys))
    return rocks


def plot_cave(rocks: set[tuple[int, int]], sand: set[tuple[int, int]]):
    occ = rocks | sand
    minx, maxx = min(x for x, _ in occ), max(x for x, _ in occ)
    miny, maxy = min(y for _, y in occ), max(y for _, y in occ)

    xlen = maxx - minx + 1
    ylen = maxy - miny + 1

    vis = np.zeros((ylen, xlen))
    for r in rocks:
        x, y = r[0] - minx, r[1] - miny
        vis[y, x] = 1
    
    for s in sand:
        x, y = s[0] - minx, s[1] - miny
        vis[y, x] = 2
    
    plt.imshow(vis)
    plt.show()


if __name__ == '__main__':
    p = Puzzle(day=14, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 873
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 24813
