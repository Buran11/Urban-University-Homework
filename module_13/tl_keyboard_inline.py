from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
# ReplyKeyboardMarkup - клавиатура, KeyboardButton - кнопка
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()  # клавиатура
# callback_data - идентификатор
button = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button)  # добавление кнопки

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donat')
        ]
    ], resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer('Рады вас видеть!', reply_markup=kb)
    # await message.answer('Рады вас видеть!', reply_markup=start_menu)


@dp.callback_query_handler(text='info')
async def info(call):
    await call.message.answer('Информация о боте')  # отправляем сообщение
    await call.answer()  # закрываем клавиатуру

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
