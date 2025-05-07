# File: /src/services/orm.py
import logging
import os
from time import sleep
from typing import Generator

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.engine import URL, Engine
from sqlalchemy.exc import DatabaseError, OperationalError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session

logger = logging.getLogger(__name__)

class ORM:
    # Construct a base class for declarative class definitions.
    #
    # The new base class will be given a metaclass that produces
    # appropriate `~sqlalchemy.schema.Table` objects and makes
    # the appropriate `_orm.Mapper` calls based on the
    # information provided declaratively in the class and any subclasses
    # of the class.
    Base = declarative_base()

    @staticmethod
    def create_engine() -> Engine:
        """
        Create a SQLAlchemy engine using the environment variables.

        If the environment variables are not set, it will try to load them from a .env file.
        """
        if not os.environ.get("DB_USERNAME"):
            load_dotenv()

        db_username: str = os.environ.get("DB_USERNAME", "")
        db_password: str = os.environ.get("DB_PASSWORD", "")
        db_name: str = os.environ.get("DB_NAME", "changos")
        db_port: int = int(os.environ.get("DB_PORT", 5432))
        db_host: str = os.environ.get("DB_HOST", "localhost")
        db_echo: bool = os.environ.get("DB_ECHO", "False").lower() == "true"
        db_pool_size: int = int(os.environ.get("DB_POOL_SIZE", 5))
        db_max_overflow: int = int(os.environ.get("DB_MAX_OVERFLOW", 10))
        db_pool_timeout: int = int(os.environ.get("DB_POOL_TIMEOUT", 30))
        db_pool_recycle: int = int(os.environ.get("DB_POOL_RECYCLE", 1800))

        logger.info("Connecting to the database", extra={"db_name": db_name, "db_host": db_host, "db_port": db_port})
        logger.debug(
            "DB config",
            extra={
                "db_echo": db_echo,
                "db_pool_size": db_pool_size,
                "db_max_overflow": db_max_overflow,
                "db_pool_timeout": db_pool_timeout,
                "db_pool_recycle": db_pool_recycle
            }
        )

        # Here we create a connection URL for the database
        # But in the old people-app the connection URL was read from the environment
        connection_url: URL = sqlalchemy.URL.create(
            "postgresql+psycopg2",
            username=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )

        return sqlalchemy.create_engine(
            connection_url,
            pool_pre_ping=True,             # Already enabled, which is good
            pool_recycle=db_pool_recycle,   # Recycle connections after 30 minutes
            pool_timeout=db_pool_timeout,   # Wait up to 30 seconds for a connection
            pool_size=db_pool_size,         # Maintain at least 5 connections
            max_overflow=db_max_overflow,   # Allow up to 10 additional connections
            echo=db_echo,                   # Set to True to see SQL queries
        )

    @staticmethod
    def create_session() -> Session:
        engine: Engine = ORM.create_engine()
        maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return maker()

    @staticmethod
    def get_db_session() -> Generator[Session, None, None]:
        """
        A context manager that provides a database session to the caller.

        It uses yield to return the session and ensures that it gets
        closed after the request is processed.
        """
        session = ORM.create_session()
        session_id = id(session)
        try:
            logger.debug("DB Transaction started", extra={"session": session_id})
            yield session
            session.commit()
            logger.debug("DB Transaction committed", extra={"session": session_id})
        except Exception:
            session.rollback()
            logger.debug("DB Transaction rolled back", extra={"session": session_id})
            raise
        finally:
            session.close()

    @staticmethod
    def get_schema_session():
        """This function will provide the session used in schemas."""
        return next(ORM.get_db_session())  # Use next() to retrieve the session

    @staticmethod
    def with_retry(session_func, max_retries=3):
        retries = 0
        while retries < max_retries:
            try:
                return session_func()
            except (OperationalError, DatabaseError) as e:
                retries += 1
                if retries == max_retries:
                    raise
                logger.warning("Database operation failed, retrying...", extra={"retries": retries, "max_retries": max_retries, "error": e})
                sleep(1)  # Wait before retrying

