from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# работа с состояниями
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Класс состояний
class UserStates(StatesGroup):
    adress = State()


@dp.message_handler(text='Заказать')
async def buy(message: types.Message):
    await message.answer('Отправь нам свой адрес пожалуйста!')
    # Переход в состояние
    await UserStates.adress.set()


# Логика состояний
@dp.message_handler(state=UserStates.adress)
async def fsm_handler(message: types.Message, state: FSMContext):
    # обновляем состояние
    await state.update_data(first=message.text)
    # записываем состояние в словарь
    data = await state.get_data()
    # отправляем сообщение
    await message.answer(f'Доставка будет отправлена на {data.get("first")}')
    # Выходим из состояний
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
