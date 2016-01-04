def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

def get_road(distances):
    Home = 0
    visited_places = [Home]
    current_location = Home
    total_distance = 0
    for item in range(len(distances)-1):
        visited_roads = [distances[current_location][i] for i in visited_places]
        nearest_place = min(diff(distances[current_location], visited_roads))
        nearest_place_index = distances[current_location].index(nearest_place)
        visited_places.append(nearest_place_index)
        total_distance += distances[current_location][nearest_place_index] #  min instead of item
        current_location = nearest_place_index
    total_distance += distances[current_location][Home] #  back to home
    return total_distance
