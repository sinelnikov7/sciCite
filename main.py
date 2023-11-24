from fastapi import FastAPI

from presentation.router_instagram import instagram_router
from presentation.router_telegram import telegram_router
from presentation.router_user import user_router
from presentation.router_vk import vk_router


app = FastAPI()
app.include_router(user_router)
app.include_router(vk_router)
app.include_router(telegram_router)
app.include_router(instagram_router)