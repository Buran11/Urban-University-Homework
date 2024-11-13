from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import logging

from config import *
from keyboards import *
from admin import *
from db import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}! ' + texts.start, reply_markup=start_kb)


# message.answer_photo, answer_video, answer_audio, answer_file
@dp.message_handler(text=['О нас'])
async def price(message: types.Message):
    with open('./files/04.png', 'rb') as img:
        await message.answer_photo(img, texts.about, reply_markup=start_kb)


@dp.message_handler(text=['Стоимость'])
async def info(message: types.Message):
    await message.answer(texts.price, reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_m(call: types.CallbackQuery):
    with open('./files/01.png', 'rb') as img:
        await call.message.answer_photo(img, texts.Mgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='big')
async def buy_l(call: types.CallbackQuery):
    with open('./files/02.png', 'rb') as img:
        await call.message.answer_photo(img, texts.Lgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='very_big')
async def buy_xl(call: types.CallbackQuery):
    with open('./files/03.png', 'rb') as img:
        await call.message.answer_photo(img, texts.XLgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call: types.CallbackQuery):
    await call.message.answer(texts.other, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call: types.CallbackQuery):
    await call.message.answer(texts.price, reply_markup=catalog_kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
