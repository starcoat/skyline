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
    closest_distance = False
    
    for c in corners:
        dist = calc_distance(c)
        if (not closest_distance) or (dist < closest_distance):
            closest_distance = dist
    
    return closest_distance


def max_height(distance: float) -> int:
    return 100 + math.floor(distance) // 100


for b in buildings:
    print(max_height(closest_corner_distance(b)))