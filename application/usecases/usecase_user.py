from datetime import datetime

import pdfkit
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.service_instagram import InstagramService
from application.services.service_user import ServiceUser
from application.shemas.shema_user import UserSchema
from application.usecases.usecase_telegram import get_full_info_about_tg_contackts
from application.usecases.usecase_vk import get_full_information_about_groups, get_full_information_about_friends
from infrastructure.database.database import async_session


service_user = ServiceUser()


async def user_add(user: UserSchema, session: AsyncSession) -> dict:
    return await service_user.add(user, session)


async def generate_pdf(user_id: int) -> None:
    user = ServiceUser()
    session = async_session()
    name = await user.get_user_name(1, session)
    time = datetime.now()
    time_stamp = time.strftime('%Y-%m-%d %H-%M-%S')
    output_file = f'{name}-{time_stamp}.pdf'
    instagram = InstagramService()
    instagram_contacts = await instagram.get_instagram_users(user_id, session)
    tgelegram_contacts = await get_full_info_about_tg_contackts(user_id, session)
    vk_group = await get_full_information_about_groups(user_id, session)
    vk_friends = await get_full_information_about_friends(user_id, session)
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("application/usecases/templates/template_for_pdf.html")
    pdf_template = template.render({'name': name, 'vk_group': vk_group, 'vk_friends': vk_friends,
                                    'tgelegram_contacts': tgelegram_contacts, 'instagram_contacts': instagram_contacts})
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_string(pdf_template, f'infrastructure/file_system/{output_file}', configuration=config)
