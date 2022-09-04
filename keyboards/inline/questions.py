from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_catalog = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='назад', callback_data='back')
                                      ]




                                  ])