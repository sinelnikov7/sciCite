from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base


class Telegram(Base):
    __tablename__ = 'telegram'
    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    telegram_login = Column(String(50), nullable=True, default='qqq')
    user = relationship('User', back_populates='telegram')