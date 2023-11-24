from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from application.models.model_telegram import Telegram
from application.models.model_user import User
from application.shemas.schema_telegram import TelegramSchema


class TelegramService:

    async def add(self, telegram: TelegramSchema, session) -> Union[TelegramSchema, dict]:
        try:
            telegram = Telegram(**telegram.__dict__)
            session.add(telegram)
            await session.commit()
            await session.refresh(telegram)
            response = TelegramSchema(**telegram.__dict__)
            return {'new_telegram': response}
        except IntegrityError:
            return {'error': "Пользователь не найден"}

    async def get_list_tg_contackts(self, user_id: int, session: AsyncSession) -> list:
        query = select(User).options(selectinload(User.telegram)).where(User.id == user_id)
        user = await session.execute(query)
        user = user.fetchone()[0]
        return [contact.telegram_login for contact in user.telegram]





