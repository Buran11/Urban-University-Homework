# 2024/02/01 00:00|Домашнее задание по теме "План написания админ панели"
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import *  # MODULE_14_4
'''
Префиксы в именах экземпляров класса:
rkb_ - reply keyboard, ikb_ - inline keyboard
rb_ - reply button, ib_ - inline button
'''


# Bot
api = '7663349655:AAGezQpU1w27WnIbSU0-Z7xwE4LdS38j33U'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Keyboards
rkb_markup = ReplyKeyboardMarkup(resize_keyboard=True)
ikb_markup = InlineKeyboardMarkup(resize_keyboard=True)
ikb_products = InlineKeyboardMarkup(resize_keyboard=True)


# Buttons
rb_calculate = KeyboardButton(text='Рассчитать')
rb_info = KeyboardButton(text='Информация')
rb_buy = KeyboardButton(text='Купить')
ib_calculate = InlineKeyboardButton(
    text='Рассчитать норму калорий', callback_data='calories')
ib_formulas = InlineKeyboardButton(
    text='Формулы расчёта', callback_data='formulas')
ib_Product1 = InlineKeyboardButton(
    text='Product1', callback_data='product_buying')
ib_Product2 = InlineKeyboardButton(
    text='Product2', callback_data='product_buying')
ib_Product3 = InlineKeyboardButton(
    text='Product3', callback_data='product_buying')
ib_Product4 = InlineKeyboardButton(
    text='Product4', callback_data='product_buying')


# Adding buttons to Keyboards
rkb_markup.row(rb_calculate, rb_info)
rkb_markup.add(rb_buy)
ikb_markup.add(ib_calculate, ib_formulas)
ikb_products.row(ib_Product1, ib_Product2,
                 ib_Product3, ib_Product4)


# FSM 'Formulas callories'
class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# ORM sqlite
def orm_add_product():  # MODULE_14_4
    initiate_db()
    for i in range(1, 5):
        add_product(f'Product{i}', f'description{i}', f'{i * 100}')


# Handler commands to start menu
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=rkb_markup)


# Handlers for FSM 'Formulas callories'
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите действие:', reply_markup=ikb_markup)


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


# Handlers 'Buy product'
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.Message):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):  # MODULE_14_4
    product = get_all_products()
    for i in range(1, 5):
        await message.answer(f'Название: {product[i-1][1]} | Описание: {product[i-1][2]} | Цена: {product[i-1][3]}₽')
        with open(f'./files/0{i}.png', 'rb') as img:
            await message.answer_photo(img, reply_markup=rkb_markup)
    await message.answer('Выберите продукт:', reply_markup=ikb_products)


# Handler default
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение')


# Run
if __name__ == '__main__':
    orm_add_product()  # MODULE_14_4
    executor.start_polling(dp, skip_updates=True)
