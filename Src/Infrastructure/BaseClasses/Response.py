class Response:
    _status: bool = True
    _statusCode: int = 200

    @property
    def Status(self):
        return self._status

    @Status.setter
    def Status(self, value):
        self._status = value

    @property
    def StatusCode(self):
        return self._statusCode

    @StatusCode.setter
    def StatusCode(self, value):
        self._statusCode = value
