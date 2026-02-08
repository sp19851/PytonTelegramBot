from string import punctuation

from aiogram import types, Router, F
from aiogram.filters import CommandStart

from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


restricted_words = {'кабан', 'хомяк', 'выхухоль', 'олень'}

def cleaner(text:str):
    return text.translate(str.maketrans('','', punctuation))

@user_group_router.edited_message()
@user_group_router.message()
async def start_cmd(message: types.Message):
    if restricted_words.intersection(cleaner(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}! Вы используете запрещенные слова!")
        await message.delete()


