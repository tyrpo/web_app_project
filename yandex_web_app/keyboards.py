from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://tyrpo.github.io/web_app_project/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Товары', web_app=web_app)]
    ],
    resize_keyboard=True
)
