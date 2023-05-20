
class Instances:
    def __init__(self, serverName, serverAuthenticationType, login, password, version):
        self._serverName = serverName
        self._serverAuthenticationType = serverAuthenticationType
        self._password = password
        self._login = login
        self._version = version

    @property
    def Version(self):
        return self._version

    @Version.setter
    def Version(self, value):
        self._version = value

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
