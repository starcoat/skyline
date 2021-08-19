import math


buildings = [
    ((-80,100), (-20,100), (-20,160), (-80,160)),
    ((60,160), (120,60), (120,250), (60,250)),
    ((-400,200), (-300,200), (-300,300), (-400,300))
]


def calc_distance(corner: tuple[int, int]) -> int:
    return math.sqrt(pow(corner[0], 2) + pow(corner[1], 2))


# Gibt es eine schönere Alternative für diese Signatur:
# corners: tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]
def closest_corner_distance(corners) -> float:
    return 0


def max_height(distance: float) -> int:
    return 0