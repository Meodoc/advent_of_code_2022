from aocd.models import Puzzle

from collections import namedtuple


Rucksack = namedtuple('Rucksack', ['compartment_1', 'compartment_2']) 


def priority(item):
    assert item.isascii()
    return ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27
    

def part_a(rucksacks):
    return sum(priority((rucksack.compartment_1 & rucksack.compartment_2).pop()) for rucksack in rucksacks)


def part_b(rucksacks):
    prio_sum = 0

    grouped = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

    for group in grouped:      
        shared, = set.intersection(*[rucksack.compartment_1 | rucksack.compartment_2 for rucksack in group])
        prio_sum += priority(shared)
    
    return prio_sum


def load(data):
    return [Rucksack(set(items[:len(items)//2]), set(items[len(items)//2:])) for items in data.splitlines()]


if __name__ == '__main__':
    p = Puzzle(day=3, year=2022)

    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 7553
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 2758
