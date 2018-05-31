import numpy


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Centroid(Point):
    def __init__(self, points, x=0.0, y=0.0, move=True):
        super().__init__(x, y)
        self.move = move
        if points is None:
            self.points = []
        else:
            self.points = points


class Plane:
    def __init__(self, old, new, points):
        if old is None:
            self.old = []
        else:
            self.old = old

        if new is None:
            self.new = []
        else:
            self.new = new

        if points is None:
            self.points = []
        else:
            self.points = points
