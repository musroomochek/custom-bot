from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.goods import Goods


async def add_place(category,  product, description, price, photo):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Goods(category=category, product=product, description=description, price=price, photo=photo))

            await session.commit()
    except IntegrityError:
        return True


async def get_categories():
    async with async_sessionmaker() as session:
        array = []
        sql = select(Goods.category)

        result = await session.execute(sql)

        for row in result.scalars():
            array.append(row)

    return array