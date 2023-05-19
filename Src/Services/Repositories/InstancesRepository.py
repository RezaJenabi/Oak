import connectorx as cx

from Src.Infrastructure.ReadOnly.AuthenticationType import AuthenticationType
from Src.Services.Domain.Models.Instances.Instances import Instances


class InstancesRepository:

    @staticmethod
    def GetVersion(instance: Instances):
        try:
            server = instance.ServerName
            database = 'master'
            login = instance.Login
            password = instance.Password
            url = f'mssql://{server}/{database}?trusted_connection=true'
            if instance.ServerAuthenticationType == AuthenticationType.AuthenticationTypeDictionary.get(
                    'SqlServerAuthentication', {}):
                url = f'mssql://{login}:{password}@{server}/{database}?encrypt=true&trusted_connection=true'

            query = "SELECT @@VERSION AS  DatabaseVersion"
            data = cx.read_sql(url, query)
            databaseVersion: str = data[['DatabaseVersion']]
            return databaseVersion
        except:
            return None

