from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def pagination_keyboard(list_id, category, good_id):
    pagination = InlineKeyboardMarkup(row_width=5,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='<-',
                                                                   callback_data=f'category_{category}_{list_id - 1}'),
                                              InlineKeyboardButton(text='Заказать', callback_data=f'order_{good_id}'),
                                              InlineKeyboardButton(text='Назад', callback_data='in_categories'),
                                              InlineKeyboardButton(text='->',
                                                                   callback_data=f'category_{category}_{list_id + 1}')
                                          ]
                                      ])

    return pagination
