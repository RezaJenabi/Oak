class ReadOnlyDictionary(dict):

    __readonly = True

    def readonly(self, allow=1):
        """Allow or deny modifying dictionary"""
        self.__readonly = bool(allow)

    def __setitem__(self, key, value):

        if self.__readonly:
            raise Exception('deny modifying readonly dictionary')
        return dict.__setitem__(self, key, value)

    def __delitem__(self, key):

        if self.__readonly:
            raise Exception('deny modifying readonly dictionary')
        return dict.__delitem__(self, key)