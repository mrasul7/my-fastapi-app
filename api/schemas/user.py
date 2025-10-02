from pydantic import BaseModel


class UserMessage(BaseModel):
    phone_number: str
    text: str