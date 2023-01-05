from aocd.models import Puzzle


def trapped(pos: tuple[int], cubes: list[tuple[int]], vrange: list[range]):
    def escaped(cube):
        x, y, z = cube
        return x not in vrange[0] or y not in vrange[1] or z not in vrange[2]

    stack = [pos]
    visited = set()

    while stack:
        cur = stack.pop()

        if escaped(cur):
            return False

        if cur not in visited:
            visited.add(cur)
            stack.extend(neigh for neigh in free_neighs(cur, cubes) if neigh not in visited)

    return True


def free_neighs(cube: tuple[int], cubes: set[tuple[int]]):
    x, y, z = cube
    neighbours = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
    return [neigh for neigh in neighbours if neigh not in cubes]


def solve(cubes: set[list[int]], ignore_trapped_air=False):
    if ignore_trapped_air:
        vrange = [range(min(c[i] for c in cubes), max(c[i] for c in cubes)+1) for i in range(3)]
        trapped_cache = {}

    surface = 0
    for cube in cubes:
        fneighs = free_neighs(cube, cubes)
        if ignore_trapped_air:
            for neigh in fneighs:
                if neigh not in trapped_cache:
                    trapped_cache[neigh] = trapped(neigh, cubes, vrange)
                surface += not trapped_cache[neigh]
        else:
            surface += len(fneighs)
    return surface


def load(data: str):
    return {tuple(int(c) for c in line.split(',')) for line in data.splitlines()}


if __name__ == '__main__':
    p = Puzzle(day=18, year=2022)

    ans_a = solve(load(p.input_data))
    p.answer_a = ans_a  # 2006    
    ans_b = solve(load(p.input_data), ignore_trapped_air=True)
    p.answer_b = ans_b  # 3364
