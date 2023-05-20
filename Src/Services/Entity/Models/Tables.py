class Tables:
    def __init__(self, name):
        self._name = name

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value


