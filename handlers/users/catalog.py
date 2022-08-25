from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.categories import get_categories_kb
from loader import dp


@dp.callback_query_handler(Text(equals='catalog'))
async def show_catalog(call: types.CallbackQuery):
    keyboard = await get_categories_kb()
    await call.message.edit_text('Вы попали в каталог, выберете необходимую вам категорию!', reply_markup=keyboard)