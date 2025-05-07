# File: /src/models/birthdate.py
from datetime import date, datetime

from sqlalchemy import types


class Birthdate:
    def __init__(self, date_value: date):
        if isinstance(date_value, datetime):
            date_value = date_value.date()
        self.date = date_value

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date.year
        if (today.month, today.day) < (self.date.month, self.date.day):
            years -= 1
        return years

    def __repr__(self):
        return f"Birthdate(date={self.date}, age={self.age})"


class BirthdateType(types.TypeDecorator):
    """SQLAlchemy type for Birthdate objects"""
    impl = types.Date

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, Birthdate):
            return value.date
        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return Birthdate(value)

