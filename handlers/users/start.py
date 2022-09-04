from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text

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


@dp.callback_query_handler(Text(equals='in_menu'), state='*')
async def go_menu(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(True)
    await call.message.delete()
    await bot_start(message=call.message)
