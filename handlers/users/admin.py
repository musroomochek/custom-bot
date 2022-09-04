import aiofiles
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.utils.exceptions import BotBlocked

from data import config
from keyboards.inline.admin_keyboard import admin
from loader import dp, bot
from states.select_info import GetMessage
from utils.db_api.commands.goods_cmd import add_item, delete_goods_id
from utils.db_api.commands.users_cnd import select_all_users
from utils.misc.admin_helper import insert_txt


@dp.message_handler(Command('admin'))
async def admin_cmd(message: types.Message):
    if str(message.chat.id) in config.ADMINS:
        await message.answer('Добро пожаловать в админ-панель.\n'
                             'Выберите необходимое действие на клавиатуре.', reply_markup=admin)
    else:
        pass


@dp.callback_query_handler(Text(equals='add_item'))
async def first_step_add(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Отправь мне сообщение по следующей форме:\n\n'
                                 'Категория|Название|Описание|Цена|Ссылка на картинку\n\n'
                                 '(можно вносить сразу несколько товаров)')

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
            await add_item(
                category=for_db[0],
                product=for_db[1],
                description=for_db[2],
                price=for_db[3],
                photo=for_db[4]

            )
        await state.reset_state()
        await message.answer(f'{counter} записей было добавлено.')


@dp.callback_query_handler(Text(equals='delete_item'))
async def delete_goods(call: types.CallbackQuery):
    await insert_txt()
    async with aiofiles.open('goods.txt', mode='rb') as f:
        await bot.send_document(call.message.chat.id, f, caption='Введите ID товара для удаления')
        await f.close()
    await GetMessage.get_id.set()


@dp.message_handler(state=GetMessage.get_id)
async def delete_second(message: types.Message, state: FSMContext):
    await state.reset_state()
    rows = message.text.split('\n')
    counter = 0
    for row in rows:
        await delete_goods_id(row)
        counter += 1
    await message.answer(f'{counter} записей было удалено!')


@dp.callback_query_handler(Text(equals='mailing'))
async def start_mailing(call: types.CallbackQuery):
    await call.message.edit_text('Введите текст для рассылки')
    await GetMessage.message.set()


@dp.message_handler(state=GetMessage.message)
async def get_message_mailing(message: types.Message, state: FSMContext):
    counter_user = 0
    counter_blocked = 0
    text = message.text
    users = await select_all_users()
    try:
        for user in users:
            await dp.bot.send_message(
                chat_id=user,
                text=text
            )
            counter_user += 1
    except BotBlocked:
        counter_blocked += 1
    await state.reset_state()

    await message.answer(f'Сообщение было доставлено {counter_user} людям.\n'
                         f'Не получили - {counter_blocked} человек')
