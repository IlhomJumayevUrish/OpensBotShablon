from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
import logging
from data.config import ADMINS
from states.userData import PersonalData
# @dp.message_handler(Command('anketa'))
# async def enter_test(message:types.Message):
#     await message.answer("To'liq ismingizni kiriting!\n Misol: Ali Valiyev")
#     await PersonalData.fullName.set()
@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {"fullName":fullname}
    )
    await message.answer("Telefon nomerni kiriting! \n Misol: +99890 330 55 066")
    await PersonalData.phoneNum.set()



@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phoneNum = message.text
    await state.update_data(
        {"phoneNum": phoneNum}
    )
    data=await state.get_data()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"Ism familiya: {data.get('fullName')} \nKurs nomi: {data.get('kursName')} \nTelefon: {data.get('phoneNum')}")

        except Exception as err:
            logging.exception(err)
    await state.finish()
