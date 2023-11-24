from pydantic import BaseModel

class VkSchema(BaseModel):
    user_id: int
    vk_id: str