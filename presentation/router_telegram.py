from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.shemas.schema_telegram import TelegramSchema
from application.usecases.usecase_telegram import telegram_add
from infrastructure.database.database import get_session


telegram_router = APIRouter(
    prefix="/telegram",
    tags=["Telegram"]
)


@telegram_router.post('/add', status_code=201)
async def add_telegram(telegram: TelegramSchema, session: AsyncSession = Depends(get_session)):
    return await telegram_add(telegram, session)
