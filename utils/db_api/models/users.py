from sqlalchemy import Column, Integer, BigInteger, String, sql

from utils.db_api.base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    telegram_id = Column(BigInteger, unique=True)
    username = Column(String)
    address = Column(String)
    phone = Column(String)

    query: sql.Select
