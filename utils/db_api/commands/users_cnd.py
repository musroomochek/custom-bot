from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.users import Users


async def add_user(telegram_id, username):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Users(telegram_id=telegram_id, username=username))
            await session.commit()
    except IntegrityError:
        return True




