import os
import logging

from dotenv import load_dotenv
from pydantic import BaseSettings

'''
    Load Environments
'''
load_dotenv(verbose=True)


class Settings(BaseSettings):
    PRODUCTION: bool = os.getenv('PRODUCTION')

    SERVICE_NAME: str = os.getenv('SERVICE_NAME')
    SERVICE_DESC: str = os.getenv('SERVICE_DESC')
    SERVICE_VERSION: str = os.getenv('SERVICE_VERSION')

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

    ESUME_DATABASE_URL: str = os.getenv('ESUME_DATABASE_URL')


settings = Settings()

logging.info(f'DATABASE {settings.ESUME_DATABASE_URL}')
