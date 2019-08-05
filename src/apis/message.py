import requests
import logging

from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from settings import Settings
from typing import List

_log = logging.getLogger(__name__)

router = APIRouter()
tags = ["messages"]

settings = Settings()

class Message(BaseModel):
    time: datetime
    source: str
    msg: str

class Messages(BaseModel):
    msgs: List[Message] = list()


messages = Messages()


@router.get("/", status_code=HTTP_200_OK, response_model=Messages)
def get_messages():
    """
    Returns the messages recieved
    """
    _log.info(f"Get messages: {messages}")
    return messages


@router.post("/", status_code=HTTP_200_OK)
def recieve_message(message: Message):
    _log.info(f"Recieved message: {message}")

    messages.msgs.append(message)
    return "OK"


@router.post("/{muppet}", status_code=HTTP_200_OK)
def send_message(muppet: str, message: str):
    """
    Sends a message to the named muppet
    """
    _log.info(f"Send message: To: {muppet} Content: {messages}")

    to_send = Message(time=datetime.utcnow(), source=settings.hostname, msg=message)
    requests.post(f"http://{muppet}{settings.zone}:5000/messages/", data=to_send.json())

    return "OK"
