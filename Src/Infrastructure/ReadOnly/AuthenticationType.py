from Src.Infrastructure.Dictionaries.ReadOnlyDictionary import ReadOnlyDictionary


class AuthenticationType:
    AuthenticationTypeDictionary = ReadOnlyDictionary({"WindowsAuthentication": "Windows Authentication",
                                                           'SqlServerAuthentication': 'SQL Server Authentication'})