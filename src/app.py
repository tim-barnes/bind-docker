import logging
import uvicorn
from fastapi import FastAPI

import apis.health
import apis.message
from settings import Settings


# Default to debug for logging
logging.getLogger().setLevel(logging.DEBUG)
_log = logging.getLogger(__name__)


settings = Settings()
app = FastAPI(title="Encrypted comms demo",
              description=f"# {settings.hostname}{settings.zone}")
_log.info(f"Hello {settings.hostname}")

app.include_router(apis.health.router, prefix="/health", tags=apis.health.tags)
app.include_router(apis.message.router, prefix="/messages", tags=apis.message.tags)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
