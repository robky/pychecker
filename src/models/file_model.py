from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class File(Base):
    __tablename__ = "file"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    created_ad = Column(DateTime, index=True, default=datetime.utcnow)
    size = Column(Integer, nullable=False)
    check_result = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship(
        "User",
        cascade="all, delete",
        back_populates="file",
    )

    def __repr__(self):
        return f"{self.name} ({self.created_ad})"
