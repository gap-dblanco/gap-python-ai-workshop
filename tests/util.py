# -*- coding: utf-8 -*-
# File: /tests/util.py

from datetime import date

from src.models.birthdate import Birthdate


class Util:

    @staticmethod
    def fake_birthdate() -> Birthdate:
        """Generate a fake birthdate."""
        return Birthdate(date(1990, 1, 1))
