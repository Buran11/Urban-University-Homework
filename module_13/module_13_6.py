# 2024/01/22 00:00|Домашнее задание по теме "Инлайн клавиатуры".
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
reply_button_calculate = KeyboardButton(text='Рассчитать')
reply_button_info = KeyboardButton(text='Информация')
reply_keyboard_markup.row(reply_button_calculate, reply_button_info)

inline_keyboard_markup = InlineKeyboardMarkup(resize_keyboard=True)
inline_button_calculate = InlineKeyboardButton(
    text='Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton(
    text='Формулы расчёта', callback_data='formulas')
inline_keyboard_markup.add(inline_button_calculate, inline_button_formulas)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=reply_keyboard_markup)


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите действие:', reply_markup=inline_keyboard_markup)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.Message):
    await call.message.answer('М: 10 * вес (кг) + 6.25 * рост (см) – 4.92 * возраст + 5')
    await call.message.answer('Ж: 10 * вес (кг) + 6.25 * рост (см) – 4.92 * возраст - 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.Message):
    await call.message.answer('Введите свой возраст(лет):')
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост(см):')
    await UserStates.growth.set()


@dp.message_handler(state=UserStates.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес(кг):')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'При слабой активности (три тренировки в неделю по 30–60 минут) или ежедневная ходьба пешком не менее часа в день: ')
    await message.answer(f'Калорийность мужчины: {round(((10*int(data.get("weight"))+6.5*int(data.get("growth"))-5*int(data.get("age"))+5)*1.375), 1)}')
    await message.answer(f'Калорийность женшины: {round(((10*int(data.get("weight"))+6.5*int(data.get("growth"))-5*int(data.get("age"))-161)*1.375), 1)}')
    await state.finish()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
