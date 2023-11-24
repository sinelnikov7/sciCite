import asyncio

from telethon import TelegramClient
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.service_telegram import TelegramService
from application.shemas.schema_telegram import TelegramSchema
from config import API_ID, API_HASH


service_telegram = TelegramService()
api_id = int(API_ID)
api_hash = API_HASH


async def telegram_add(telegram: TelegramSchema, session: AsyncSession) -> dict:
    return await service_telegram.add(telegram, session)


async def get_contacts_info(client: TelegramClient, contact: str):
    entity = await client.get_entity(contact)
    return entity


async def get_full_info_about_tg_contackts(user_id: int, session: AsyncSession) -> list:
    tg = TelegramService()
    contacts = await tg.get_list_tg_contackts(user_id, session)
    client = await TelegramClient('session_name', api_id, api_hash).start()
    async with client:
        tasks = [get_contacts_info(client, contact) for contact in contacts]
        results = await asyncio.gather(*tasks)
    information_about_contack = []
    for contact in results:
        first_name = contact.first_name if contact.first_name != None else 'Не указано'
        last_name = contact.last_name if contact.last_name != None else 'Не указана'
        phone = contact.phone if contact.phone != None else 'Не указан'
        information_about_contack.append({'first_name': first_name, 'last_name': last_name, "phone": phone})
    return information_about_contack