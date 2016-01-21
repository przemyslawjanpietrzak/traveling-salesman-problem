from itertools import permutations
from brudforce.data import get_road

from settings import points_count

def get_distance(distances):
    lst = range(1, points_count)
    roads = []
    for road in list(permutations(lst)):
        roads.append(get_road(road, distances))

    return min(roads)
