from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from settings import Settings

router = APIRouter()
tags = ["health"]

hostname = Settings().hostname


@router.get("/", status_code=HTTP_200_OK)
def get_health():
    """
    Returns that the service is healthy
    """
    return f"{hostname} OK"
