from itertools import permutations
from brudforce.data import get_road
from math import factorial

from settings import points_count

Home = 0
def get_distance(distances):
    lst = range(1, points_count)
    roads = []
    shortest_road = Ellipsis
    all_ways = list(permutations(lst))
    index = 0
    while index <= len(all_ways):
        current_location = Home
        total_distance = 0
        for step, item in enumerate(all_ways[index-1]):
            total_distance += distances[current_location][item]
            if total_distance > shortest_road:
                index += factorial(len(all_ways[index-1]) - step - 1)
                break
            current_location = item
        total_distance += distances[current_location][Home]  # back to home
        if total_distance < shortest_road:
            shortest_road = total_distance

        roads.append( total_distance )
        index += 1
    return min(roads)
