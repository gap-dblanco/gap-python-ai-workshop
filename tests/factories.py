# File: /tests/factories.py

import factory

from src.models.article import Article
from src.models.user import User
from tests.util import Util


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base factory that all other factories can inherit from."""

    class Meta:  # type: ignore
        # Prevents instantiation of BaseFactory directly
        abstract = True
        # Will be assigned automatically
        sqlalchemy_session = None

    @classmethod
    def assign_session(cls, session):
        """Assign the session to all subclasses of BaseFactory."""
        for subclass in cls.__subclasses__():
            subclass._meta.sqlalchemy_session = session  # type: ignore
            # Recursively assign the session to subclasses of subclasses
            subclass.assign_session(session)

    @classmethod
    def _after_postgeneration(cls, obj, create, results=None):
        """Automatically flush the session after creating an object"""
        if create:
            db_session = cls._meta.sqlalchemy_session
            db_session.flush()


class UserFactory(BaseFactory):
    class Meta:  # type: ignore
        model = User

    name = factory.Faker('name')
    dob = factory.LazyFunction(lambda: Util.fake_birthdate())
    picture = factory.Faker('image_url')


class ArticleFactory(BaseFactory):
    class Meta:  # type: ignore
        model = Article

    name = factory.Faker('name')
    content = factory.Faker('text')
    author_id = factory.LazyAttribute(lambda _: UserFactory().id)
