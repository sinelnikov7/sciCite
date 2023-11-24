from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.shemas.schema_instagram import InstagramSchema
from application.usecases.usecase_instagram import instagram_add
from infrastructure.database.database import get_session



instagram_router = APIRouter(
    prefix="/instagram",
    tags=["Instagram"]
)


@instagram_router.post('/add', status_code=201)
async def add_instagram(instagram: InstagramSchema, session: AsyncSession = Depends(get_session)):
    return await instagram_add(instagram, session)