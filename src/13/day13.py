from aocd.models import Puzzle

from typing import Union
from math import prod
from functools import cmp_to_key


def compare_packets(left: Union[int, list[int]], right: Union[int, list[int]]) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right 

    if isinstance(left, list) ^ isinstance(right, list):
        left = left if isinstance(left, list) else [left]
        right = right if isinstance(right, list) else [right]
    
    for e1, e2 in zip(left, right):
        c = compare_packets(e1, e2)
        if c:
            return c

    return len(left) - len(right)


def part_a(pairs: list[tuple[list[int], list[int]]]) -> int:
    return sum(i for i, (left, right) in enumerate(pairs, 1) if compare_packets(left, right) < 0)


def part_b(packets: list[list[int]]) -> int:
    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)
    packets.sort(key=cmp_to_key(compare_packets))
    return prod(i for i, packet in enumerate(packets, 1) if packet in divider_packets)


def load(data: str, ignore_blanks=False) -> Union[list[tuple[list[int], list[int]]], list[list[int]]]:
    if ignore_blanks:
        data = data.replace('\n\n', '\n')
        return [eval(packet) for packet in data.splitlines()]

    pairs = []   
    for pair in data.split('\n\n'):
        left, right = pair.splitlines()
        pairs.append((eval(left), eval(right)))
    return pairs


if __name__ == '__main__':
    p = Puzzle(day=13, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 6415
    ans_b = part_b(load(p.input_data, ignore_blanks=True))
    p.answer_b = ans_b  # 20056
