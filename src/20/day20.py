from aocd.models import Puzzle


def mix(file: list[int], decrypt_key=1, rounds=1) -> int:
    file = [e * decrypt_key for e in file]
    unique = [u for u in enumerate(file)]
    l = len(file)

    for _ in range(rounds):
        for i, e in enumerate(file):
            old_idx = unique.index((i,e))
            insert = (old_idx + e) % (l-1)
            unique.remove((i,e))
            unique.insert(insert, (i,e))

    zero_idx = unique.index((file.index(0), 0))
    return sum(unique[(zero_idx + o) % l][1] for o in [1000, 2000, 3000])


def part_a(file: list[int]) -> int:
    return mix(file)


def part_b(file: list[int]) -> int:
    return mix(file, decrypt_key=811589153, rounds=10)


def load(data: str) -> list[int]:
    return [int(l) for l in data.splitlines()]


if __name__ == '__main__':
    p = Puzzle(day=20, year=2022)

    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 3473
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 7496649006261
