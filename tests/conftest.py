# File: /tests/conftest.py

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app import app
from src.services.orm import ORM
from tests.factories import BaseFactory

load_dotenv()

@pytest.fixture(scope="session")
def test_engine():
    # Create a database connection using environment variables (already loaded by pytest_configure)
    engine = ORM.create_engine()

    # Create the tables
    ORM.Base.metadata.create_all(engine)

    yield engine

    # Drop the tables after tests with cascade
    ORM.Base.metadata.drop_all(engine, checkfirst=True)

    # Execute raw SQL for cascading drop of any dependent objects
    with engine.connect() as connection:
        connection.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))

    engine.dispose()


@pytest.fixture(scope="function", autouse=True)
def db_session(test_engine):
    """Creates a new scoped database session for a test."""
    maker = sessionmaker(bind=test_engine)
    session = maker()

    try:
        yield session
    finally:
        # Rollback after each test to ensure a clean state
        session.rollback()
        session.close()


@pytest.fixture(autouse=True)
def set_session_for_factories(db_session):
    """Assign the session to all SQLAlchemyModelFactory instances."""

    # Assign the session to BaseFactory and all subclasses
    BaseFactory._meta.sqlalchemy_session = db_session  # type: ignore
    BaseFactory.assign_session(db_session)


@pytest.fixture(scope="function")
def routes_client(db_session):
    # Override dependency for tests
    app.dependency_overrides[ORM.get_db_session] = lambda: db_session
    yield TestClient(app)

