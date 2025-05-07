# File: /src/models/article.py
from uuid import uuid4

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.services.orm import ORM


class Article(ORM.Base):
    __tablename__ = "articles"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", name="users_author_id_fk"),
        nullable=False,
    )
    author = relationship("User", foreign_keys=[author_id])


