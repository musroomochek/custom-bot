from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.Goods import sow_goods
from loader import dp


@dp.message_handler(Text(equals='cart'))
async def show_cart(call: types.CallbackQuery):
    await call.message.edit_text('Вы попали в корзину!', reply_markup=sow_goods)