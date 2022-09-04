from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from keyboards.inline.back import go_back
from keyboards.inline.categories import get_categories_kb
from keyboards.inline.pagination import pagination_keyboard
from loader import dp
from utils.db_api.commands.goods_cmd import get_item_category


@dp.callback_query_handler(Text(equals='catalog'))
async def show_catalog(call: types.CallbackQuery):
    keyboard = await get_categories_kb()
    await call.message.edit_text('Вы попали в каталог, выберете необходимую вам категорию!', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='category_'))
async def get_item_by_category(call: types.CallbackQuery):
    await call.message.delete()
    category = call.data.split('_')[1]
    list_id = call.data.split('_')[2]

    try:
        data = await get_item_category(category)

        if int(list_id) <= 0:
            list_id = 0

        if int(list_id) >= len(data):
            list_id = 0

        photo = data[int(list_id)].split('|')[3]
        product = data[int(list_id)].split('|')[0]
        description = data[int(list_id)].split('|')[1]
        price = data[int(list_id)].split('|')[2]
        good_id = data[int(list_id)].split('|')[4]
        keyboard = await pagination_keyboard(list_id=int(list_id), category=category, good_id=good_id)

        await call.message.answer_photo(
            photo=photo,
            caption=f'{product}\n\n'
                    f'{description}\n\n'
                    f'Цена: {price} рублей.',
            reply_markup=keyboard
        )
    except IndexError as error:
        print(error)
        await call.answer('К сожалению, товар отсутствует.')


@dp.callback_query_handler(Text(equals='in_categories'))
async def go_categories(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = await get_categories_kb()
    await call.message.answer('Вы попали в каталог, выберете необходимую вам категорию!', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='order_'))
async def send_order(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Мы успешно уведомили администратора о новом заказе, с вами скоро свяжутся.',
                              reply_markup=go_back)
    good_id = call.data.split('_')[1]

    await dp.bot.send_message(
        chat_id=ADMINS[0],
        text=f'Поступил новый заказ от @{call.from_user.username}\n'
             f'Информация по заказу: ID товара в таблице {good_id}'
    )
