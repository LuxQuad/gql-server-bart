from fastapi import FastAPI
from .settings import settings

from . import middleware
from . import routers

app = FastAPI(
    title=settings.SERVICE_NAME,
    description=settings.SERVICE_NAME,
    verison=settings.SERVICE_NAME,
)
'''
    Fast API Middleware
'''
app.add_middleware(
    middleware.cors.CORSMiddleware,
    **middleware.cors.config
)

'''
    Fast API Router
'''
app.include_router(routers.hello.router)
