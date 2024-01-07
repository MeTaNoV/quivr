from pydantic import BaseModel


class ApiKeyInfo(BaseModel):
    key_id: str
    name: str
    days: int
    creation_time: str
