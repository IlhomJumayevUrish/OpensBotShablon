import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuBottom import menuAsosiy, topmenu
from loader import dp


@dp.message_handler(CommandStart(),state=None)
async def bot_start(message: types.Message, state: FSMContext):
    # logging.info(message)
    await state.finish()
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuAsosiy)
