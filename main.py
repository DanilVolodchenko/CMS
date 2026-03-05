import uvicorn

from core.config import Config
from core.registrar import create_app

__version__ = '0.0.1'

config = Config()
app = create_app(config.fastapi, version=__version__)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
