# File: /src/controllers/healthcheck_controller.py

from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import text


class HealthcheckController:

    def run(self, session: Session):
        if not self._check_db_connection(session):
            return JSONResponse(
                status_code=503,
                content={"status": "sick", "error": "Database connection unavailable"}
            )
        return {"status": "healthy"}


    def _check_db_connection(self, session: Session) -> bool:
        try:
            # Attempt to execute a simple query to check the connection
            session.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
