"""
Utility functions to aid knn
"""

from random import choices, randint
from math import sqrt
from numpy import arange, random, insert
from Point import Point


def cir(cx, cy, radius, training_size, id=-1):
    """
    Returns a list, length training_size, of points with the circle described by the center (cx, cy) with a radius radius.
    
    (x - cx)**2 + (y-cy)**2 <= radius**2

    Params:
        cx: the x coordinate of the circle
        cy: the y coordinate of the circle
        radius: the radius of the center to find points within
        training_size: the number of points to create
        id: the group the points will belong to
    """
    randxs = [x for x in choices(arange(cx-radius, cx+radius, 0.1), k=training_size) if x >= 0]
    randys = [random.choice(insert(arange(cy-sqrt(radius**2 - (x-cx)**2), cy+sqrt(radius**2 - (x-cx)**2), 0.1), 0, cy)) for x in randxs]
    points = [Point([randxs[n], randys[n]], id) for n in range(training_size)]
    return points

def max_value(lis, point):
    """
    Returns the point in lis that is the furthest from point

    Params:
        lis: the list of points
        point: the point to check distance to

    Returns:
        the point with the greatest distance to point
    """
    print("\nPoint:",point)
    max_value = 0
    max_index = len(lis)
    values = [point.distance_to(p) for p in lis]
    return lis[values.index(max(values))]

def set_count(distances, id_types):
    """
    Gets the id that is shared with the most amount of points in distances

    Params:
        distances: the list to get the frequency of id in
        sets_num: the number of different ids
    """
    set_count = [0 for i in range(id_types+1)]
    for p in distances:
        set_count[p.id] += 1
    set_id = set_count.index(max(set_count))
    return set_id

def id_count(points):
    """
    Counts the number of unique ids in a list of points

    Params:
        points: the list of points to get the number of unique ids from

    Returns:
        the number of unique ids in a list of points
    """
    count = 0
    ids = []
    for p in points:
        if p.id not in ids:
            ids += p.id
    return len(ids)
