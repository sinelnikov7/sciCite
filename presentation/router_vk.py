from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.shemas.shema_vk import VkSchema
from application.usecases.usecase_vk import vk_add
from infrastructure.database.database import get_session


vk_router = APIRouter(
    prefix="/vk",
    tags=["Vk"]
)


@vk_router.post('/add', status_code=201)
async def add_vk(vk: VkSchema, session: AsyncSession = Depends(get_session)):
    return await vk_add(vk, session)
