from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.goods import Goods


async def add_item(category, product, description, price, photo):
    try:
        async with async_sessionmaker() as session:
            await session.merge(
                Goods(category=category, product=product, description=description, price=price, photo=photo))

            await session.commit()
    except IntegrityError:
        return True


async def get_categories():
    async with async_sessionmaker() as session:
        array = []
        sql = select(Goods.category)

        result = await session.execute(sql)

        for row in result.scalars():
            if row not in array:
                array.append(row)

    return array


async def get_item_category(category):
    async with async_sessionmaker() as session:
        array = []
        sql = select(Goods).where(Goods.category == category)

        result = await session.execute(sql)

        for row in result.scalars():
            array.append(f'{row.product}|{row.description}|{row.price}|{row.photo}|{row.id}')

        return array


async def get_all_goods():
    array = []
    async with async_sessionmaker() as session:
        data = select(Goods)

        result = await session.execute(data)

        for row in result.scalars():
            array.append(f'{row.id}| {row.category} - {row.product} - {row.description} - {row.price}')
        return array


async def delete_goods_id(id: int):
    async with async_sessionmaker() as session:
        bye = delete(Goods).where(Goods.id == int(id))
        await session.execute(bye)
        await session.commit()