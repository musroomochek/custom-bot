from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menu import menu
from loader import dp
from utils.db_api.commands.users_cnd import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, ты попал в бота с моими кастомами! \n"
                         f"Для начала выбери на клавиатуре пункт, который тебе нужен.", reply_markup=menu)
    await add_user(
        telegram_id=message.chat.id,
        username=message.from_user.username
    )