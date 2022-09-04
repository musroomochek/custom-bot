from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_back = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Назад', callback_data='in_menu'),
                                   ]
                               ])