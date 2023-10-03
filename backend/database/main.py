from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.utils.singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    BASE: Final = declarative_base()

    def __init__(self):
        self._engine = create_engine('sqlite:///database.db')
        session = sessionmaker(bind=self._engine)
        self._session = session()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine
