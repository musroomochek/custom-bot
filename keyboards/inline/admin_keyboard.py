from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Рассылка', callback_data='mailing')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Добавить новое место', callback_data='add_place')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Удалить место', callback_data='delete_place')
                                 ]
                             ])
