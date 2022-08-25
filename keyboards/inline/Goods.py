from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sow_goods = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Показать товары', callback_data='show_goods')
                                ],
                                [
                                    InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                ]
                            ])