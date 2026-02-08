from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кто я", request_location=True),
            KeyboardButton(text="Погода")
        ],
        [
            KeyboardButton(text="Картинка"),
            KeyboardButton(text="Анекдот")
        ]
    ],
    is_persistent=True,
    resize_keyboard=True,
    input_field_placeholder="Что Вас интересует?"
)

del_kb=ReplyKeyboardRemove()