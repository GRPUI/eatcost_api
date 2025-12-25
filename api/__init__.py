from litestar import Router

from api import v1

router = Router(path="/api", route_handlers=[v1.router])
