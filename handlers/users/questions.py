from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.callback_query_handler(Text(equals='questions'))
async def show_questions(call: types.CallbackQuery):
    await call.message.edit_text('Здесь вы можете найти часто задаваемые вопросы')