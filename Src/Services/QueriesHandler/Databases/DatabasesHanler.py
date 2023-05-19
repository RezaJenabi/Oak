from Src.Infrastructure.BaseClasses.QueriesHandler import QueriesHandler
from Src.Services.Entity.Models.Databases import Databases
from Src.Services.Queries.Databases.Databases import DatabasesResponse, DatabasesRequest


class DatabasesHanler(QueriesHandler):

    def Handler(self, item: DatabasesRequest) -> DatabasesResponse:
        response = DatabasesResponse()
        database = Databases()

        response.IsExists = True

        return response
