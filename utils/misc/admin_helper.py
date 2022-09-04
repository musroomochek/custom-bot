import os

import aiofiles as aiofiles

from utils.db_api.commands.goods_cmd import get_all_goods


async def insert_txt():
    rows = await get_all_goods()

    if os.path.exists('goods.txt'):
        os.remove('goods.txt')

    async with aiofiles.open('goods.txt', mode='a', encoding='utf-8') as f:
        for row in rows:
            await f.write(row)
            await f.write('\n')
        await f.close()
