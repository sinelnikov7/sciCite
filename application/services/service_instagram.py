from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from application.models.model_instagram import Instagram
from application.models.model_user import User
from application.shemas.schema_instagram import InstagramSchema


class InstagramService:

    async def add(self, instagram: InstagramSchema, session) -> Union[InstagramSchema, dict]:
        try:
            instagram = Instagram(**instagram.__dict__)
            session.add(instagram)
            await session.commit()
            await session.refresh(instagram)
            response = InstagramSchema(**instagram.__dict__)
            return {'new_instagram': response}
        except IntegrityError:
            return {'error': "Пользователь не найден"}

    async def get_instagram_users(self, user_id: int, session: AsyncSession):
        query = select(User).options(selectinload(User.instagram)).where(User.id == user_id)
        user = await session.execute(query)
        user = user.fetchone()[0]
        list_result = [contact.instagram_login for contact in user.instagram]
        return list_result