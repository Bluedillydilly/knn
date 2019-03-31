from util import cir, max_value, set_count
from Point import Point

def main():
    set1 = cir(3, 3, 1, 5, 1)
    set2 = cir(5, 5, 1, 5, 2)
    poi = Point([6,6])
    print("set1:", set1)
    print("set2:", set2)
    print(knn(3, [set1, set2], poi))
    print("Updated point:",poi)

def knn(k, sets, poi):
    """
    Gets the group of points the the point poi should belong to.
    Uses the k-nearest neighbors to get the group

    Params:
        k: the number of numbers to check the id of
        sets: the points to check if poi belongs
        poi: the point of interest

    Returns:
        the id of the group poi should belong to
    """
    # gets the k nearest points to poi from the points in sets
    distances_to_poi = []
    for s in sets:
        for set_p in s:
            if len(distances_to_poi) < k:
                distances_to_poi.append(set_p)
            elif poi.distance_to(set_p) < poi.distance_to(max_value(distances_to_poi, poi)):            
                distances_to_poi.remove(max_value(distances_to_poi, poi))
                distances_to_poi.append(set_p)
            print("Distances:",distances_to_poi)
    set_id = set_count(distances_to_poi, len(sets))
    poi.set_id(set_id)
    return set_id




if __name__ == "__main__":
    main()
    p1 = Point([6,6])
    p2 = Point([2.4,3.6])
    p3 = Point([2.9, 2.6])
    print(p1.distance_to(p2))
    print(p1.distance_to(p3))
