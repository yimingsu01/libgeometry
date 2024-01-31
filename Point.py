import math
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


    def dist(self, p1, p2):
        return math.sqrt(
            math.pow((p1.x - p2.x), 2) +
            math.pow((p1.y - p2.y), 2)
        )

    def area_of_circle(self, radius):
        return 3.14 * math.pow(radius, 2)

<<<<<<< HEAD
class Square:
    def __init__(self, size):
        self.size = int(size)
=======

>>>>>>> f5bb92d (changed ownership of attributes)

