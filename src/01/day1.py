from aocd.models import Puzzle

import numpy as np


def part_a(data):
    return max(data)


def part_b(data):
    return sum(sorted(data)[-3:])


def load(data):
    return [sum(int(food) for food in foods.splitlines()) for foods in data.split('\n\n')]


if __name__ == '__main__':
    p = Puzzle(day=1, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b
