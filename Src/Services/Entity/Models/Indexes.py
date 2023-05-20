class Indexed:
    def __init__(self, name, sourceName, indexType):
        self._indexType = indexType
        self._sourceName = sourceName
        self._name = name

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def SourceName(self):
        return self._sourceName

    @SourceName.setter
    def SourceName(self, value):
        self._sourceName = value

    @property
    def IndexType(self):
        return self._indexType

    @IndexType.setter
    def IndexType(self, value):
        self._indexType = value
