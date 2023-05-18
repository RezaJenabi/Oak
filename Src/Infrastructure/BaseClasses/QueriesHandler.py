from Src.Infrastructure.BaseClasses.Request import Request
from Src.Infrastructure.BaseClasses.Response import Response


class QueriesHandler:
    def Handler(self, item: Request) -> Response:
        raise NotImplementedError("Subclass needs to define this.")
