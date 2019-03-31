
class Point:

    def __init__(self, coord, id=-1):
        """
        Constructor for a point
        """
        self.coords = coord
        self.id = id 

    def distance_to(self, point):
        sum = 0
        for dim in range(max(len(self.coords), len(point.coords))):
            if dim >= len(self.get_coords()):
                sum += point.coords[dim]**2
            elif dim >= len(point.get_coords()):
                sum += self.coords[dim]**2
            else:
                sum += (self.coords[dim]-point.coords[dim])**2
        return sum**.5

    def set_id(self, id):
        self.id = id

    def get_coords(self):
        return self.coords

    def __repr__(self):
        return "("+str(self.coords[0])+", "+str(self.coords[1])+", "+str(self.id)+")"