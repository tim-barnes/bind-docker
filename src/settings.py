import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    zone: str = '.muppets.things'
    hostname: str = os.environ.get('HOSTNAME')

    # uncomment this when doing encryption
    # private_key: str = ...

    class Config:
        fields = {
            'hostname': {
                'alias': 'hostname'
            }
        }