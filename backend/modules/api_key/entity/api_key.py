from pydantic import BaseModel


class ApiKey(BaseModel):
    key_id: str
    user_id: str
    name: str
    days: int
    only_chat: bool
    api_key: str
    creation_time: str
    deleted_time: str
    is_active: bool
