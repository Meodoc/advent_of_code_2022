from aocd.models import Puzzle


def solve(buffers: list[str], w_size: int) -> int:
    for buffer in buffers:
        for i in range(len(buffer) - w_size + 1):
            w = buffer[i:i+w_size]
            if len(w) == len(set(w)):
                return i + w_size


def load(data: str) -> list[str]:
    return data.splitlines()


if __name__ == '__main__':
    p = Puzzle(day=6, year=2022)
    ans_a = solve(load(p.input_data), w_size=4)
    print(ans_a)
    p.answer_a = ans_a  # 1544
    ans_b = solve(load(p.input_data), w_size=14)
    print(ans_b)
    p.answer_b = ans_b  # 2145