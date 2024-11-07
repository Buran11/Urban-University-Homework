from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Хэндлеры приёма сообщений
async def urban_message(message: types.Message):
    print('Urban message!')


@dp.message_handler(commands=['start'])  # Реагирует по командам через /
async def start_message(message: types.Message):
    print('Start message!')


@dp.message_handler()  # Реагирует на любое сообщение
async def all_messages(message: types.Message):
    print('Мы получили сообщение!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
