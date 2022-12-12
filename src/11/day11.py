from aocd.models import Puzzle

from math import prod, lcm
from collections import namedtuple


Monkey = namedtuple('Monkey', ['n', 'items', 'operation', 'test', 'monkey_true', 'monkey_false'])


def solve(monkeys: list[Monkey], rounds: int, div: int = 1, mod: int = None) -> int:
    n_inspected = [0] * len(monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            n_inspected[monkey.n] += len(monkey.items)
            for item in monkey.items:
                item = eval(monkey.operation.replace('old', f'{item}'))

                item //= div
                if mod: 
                    item %= mod

                target = monkey.monkey_true if item % monkey.test == 0 else monkey.monkey_false
                monkeys[target].items.append(item)

            monkey.items.clear()

    return prod(sorted(n_inspected)[-2:])


def part_a(monkeys: list[Monkey]) -> int:
    return solve(monkeys, div=3, rounds=20)


def part_b(monkeys: list[Monkey]) -> int:
    m = lcm(*[monkey.test for monkey in monkeys])
    return solve(monkeys, mod=m, rounds=10_000)


def load(data: str) -> list[Monkey]:
    monkeys = []
    for monkey in data.split('\n\n'):
        n, items, operation, test, monkey_true, monkey_false = monkey.splitlines()
        n = int(n.split()[1][:-1])
        items = [int(item) for item in items.split(':')[1].split(',')]
        operation = operation.split('=')[1]
        test = int(test.split()[-1])
        monkey_true = int(monkey_true.split()[-1])
        monkey_false = int(monkey_false.split()[-1])
        monkeys.append(Monkey(n, items, operation, test, monkey_true, monkey_false))
    return monkeys


if __name__ == '__main__':
    p = Puzzle(day=11, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 56595
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 15693274740
