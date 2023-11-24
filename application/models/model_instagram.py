from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base


class Instagram(Base):
    __tablename__ = 'instagram'
    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("users.id"))
    instagram_login = Column(String(50), nullable=False)
    user = relationship('User', back_populates='instagram')