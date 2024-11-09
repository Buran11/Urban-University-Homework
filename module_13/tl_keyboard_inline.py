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

kb = ReplyKeyboardMarkup()  # клавиатура
button = KeyboardButton(text='Информация')  # кнопка
button2 = KeyboardButton(text='Начало')
kb.add(button)  # добавление кнопки
kb.add(button2)
# kb.row - добавление строки kb.insert - добавление кнопки в конец строки


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # reply_markup - клавиатура
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
