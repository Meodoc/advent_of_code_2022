from aocd.models import Puzzle


def move_head(dir: str, head: tuple[int, int]):
    x, y = head
    if dir == 'L':
        return (x-1, y)
    if dir == 'R':
        return (x+1, y)
    if dir == 'U':
        return (x, y+1)
    if dir == 'D':
        return (x, y-1)


def move_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail

    # tail is overlapping or adjacent with head
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return tail

    if hx == tx:
        return (tx, ty + (1 if hy > ty else -1))
    if hy == ty:
        return (tx + (1 if hx > tx else -1), ty)

    return (tx + (1 if hx > tx else -1), ty + (1 if hy > ty else -1))


def solve(instructions: list[tuple[str, int]], n_knots: int) -> int:
    knots = [(0,0)] * n_knots
    visited = set()

    for d, steps in instructions:
        for _ in range(steps):
            knots[0] = move_head(d, knots[0])
            for i in range(n_knots - 1):
                knots[i+1] = move_tail(knots[i], knots[i+1])
            visited.add(knots[-1])
    
    return len(visited)


def load(data: str) -> list[tuple[str, int]]:
    return [(instr.split()[0], int(instr.split()[1])) for instr in data.splitlines()]


if __name__ == '__main__':
    p = Puzzle(day=9, year=2022)
    ans_a = solve(load(p.input_data), n_knots=2)
    p.answer_a = ans_a  # 6087
    ans_b = solve(load(p.input_data), n_knots=10)
    p.answer_b = ans_b  # 2493
