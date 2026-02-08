from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

from keybords import reply_keybord

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await  message.answer(f"Привет, {message.from_user.first_name}! Я виртуальный помощник.",
                          reply_markup=reply_keybord.start_kb)


@user_private_router.message(or_f(Command('whoami'), (F.text.lower() == "кто я")))
async def about_cmd(message: types.Message):
    await message.answer(f'Кто я:{message.from_user.first_name}', reply_markup=reply_keybord.del_kb)
    await message.delete()


@user_private_router.message(or_f(Command('weather'), (F.text.lower() == "погода")))
async def weather_cmd(message: types.Message):
    await message.answer("Погода:", reply_markup=reply_keybord.del_kb)
    await message.delete()


@user_private_router.message(or_f(Command('image'), (F.text.lower() == "картинка")))
async def image_cmd(message: types.Message):
    await message.answer("Картинка:", reply_markup=reply_keybord.del_kb)
    await message.delete()


@user_private_router.message(or_f(Command('joke'), (F.text.lower() == "анекдот")))
async def joke_cmd(message: types.Message):

    await message.answer("Анекдот:", reply_markup=reply_keybord.del_kb)
    await message.delete()

#@user_private_router.message(F.text)
#async def menu_cmd(message: types.Message):
#    await message.answer("Это магический фильтр:")
