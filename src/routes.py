from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm.session import Session

from src.controllers.dev.analysis_controller import AnalysisController
from src.controllers.dev.explain_controller import ExplainController
from src.controllers.healthcheck_controller import HealthcheckController
from src.controllers.home_controller import HomeController
from src.controllers.user_controller import UserController
from src.services.orm import ORM

# Dependency for the database session
SessionDep = Annotated[Session, Depends(ORM.get_db_session)]
# ---- Public API ----

router = APIRouter(prefix="/api", tags=["gap", "ai", "workshop"])

@router.get("/")
def get_root(session: SessionDep):
    return HomeController().run(session)

@router.get("/health")
def get_health(session: SessionDep):
    return HealthcheckController().run(session)


@router.get("/users")
async def get_users(session: SessionDep):
    return UserController().run(session)

# ---- Private API ----

dev_router = APIRouter(prefix="/dev", tags=["dev", "internal"])


@dev_router.get("/analysis", response_class=HTMLResponse)
async def get_analysis(session: SessionDep):
    return AnalysisController().run(session)

@dev_router.get("/explain", response_class=HTMLResponse)
async def get_analysis(session: SessionDep):
    return ExplainController().run(session)
