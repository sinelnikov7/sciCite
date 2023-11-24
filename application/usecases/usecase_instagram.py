from sqlalchemy.ext.asyncio import AsyncSession

from application.services.service_instagram import InstagramService
from application.shemas.schema_instagram import InstagramSchema


service_instagram = InstagramService()


async def instagram_add(instagram: InstagramSchema, session: AsyncSession) -> dict:
    return await service_instagram.add(instagram, session)