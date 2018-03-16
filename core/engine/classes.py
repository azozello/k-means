class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0.0
    y = 0.0


class Central(Point):
    def __init__(self, x, y, points):
        super(Point, self).__init__()
        self.x = x
        self.y = y
        self.points = points
    x = 0.0
    y = 0.0
    points = []


class Plane:
    old_centrals = []
    new_centrals = []
    points = []
