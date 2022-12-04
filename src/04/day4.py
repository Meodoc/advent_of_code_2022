from aocd.models import Puzzle


def part_a(pairs: list[tuple[set, set]]) -> int:
    n_overlap = 0

    for section_1, section_2 in pairs:
        if section_1.issubset(section_2) or section_2.issubset(section_1):
            n_overlap += 1
    
    return n_overlap


def part_b(pairs: list[tuple[set, set]]) -> int:
    n_overlap = 0

    for section_1, section_2 in pairs:
        if len(section_1 & section_2) > 0:
            n_overlap += 1
    
    return n_overlap


def load(data: str) -> list[tuple[set, set]]:
    pairs = []
    
    for pair in data.splitlines():
        elf_1, elf_2 = pair.split(',')
        sections_1 = range(int(elf_1.split('-')[0]), int(elf_1.split('-')[1]) + 1)
        sections_2 = range(int(elf_2.split('-')[0]), int(elf_2.split('-')[1]) + 1)
        pairs.append((set(sections_1), set(sections_2)))

    return pairs

if __name__ == '__main__':
    p = Puzzle(day=4, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 424
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 804