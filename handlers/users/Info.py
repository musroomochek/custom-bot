from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.callback_query_handler(Text(equals='info'))
async def show_info(call: types.CallbackQuery):
    await call.message.edit_text('Введите ваши данные для отправки по форме: \n'
                                 'Полный адрес, \n'
                                 'Номер телефона, \n'
                                 'Имя Фамилия')