# File: /src/controllers/home_controller.py
from sqlalchemy.orm.session import Session


class HomeController:

    def run(self, session: Session):
        return {"message": "Welcome to the GAP Python AI Workshop API!"}

