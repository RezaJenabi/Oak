class Request:
    _pageIndex: int = 1
    _pageSize: int = 10

    @property
    def PageIndex(self):
        return self._pageIndex

    @PageIndex.setter
    def PageIndex(self, value):
        self._pageIndex = value

    @property
    def PageSize(self):
        return self._pageSize

    @PageIndex.setter
    def PageSize(self, value):
        self._pageSize = value