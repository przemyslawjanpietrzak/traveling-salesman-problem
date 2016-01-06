def diff(a, b):
    return [aa for aa in a if aa not in b]


def get_shortest_road(distances, roads_visited_x, roads_visited_y):
    min = 9999999999
    x = 0
    y = 0
    for i, item in enumerate(distances):
        if i in roads_visited_x:
            continue
        for j, item1 in enumerate(item[:i]):
            if j in roads_visited_y:
                continue
            if item1 and item1 < min and not is_hamilton(i, j, roads_visited_x, roads_visited_y):
                min = item1
                x = i
                y = j
    print min
    return {
        'value': min,
        'x': x,
        'y': y
    }

def is_hamilton(road_x, road_y, roads_visited_x, roads_visited_y):
    for item in roads_visited_x + [road_x]:
        if item not in roads_visited_y + [road_y]:
            return False
    return True


def get_road(distances):
    roads_visited_x = []
    roads_visited_y = []
    total_distance = 0
    for i in range(len(distances)-1):
        shortest_road = get_shortest_road(distances, roads_visited_x, roads_visited_y)
        roads_visited_x.append(shortest_road['x'])
        roads_visited_y.append(shortest_road['y'])
        total_distance += shortest_road['value']

    # print roads_visited_x, roads_visited_y, diff(range(len(distances)), roads_visited_x), diff(range(len(distances)), roads_visited_y)
    # shortest_road = get_shortest_road(distances, roads_visited_x, roads_visited_y, allow_hamilton=True)
    # roads_visited_x.append(shortest_road['x'])
    # roads_visited_y.append(shortest_road['y'])
    # total_distance += shortest_road['value']

    last_road_x = diff(range(len(distances)), roads_visited_x)[0]
    last_road_y = diff(range(len(distances)), roads_visited_y)[0]
    last_road_distance = distances[last_road_x][last_road_y]
    total_distance += last_road_distance
    return total_distance
