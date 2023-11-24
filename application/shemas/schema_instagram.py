from pydantic import BaseModel

class InstagramSchema(BaseModel):
    user_id: int
    instagram_login: str