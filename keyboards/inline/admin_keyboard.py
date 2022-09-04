from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.commands.goods_cmd import get_categories

admin = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Рассылка', callback_data='mailing')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Добавить новую вещь', callback_data='add_item')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Удалить вещь', callback_data='delete_item')
                                 ]
                             ])


async def categories_kb():
    categories = InlineKeyboardMarkup(row_width=3)

    data = await get_categories()

    for row in data:
        btn = InlineKeyboardButton(text=row, callback_data=f'del_{row}')
        categories.add(btn)

    return categories


# async def description_kb(category):
#     data = await get_description(category)
#
#     desc = InlineKeyboardMarkup(row_width=3)
#
#     for row in data:
#         btn = InlineKeyboardButton(text=row, callback_data=f'get_{row}')
#         desc.add(btn)
#
#     return desc