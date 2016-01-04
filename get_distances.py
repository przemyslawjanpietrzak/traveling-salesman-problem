import math
from random import randint
from math import sqrt
import pprint

from settings import points_count

pp = pprint.PrettyPrinter()

def _random_points():
    return [(randint(0, 1000000), randint(0, 1000000)) for item in range(points_count)]

def get_distances_from_points():
    points = _random_points()
    # pp.pprint(points)
    distances = []
    for city in points:
        distances.append(
            [sqrt(
                (city[0]-item[0])**2 + (city[1]-item[1])**2
            ) for item in points]
        )
    # pp.pprint(distances)
    return distances

