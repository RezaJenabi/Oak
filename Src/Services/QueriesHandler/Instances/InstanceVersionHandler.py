# Handle
from Src.Infrastructure.BaseClasses.QueriesHandler import QueriesHandler
from Src.Services.Entity.Models.Instances import Instances
from Src.Services.Queries.Instances.InstanceVersion import InstanceVersionRequest, InstanceVersionResponse
from Src.Services.Repositories.InstancesRepository import InstancesRepository


class InstanceVersionHandler(QueriesHandler):

    def Handler(self, item: InstanceVersionRequest) -> InstanceVersionResponse:
        response = InstanceVersionResponse()
        instance = Instances(item.ServerName, item.ServerAuthenticationType, item.Login, item.Password)

        result = InstancesRepository.GetVersion(instance)
        if result is not None:
            response.Version = result
        else:
            response.Status = False

        return response
