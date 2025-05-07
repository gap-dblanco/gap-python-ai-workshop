# File: /src/controllers/user_controller.py

from sqlalchemy.orm.session import Session


class UserController:

    def run(self, session: Session):
        return {"data": []}

