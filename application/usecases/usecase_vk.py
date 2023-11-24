import asyncio
import aiohttp

from sqlalchemy.ext.asyncio import AsyncSession

from application.services.service_vk import ServiceVk
from application.shemas.shema_vk import VkSchema
from config import VK_KEY


service_vk = ServiceVk()
key = VK_KEY
headers = {'Accept-Language': 'ru'}


async def vk_add(vk: VkSchema, session: AsyncSession) -> dict:
    return await service_vk.add(vk, session)


async def get_subscriptions(vk_id: str) -> dict:
    url_get_subscriptions = f"https://api.vk.com/method/users.getSubscriptions?user_id={vk_id}&" \
                            f"access_token={key}&v=5.154"
    async with aiohttp.ClientSession() as session:
        async with session.get(url_get_subscriptions) as response:
            data = await response.json()
            return data


async def get_friends(vk_id: str) -> dict:
    url_get_friends = f"https://api.vk.com/method/friends.get?user_id={vk_id}&" \
                      f"access_token={key}&v=5.154"
    async with aiohttp.ClientSession() as session:
        async with session.get(url_get_friends) as response:
            data = await response.json()
            return data


async def get_information_about_user(vk_id: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> dict:
    url_get_information_about_user = f"https://api.vk.com/method/users.get?user_ids={vk_id}&" \
                                     f"access_token={key}&fields=country,city&v=5.154"
    async with semaphore:
        await asyncio.sleep(0.5)
        async with aiohttp.ClientSession() as session:
            async with session.get(url_get_information_about_user, headers=headers) as response:
                data = await response.json()
                return data


async def get_information_about_group(group_id, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> dict:
    get_information_about_group = f"https://api.vk.com/method/groups.getById?group_id={group_id}" \
                                  f"&access_token={key}&v=5.154"
    async with semaphore:
        await asyncio.sleep(0.5)
        async with session.get(get_information_about_group, headers=headers) as response:
            data = await response.json()
            return data


async def get_full_information_about_groups(user_id: int, session: AsyncSession) -> list:
    vk = ServiceVk()
    vk_id = await vk.get_vk_id(user_id, session)
    subscriptions = await get_subscriptions(vk_id)
    group_list = subscriptions.get('response').get('groups').get('items')
    semaphore = asyncio.Semaphore(2)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_information_about_group(group_id, session, semaphore)) for group_id in group_list]
        result = await asyncio.gather(*tasks)
    list_group_names = []
    for name in result:
        list_group_names.append(name.get('response').get('groups')[0].get('name'))
    return list_group_names


async def get_full_information_about_friends(user_id: int, session: AsyncSession) -> list:
    vk = ServiceVk()
    vk_id = await vk.get_vk_id(user_id, session)
    friends = await get_friends(vk_id)
    friends_list = friends.get('response').get('items')
    semaphore = asyncio.Semaphore(2)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_information_about_user(friend_id, session, semaphore)) for friend_id in friends_list]
        result = await asyncio.gather(*tasks)
    list_friends = []
    for info in result:
        if info.get('response')[0].get('deactivated') != 'deleted':
            list_friends.append({"first_name": info.get('response')[0].get('first_name'), "last_name": info.get('response')[0].get('last_name')})
    return list_friends