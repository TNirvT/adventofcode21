import re
from math import comb
from itertools import combinations
from collections import namedtuple

RE_IDX = re.compile(r"(?<=scanner )\d+")
RE_COORD = re.compile(r"(-?\d+),(-?\d+),(-?\d+)")
TWELVE_C_TWO = comb(12, 2)
error_count = 0

def open_file(filename) -> dict:
    scanners = {}
    with open(filename) as f:
        for line in f:
            idx_match = RE_IDX.search(line)
            coord_match = RE_COORD.match(line)
            if idx_match:
                scanner_idx = int(idx_match[0])
                scanners[scanner_idx] = []
            elif coord_match:
                coords = tuple((int(coord_match.group(i)) for i in range(1,4)))
                scanners[scanner_idx].append(coords)
            else:
                pass
        return scanners

def rotate_x(coords: tuple[int, int, int]) -> tuple[int, int, int]:
    # rotate along x, clockwise by pi/2
    # y' = z; z' = -y
    return coords[0], coords[2], -coords[1]

def rotate_y(coords: tuple[int, int, int]) -> tuple[int, int, int]:
    # rotate along y, clockwise by pi/2
    # x' = -z; z' = x
    return -coords[2], coords[1], coords[0]

def rotate_z(coords: tuple[int, int, int]) -> tuple[int, int, int]:
    # rotate along z, clockwise by pi/2
    # x' = y; y' = -x
    return coords[1], -coords[0], coords[2]


def get_distances(beacons: list[tuple]) -> tuple[list[tuple], list[int]]:
    def get_distance(beacon1: tuple, beacon2: tuple) -> int:
        # this function returns distance ** 2, not simple distance
        return sum([(b1_coord - b2_coord) ** 2 for b1_coord, b2_coord in zip(beacon1, beacon2)])

    distances = []
    pairs = list(combinations(beacons, 2))
    for pair in pairs:
        distance = get_distance(pair[0], pair[1])
        distances.append(distance)
    return pairs, distances

def get_commons(beacons1, beacons2):
    commons = []
    pairs1, distances1 = get_distances(beacons1)
    pairs2, distances2 = get_distances(beacons2)
    # set() is unordered!
    common_set = set(distances1).intersection(distances2)

    if len(common_set) < TWELVE_C_TWO:
        global error_count
        error_count += 1
        print(f"No overlapping error! ({error_count})", end="")
        return

    common_pairs1, common_pairs2 = [], []
    for c in common_set:
        common_pairs1.append(pairs1[distances1.index(c)])
        common_pairs2.append(pairs2[distances2.index(c)])
    # print("common_pairs1", common_pairs1)
    # print("common_pairs2", common_pairs2)

    vector_subtract1 = tuple(map(lambda x0, x1: x1 - x0, common_pairs1[0][0], common_pairs1[0][1]))
    Rotation_no = namedtuple("Rotation", "x y z")
    rotation = Rotation_no(0, 0, 0)
    for i in range(4):
        if common_pairs2[0] == common_pairs1[0]:
            return
        rotate_x(common_pairs2[0])
        rotation.x += 1
    # return commons
    return [1]

if __name__ == "__main__":
    # scanners = open_file("aoc19.txt")
    scanners = open_file("test.txt")

    scanner_comobo = combinations(scanners, 2)
    for i, j in scanner_comobo:
        c = get_commons(scanners[i], scanners[j])
        if not c:
            print(f"in scanners {i}, {j}")

