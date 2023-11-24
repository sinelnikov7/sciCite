from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from application.shemas.shema_user import UserSchema
from application.usecases.usecase_user import user_add
from infrastructure.database.database import get_session
from infrastructure.celery.worker import user_report


user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@user_router.post('/add', status_code=201)
async def user_get(user: UserSchema, session: AsyncSession = Depends(get_session)):
    return await user_add(user, session)


@user_router.get('/generate_pdf/{user_id}')
async def generate_user_pdf(user_id: int):
    user_report.delay(user_id)
    return {"success": "Отчет сформирован"}
