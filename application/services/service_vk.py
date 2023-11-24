from typing import Union
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from application.models.model_vk import Vk
from application.shemas.shema_vk import VkSchema


class ServiceVk:

    async def add(self, vk: VkSchema, session: AsyncSession) -> Union[VkSchema, dict]:
        try:
            vk = Vk(**vk.__dict__)
            session.add(vk)
            await session.commit()
            await session.refresh(vk)
            response = VkSchema(**vk.__dict__)
            return {'new_vk': response}
        except IntegrityError:
            return {'error': "Пользователь не найден или он является дубликатом"}

    async def get_vk_id(self, user_id, session: AsyncSession) -> str:
        query = select(Vk).where(Vk.user_id == user_id)
        user_vk = await session.execute(query)
        user_vk = user_vk.fetchone()[0]
        vk_id = user_vk.vk_id
        return vk_id
