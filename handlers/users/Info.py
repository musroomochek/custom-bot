from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp
from states.select_info import GetMessage
from utils.db_api.commands.users_cnd import add_info_user


@dp.callback_query_handler(Text(equals='info'))
async def show_info(call: types.CallbackQuery):
    await call.message.edit_text('Введите ваши данные для отправки по форме: \n'
                                 'Полный адрес, \n'
                                 'Номер телефона, \n'
                                 'Имя Фамилия')

    await GetMessage.get_address.set()


@dp.message_handler(state=GetMessage.get_address)
async def type_info(message: types.Message, state: FSMContext):
    text = message.text
    data = text.split(',')
    await add_info_user(
        telegram_id=message.chat.id,
        address=data[0],
        phone=data[1],
        name=data[2]
    )
    await message.answer('Данные были успешно добавлены')
    await state.reset_state(True)


