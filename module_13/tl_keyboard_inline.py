from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
# ReplyKeyboardMarkup - клавиатура, KeyboardButton - кнопка
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
