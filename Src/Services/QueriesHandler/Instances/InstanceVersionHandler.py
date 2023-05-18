# Handle
from Src.Infrastructure.BaseClasses.QueriesHandler import QueriesHandler
from Src.Services.Domain.Models.Instances.Instances import Instances
from Src.Services.Queries.Instances.InstanceVersion import InstanceVersionRequest, InstanceVersionResponse
from Src.Services.Repositories.InstancesRepository import InstancesRepository


class InstanceVersionHandler(QueriesHandler):

    def Handler(self, item: InstanceVersionRequest) -> InstanceVersionResponse:
        response = InstanceVersionResponse()
        instance = Instances()
        instance.ServerName = item.ServerName
        instance.Login = item.Login
        instance.Password = item.Password

        result = InstancesRepository.CheckExists(instance)
        response.Version = result

        return response
