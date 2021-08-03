"""
@Author:
    Bart Kim 

@Note:

"""

from fastapi.middleware.cors import CORSMiddleware


from app.settings import settings


if settings.PRODUCTION:
    ALLOW_HOST: list = [
        "https://esume.me",
        "https://api.esume.me",
    ]
else:
    ALLOW_HOST: list = [
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://localhost:5000",
    ]

config: dict = {
    'allow_origins': ALLOW_HOST,
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}
