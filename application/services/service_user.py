from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.models.model_user import User
from application.shemas.shema_user import UserSchema


class ServiceUser:

    async def add(self, user: UserSchema, session: AsyncSession) -> Union[UserSchema, dict]:
        user = User(**user.__dict__)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        response = UserSchema(**user.__dict__)
        return {'new_user': response}

    async def get_user_name(self, user_id, session: AsyncSession) -> str:
        query = select(User).where(User.id == user_id)
        user = await session.execute(query)
        user = user.fetchone()[0]
        name = f'{user.name} {user.surname}'.title()
        return name