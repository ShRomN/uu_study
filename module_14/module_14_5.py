from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import *

# Инициализируем базу.
initiate_db()
# Получаем все продукты и их описание из базы
products = get_all_products()

api=''
with open('bot_key.txt', 'r') as f_key:
    api=f_key.readline()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Формируем клавиатуру
kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Регистрация')
        ]
    ],
    resize_keyboard=True
)

# Формируем inline-клавиатуру
ikb = InlineKeyboardMarkup(
    [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    ]
)

# Формируем inline-клавиатуру с продуктами
ikb_products = InlineKeyboardMarkup(
    inline_keyboard =
    [
        [
        InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    """
    Класс для хранения состояний пользователя.
    """
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    """
    Класс для хранения состояний регистрации пользователя.
    """
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start(message):
    """
    Стартовая функция реагирующая на команду start
    выводящяя пользователю приветственное сообщение
    и разметку клавиатуры.
    """
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    """
    Функция вывода inline-меню при получения сообщения
    нажатия на кнопку - 'Рассчитать'.
    """
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    """
    Функция запуска цепочки сообщений (1-функция цепочки).
    """
    await call.message.answer('Введите свой возраст:')
    # Запуск следующей функции в цепочке
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    """
    Функция устанавливающая значение переменной age в классе
    машины состояний и запуска следующего по цепочке сообщений
    (2-функция цепочки).
    """
    # Установка значения в переменную age
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    # Запуск следующей функции в цепочке
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    """
    Функция устанавливающая значение переменной growth в классе
    машины состояний и запуска следующего по цепочке сообщений
    (3-функция цепочки).
    """
    # Установка значения в переменную growth
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    # Запуск следующей функции в цепочке
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    """
    Функция устанавливающая значение переменной weight в классе
    машины состояний, после чего соберает данные из машины состояний
    и производит вычисления с выводом информации пользователю
    (4-функция (последняя) цепочки).
    """
    # Установка значения в переменную weight
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    # Расчет значения каллорийности по формуле
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    # Выводим значение пользователю обратным сообщением
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    """
    Функция вывода пользователю используемой формулы
    расчета калорийности при нажатии на кнопку
    'Формулы расчёта' в inline-меню.
    """
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    """
    Функция вывода списка товаров и их изображений.
    """
    for product in products:
        with open(f'product_{product[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')

    await message.answer('Выберите продукт для покупки:', reply_markup=ikb_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    """
    Функция вывода информации об успешности совершенной покупки.
    """
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    """
    Функция начального запуска цепочки сообщений при нажатии на
    кнопку регистрации нового пользователя (реакция на нажатие
    на кнопку - 'Регистрация').
    """
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    # Запуск следующей функции в цепочке
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    """
    Функция устанавливающая значение переменной username в классе
    машины состояний RegistrationState и запускает следующее по
    цепочке сообщение (1-функция цепочки) или запрос повторного ввода.
    """
    # Проверяем наличие пользователя в БД
    # Если пользователя нет
    if not is_included(message.text):
        # Установка значения в переменную username
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    
    # Если пользователя c данным именем есть
    else:
        # Запуск следующей функции в цепочке
        await message.answer('Пользователь существует, введите другое имя:')
        # Повторный запуск это же функции
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    """
    Функция устанавливающая значение переменной email в классе
    машины состояний RegistrationState и запускает следующее по
    цепочке сообщение (2-функция цепочки).
    """
    # Установка значения в переменную email
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()
    

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    """
    Функция устанавливающая значение переменной age в классе
    машины состояний RegistrationState добавляет данные о
    новом пользователе в БД и выводит информационное сообщение
    о успешности регистрации нового пользователя (3-функция цепочки).
    """
    # Установка значения в переменную email
    await state.update_data(age=int(message.text))
    # Установка значения в переменную balance
    await state.update_data(balance=1000)

    data = await state.get_data()
    # print(data)
    add_user(**data)

    await message.answer('Регистрация прошла успешно!')
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)