from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Каталог', callback_data='catalog')
                                ],
                                [
                                    InlineKeyboardButton(text='Данные', callback_data='info')
                                ],
                                [
                                    InlineKeyboardButton(text='вопросы', callback_data='questions')
                                ],
                                [
                                    InlineKeyboardButton(text='ТГ канал', url='https://t.me/+k2CCiD1lgkgyZTBi')
                                ]
                            ])
