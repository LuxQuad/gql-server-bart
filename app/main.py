from fastapi import FastAPI
from .settings import settings

from . import middleware
from . import routers
from . import database

'''
    DB Migrate
'''
core_db = database.esume
core_db.Base.metadata.create_all(bind=core_db.Engine)


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
app.include_router(routers.user.router)
