from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base


class Vk(Base):
    __tablename__ = 'vk'
    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("users.id"), unique=True)
    vk_id = Column(String(50), nullable=False)
    user = relationship('User', back_populates='vk')