class Indexed:
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value