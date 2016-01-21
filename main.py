import time

from brudforce.tsp import get_distance as brudforce
from najblizszy_sasiad.tsp import get_distance as najblizszy_sasiad
from multi_fragment.tsp import get_distance as multi_fragment
from branch_bound.tsp import get_distance as branch_bound

from get_distances import get_distances_from_points

from settings import multi_fragment_on, najblizszy_sasiad_on, branch_bound_on, brudforce_on
import pprint

distances = get_distances_from_points()

pprint.pprint(distances)


if multi_fragment_on:
    start_time = time.time()
    result = multi_fragment(distances)
    print("multi_fragment --- %s seconds ---" % (time.time() - start_time))
    print("mnulti_fragment - distance", result)

if najblizszy_sasiad_on:
    start_time = time.time()
    result = najblizszy_sasiad(distances)
    print("najblizszy_sasiad --- %s seconds ---" % (time.time() - start_time))
    print("najblizszy_sasiad - distance", result)

if brudforce_on:
    start_time = time.time()
    result = brudforce(distances)
    print("brudforce --- %s seconds ---" % (time.time() - start_time))
    print("najblizszy_sasiad - distance", result)

if branch_bound_on:
    start_time = time.time()
    result = branch_bound(distances)
    print("branch_bound --- %s seconds ---" % (time.time() - start_time))
    print("branch_bound - distance", result)
