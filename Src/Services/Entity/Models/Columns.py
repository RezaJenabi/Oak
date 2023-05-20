class Columns:
    def __init__(self):
        self._name = None

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def DataType(self):
        return self._dataType

    @DataType.setter
    def DataType(self, value):
        self._dataType = value

    @property
    def Identity(self):
        return self._identity

    @Identity.setter
    def Identity(self, value):
        self._identity = value

    @property
    def PrimaryKey(self):
        return self._primaryKey

    @PrimaryKey.setter
    def PrimaryKey(self, value):
        self._primaryKey = value

