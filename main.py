import time

from brudforce.tsp import get_distance as brudforce
from najblizszy_sasiad.tsp import get_distance as najblizszy_sasiad

from multi_fragment.tsp import get_distance as multi_fragment

from get_distances import get_distances_from_points
import pprint

distances = get_distances_from_points()
pprint.pprint(distances)


start_time = time.time()
x = multi_fragment(distances)
print("multi_fragment --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
y = najblizszy_sasiad(distances)
print("najblizszy_sasiad --- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
z = brudforce(distances)
print("brudforce --- %s seconds ---" % (time.time() - start_time))


print('multi_fragment', x)
print('najblizszy_sasiad', y)
print('brudforce', z)
