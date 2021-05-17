class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self, mass, amount_cm):
        return self._length*self._width*mass*amount_cm


road_1 = Road(20, 5000)
print(road_1.asphalt_mass(25, 5), "kg")
