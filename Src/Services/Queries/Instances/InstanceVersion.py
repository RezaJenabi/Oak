from Src.Infrastructure.BaseClasses.Request import Request
from Src.Infrastructure.BaseClasses.Response import Response


class InstanceVersionRequest(Request):

    _serverName = None
    _serverAuthenticationType = None
    _password = None
    _login = None

    def __init__(self, serverName, serverAuthenticationType, login, password):
        self.Login = login
        self.Password = password
        self.ServerAuthenticationType = serverAuthenticationType
        self.ServerName = serverName

    @property
    def Login(self):
        return self._login

    @Login.setter
    def Login(self, value):
        self._login = value

    @property
    def Password(self):
        return self._password

    @Password.setter
    def Password(self, value):
        self._password = value

    @property
    def ServerAuthenticationType(self):
        return self._serverAuthenticationType

    @ServerAuthenticationType.setter
    def ServerAuthenticationType(self, value):
        self._serverAuthenticationType = value

    @property
    def ServerName(self):
        return self._serverName

    @ServerName.setter
    def ServerName(self, value):
        self._serverName = value


class InstanceVersionResponse(Response):

    _version = None

    @property
    def Version(self):
        return self._version

    @Version.setter
    def Version(self, value):
        self._version = value
