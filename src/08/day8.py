from aocd.models import Puzzle

import numpy as np


def takewhile_plus_one(pred, iter):
    for i in iter:
        yield i 
        if not pred(i):
            break


def part_a(trees: np.ndarray) -> int:
    size_y, size_x = trees.shape
    n_visible = 0

    for y in range(size_y):
        for x in range(size_x):
            if all(trees[y,x] > trees[y,i] for i in range(x)) or \
                    all(trees[y,x] > trees[y,i] for i in range(x+1, size_x)) or \
                    all(trees[y,x] > trees[i,x] for i in range(y)) or \
                    all(trees[y,x] > trees[i,x] for i in range(y+1, size_y)):
                n_visible += 1
    
    return n_visible


def part_b(trees: np.ndarray) -> int:
    size_y, size_x = trees.shape
    max_score = 0

    for y in range(1, size_y - 1):
        for x in range(1, size_x - 1):
            score = len(list(takewhile_plus_one(lambda i: trees[y,x] > trees[y,i], reversed(range(x))))) * \
                        len(list(takewhile_plus_one(lambda i: trees[y,x] > trees[y,i], range(x+1, size_x)))) * \
                        len(list(takewhile_plus_one(lambda i: trees[y,x] > trees[i,x], reversed(range(y))))) * \
                        len(list(takewhile_plus_one(lambda i: trees[y,x] > trees[i,x], range(y+1, size_y))))
            max_score = max(score, max_score)

    return max_score


def load(data: str) -> np.ndarray:
    return np.array([list(map(int, trees)) for trees in data.splitlines()])


if __name__ == '__main__':
    p = Puzzle(day=8, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 1827
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 335580
