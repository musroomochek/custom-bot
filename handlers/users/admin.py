from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data import config
from keyboards.inline.admin_keyboard import admin
from loader import dp
from states.select_info import GetMessage
from utils.db_api.commands.goods_cmd import add_place


@dp.message_handler(Command('admin'))
async def admin_cmd(message: types.Message):
    if str(message.chat.id) in config.ADMINS:
        await message.answer('Добро пожаловать в админ-панель.\n'
                             'Выберите необходимое действие на клавиатуре.', reply_markup=admin)
    else:
        pass



@dp.callback_query_handler(Text(equals='add_place'))
async def first_step_add(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Отправь мне сообщение по следующей форме:\n\n'
                                 'Категория|Название|Описание|Цена|Ссылка на картинку\n\n'
                                 '(можно вносить сразу несколько мест)')

    await GetMessage.first()


@dp.message_handler(state=GetMessage.info)
async def last_step_add(message: types.Message, state: FSMContext):
    info = message.text
    counter = 0
    if info.find('|') == 0:
        await state.reset_state()
        await message.answer('Вы отправили что-то другое. Стейт сбросился.')
    else:
        rows = info.split('\n')
        for row in rows:
            counter += 1
            for_db = row.split('|')
            await add_place(
                category=for_db[0],
                product=for_db[1],
                description=for_db[2],
                price=for_db[3],
                photo=for_db[4]

            )
        await state.reset_state()
        await message.answer(f'{counter} записей было добавлено.')