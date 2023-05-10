class CreateInstance:

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def calculate_area(self):
        return round(self._side**2, 2)