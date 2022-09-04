from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.commands.goods_cmd import get_categories


async def get_categories_kb():
    categories = InlineKeyboardMarkup(row_width=3)

    data = await get_categories()

    for row in data:
        button = InlineKeyboardButton(text=row, callback_data=f'category_{row}_0')
        categories.add(button)

    go_back = InlineKeyboardButton(text='Назад', callback_data='in_menu')
    categories.add(go_back)
    return categories
