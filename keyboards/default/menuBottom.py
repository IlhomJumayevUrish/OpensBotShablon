from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menuAsosiy=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻 Kurslar bilan tanishing!'),
        ],
        [
            KeyboardButton(text='📆 Ochiq darslar vaqti!'),

            # KeyboardButton(text='👩‍💻 Ro\'yxatdan o\'ting!',request_contact=True),

        ],
        [
            KeyboardButton(text='📍 Location'),
            KeyboardButton(text='📞 Contact'),

            # KeyboardButton(text='🏢 Biz haqimizda!'),
# https://maps.google.com/maps?q=41.362787,69.193824&ll=41.362787,69.193824&z=16
        ],
        # [
        #     KeyboardButton(text='Ro\'yxatdan o\'tish!'),
        # ],

        # [
        #     KeyboardButton(text='Tilni tanlash!'),
        #     # KeyboardButton(text='Orqaga'),
        # ],
    ],
    resize_keyboard=True,

)
topmenu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu'),
            # KeyboardButton(text='Ortga'),

        ],
    ],
    resize_keyboard=True,

)

# menuStart = ReplyKeyboardMarkup(
#     keyboard = [
#         [
#             KeyboardButton(text='Contact', request_contact=True),
#         ],
#     ],
#     resize_keyboard=True
# )