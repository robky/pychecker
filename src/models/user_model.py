from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.enums import limits
from db.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(
        String(limits.MAX_LENGTH_EMAIL), unique=True, nullable=False
    )
    password = Column(String(limits.MAX_LENGTH_PASSWORD), nullable=False)

    file = relationship(
        "File",
        cascade="all, delete",
        back_populates="author",
    )

    def __repr__(self):
        return f"{self.email}"
