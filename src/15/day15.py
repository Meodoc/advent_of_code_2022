from aocd.models import Puzzle

import re
from collections import namedtuple
from tqdm import tqdm


Sensor = namedtuple('Sensor', ['x', 'y', 'closest_beacon'])


def manhattan_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def line_slice(s: Sensor, dist: int, target_y: int) -> list[tuple[int, int]]:
    dx = dist - abs(s.y - target_y)
    return [(x, target_y) for x in range(s.x-dx, s.x+dx+1)] if dx >= 0 else []


def perimeter(s: Sensor, dist: int, outside=False) -> set[tuple[int, int]]:
    i = 2 if outside else 1
    points = {(s.x+dx, s.y+dy) for dx, dy in zip(range(dist+i), reversed(range(dist+i)))}
    points.update([(s.x-abs(x-s.x), y) for x, y in points])
    points.update([(x, s.y-abs(y-s.y)) for x, y in points])
    return points


def calc_sensor_dists(sensors: set[Sensor]) -> dict[tuple[int, int], int]:
    sensor_dists = {}
    for s in sensors:
        bx, by = s.closest_beacon
        dist = manhattan_dist(s.x, s.y, bx, by)
        sensor_dists[s] = dist
    return sensor_dists


def part_a(sensors: set[Sensor], beacons: set[tuple[int, int]]) -> int:
    sensor_dists = calc_sensor_dists(sensors)
    occ = set([(s.x, s.y) for s in sensors]) | beacons

    target_y = 2_000_000
    no_beacon = set()
    for s, dist in tqdm(sensor_dists.items()):
        no_beacon.update([(x, y) for x, y in line_slice(s, dist, target_y) if (x, y) not in occ])
    return len(no_beacon)


def part_b(sensors: set[Sensor], beacons: set[tuple[int, int]]) -> int:
    sensor_dists = calc_sensor_dists(sensors)
    occ = set([(s.x, s.y) for s in sensors]) | beacons

    viable_range = range(4_000_000 + 1)

    for s, dist in tqdm(sensor_dists.items()):
        for px, py in tqdm(perimeter(s.x, s.y, dist, outside=True)):
            if (px, py) in occ or px not in viable_range or py not in viable_range:
                continue
            if all(manhattan_dist(s.x, s.y, px, py) > dist for s, dist in sensor_dists.items()):
                return px * (viable_range.stop-1) + py


def load(data: str) -> tuple[set[Sensor], set[tuple[int, int]]]:
    match = 'Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)'
    sensors, beacons = set(), set()
    for line in data.splitlines():
        sx, sy, bx, by = [int(p) for p in re.findall(match, line)[0]]
        sensors.add(Sensor(sx, sy, (bx, by)))
        beacons.add((bx, by))
    return sensors, beacons


if __name__ == '__main__':
    p = Puzzle(day=15, year=2022)
    ans_a = part_a(*load(p.input_data))
    p.answer_a = ans_a  # 4886370
    ans_b = part_b(*load(p.input_data))
    p.answer_b = ans_b  # 11374534948438
