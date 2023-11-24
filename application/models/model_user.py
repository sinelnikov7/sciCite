from sqlalchemy import Column, INTEGER, String
from sqlalchemy.orm import relationship

from application.models.model_instagram import Instagram
from application.models.model_telegram import Telegram
from infrastructure.database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    telegram = relationship(Telegram, back_populates="user", uselist=True)
    instagram = relationship(Instagram, back_populates="user", uselist=True)
    vk = relationship('Vk', back_populates="user", uselist=False)

