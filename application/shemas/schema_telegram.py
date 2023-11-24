from pydantic import BaseModel

class TelegramSchema(BaseModel):
    user_id: int
    telegram_login: str