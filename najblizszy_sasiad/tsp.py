from najblizszy_sasiad.data import get_road
from get_distances import get_distances_from_points



# distances = [
#     [0, 36, 32, 54, 20,  40],
#     [36, 0, 22, 58, 54, 67],
#     [32, 22, 0, 36, 42, 71],
#     [54, 58, 36, 0, 50, 92],
#     [20, 54, 42, 50, 0, 45],
#     [40, 67, 71, 92, 45, 0]
# ]
def get_distance(distances):
    return get_road(distances)

