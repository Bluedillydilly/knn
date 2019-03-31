from random import choices, randint
from math import sqrt
from numpy import arange, random, insert
from Point import Point


def cir(cx, cy, radius, training_size, id=0):
    """
    Returns a list, length training_size, of points with the circle described by the center (cx, cy) with a radius radius.
    
    (x - cx)**2 + (y-cy)**2 = radius**2
    """
    randxs = [x for x in choices(arange(cx-radius, cx+radius, 0.1), k=training_size) if x >= 0]
    randys = [random.choice(insert(arange(cy-sqrt(radius**2 - (x-cx)**2), cy+sqrt(radius**2 - (x-cx)**2), 0.1), 0, cy)) for x in randxs]
    points = []
    for n in range(training_size):
        points.append(Point([randxs[n], randys[n]], id))
    return points

def max_value(lis, point):
    """
    Returns the point in lis that is the furthest from poit
    """
    print("\nPoint:",point)
    max_value = 0
    max_index = len(lis)
    values = [point.distance_to(p) for p in lis]
    return lis[values.index(max(values))]

def set_count(distances, sets_num):
    set_count = []
    for s in range(sets_num+1):
        set_count += [0]
    for p in distances:
        set_count[p.id] += 1
    set_id = set_count.index(max(set_count))
    return set_id