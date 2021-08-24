from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message,ReplyKeyboardRemove
from loader import dp
from keyboards.default.menuBottom import menuAsosiy, topmenu


@dp.message_handler(Command('clear'))
async def show_menu(message: Message):
    await message.answer("Hamma narsa tozalandi!",reply_markup=ReplyKeyboardRemove())
