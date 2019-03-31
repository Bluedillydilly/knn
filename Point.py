
class Point:

    def __init__(self, coord, id=-1):
        """
        Constructor for a point

        Params:
            coord: the coordinates of the point to be created
            id: a identifier for the group the point belongs to
                defaults to -1
        """
        self.coords = coord
        self.id = id 

    def distance_to(self, point):
        """
        Gets the distance from this point to another new point

        Params:
            point: the point to get the distance to

        Returns:
            float representing the distance from self to point
        """
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
        """
        Sets the id of the point to a new provided one.

        Args:
            id: the new id of the Point object

        """
        self.id = id

    def get_coords(self):
        """
        Gets the coords of the point.

        Returns:
            the list of coordinates of the point, supports n-dimensions
        """
        return self.coords

    def __repr__(self):
        """
        The string representation of the Point

        Returns:
            the coords and id of the point
        """
        str_rep = "(["
        for i in range(len(self.coords)-1):
            str_rep += str(self.coords[i])+", "
        str_rep += str(self.coords[-1])
        str_rep += "], " + str(self.id) + ")"
        return str_rep