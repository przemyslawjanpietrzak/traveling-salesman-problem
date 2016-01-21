from get_distances import get_distances_from_points

Home = 0
def get_road(input, distances):
    current_location = Home
    total_distance = 0
    for item in input:
        total_distance += distances[current_location][item]
        current_location = item
    total_distance += distances[current_location][Home]  # back to home
    return total_distance

