from aocd.models import Puzzle


TOTAL_DISC_SPACE = 70_000_000
NEEDED_UNUSED_DISC_SPACE = 30_000_000


def all_dirs(dir: dict) -> list[dict]:
    dirs = [dir]
    for val in dir.values():
        if isinstance(val, dict):
            dirs.extend(all_dirs(val))
    return dirs


def dir_size(dir: dict) -> int:
    return sum(val if isinstance(val, int) else dir_size(val) for val in dir.values())


def part_a(root: dict) -> int:
    sum = 0
    for dir in all_dirs(root):
        size = dir_size(dir)
        if size <= 100_000:
            sum += size
    return sum


def part_b(root: dict) -> int:
    used = dir_size(root)
    unused = TOTAL_DISC_SPACE - used
    to_free = NEEDED_UNUSED_DISC_SPACE - unused

    dir_sizes = sorted(dir_size(dir) for dir in all_dirs(root))

    for size in dir_sizes:
        if size > to_free:
            return size


def load(data: str) -> dict:
    root = {'/': {}}

    cur, prev = root, []

    for line in data.splitlines():
        if line.startswith('$ ls'):
            continue
        elif line.startswith('$ cd'):
            dname = line.split()[2]
            if dname == '..':
                cur = prev.pop()
            else:
                prev.append(cur)
                cur = cur[dname]
        else:
            fsize, name = line.split()
            cur[name] = {} if line.startswith('dir') else int(fsize)
            
    return root
    

if __name__ == '__main__':
    p = Puzzle(day=7, year=2022)
    ans_a = part_a(load(p.input_data))
    p.answer_a = ans_a  # 1583951
    ans_b = part_b(load(p.input_data))
    p.answer_b = ans_b  # 214171