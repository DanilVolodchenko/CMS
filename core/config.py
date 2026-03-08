from dotenv import dotenv_values
from pydantic import BaseModel, Field

env: dict = dotenv_values('.env')


class FastApiConfig(BaseModel):
    title: str = Field(default='CRM', alias='FASTAPI_TITLE')
    description: str = Field(default='CRM Service', alias='FASTAPI_DESCRIPTION')


class Config(BaseModel):
    fastapi: FastApiConfig = Field(default_factory=lambda: FastApiConfig(**env))
