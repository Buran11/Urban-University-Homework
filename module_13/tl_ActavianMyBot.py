from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Хэндлеры приёма сообщений
# Реагирует на текст сообщения Urban и ff
@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message: types.Message):
    print('Urban message!')
    # В ответ получаем сообщение Urban message!
    await message.answer('Urban message!')


# Реагирует по командам через /
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print('Start message!')
    # В ответ получаем сообщение Рады вас видеть в нашем боте!
    await message.answer('Рады вас видеть в нашем боте!')


# Реагирует на любое сообщение
@dp.message_handler()
async def all_messages(message: types.Message):
    print('Мы получили сообщение!')
    # echo bot В ответ получаем сообщение Ваше сообщение в верхнем регистре!
    await message.answer(message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
