from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", "Asosiy menu"),
            # types.BotCommand("chat", "Chat orqali bog'lanish"),
            # types.BotCommand("clear","Menularni tozalash!")
        ]
    )
