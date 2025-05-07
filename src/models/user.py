# File: /src/models/user.py
from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID

from src.models.birthdate import BirthdateType
from src.services.orm import ORM


class User(ORM.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    dob = Column(BirthdateType, nullable=False)
    picture = Column(String(255))

