from sqlalchemy import Column, Integer, BigInteger, String, sql

from utils.db_api.base import Base


class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)

    category = Column(String)
    product = Column(String)
    description = Column(String)
    price = Column(String)
    photo = Column(String)

    query: sql.Select
