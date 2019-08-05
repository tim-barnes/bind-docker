import logging
import uvicorn
from fastapi import FastAPI

import apis.health
from settings import Settings


# Default to debug for logging
_log = logging.getLogger(__name__)
_log.info("Starting Filer Service")

settings = Settings()
app = FastAPI(title="Encrypted comms demo",
              description=f"# {settings.hostname}{settings.zone}")

app.include_router(apis.health.router, prefix="/health", tags=["health"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
