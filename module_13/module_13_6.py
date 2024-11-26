from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api=''
with open('bot_key.txt', 'r') as f_key:
    api=f_key.readline()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Формируем клавиатуру
kb = ReplyKeyboardMarkup(resize_keyboard=True)
# Формируем кнопки для клавиатуры
btn_1 = KeyboardButton(text='Рассчитать')
btn_2 = KeyboardButton(text='Информация')

# Добавляем кнопки в клавиатуру
kb.add(btn_1)
kb.add(btn_2)

# Формируем inline-клавиатуру
ikb = InlineKeyboardMarkup()
# Формируем кнопки для inline-клавиатуры
ibtn_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ibtn_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

# Добавляем кнопки в inline-клавиатуру
ikb.add(ibtn_1)
ikb.add(ibtn_2)


class UserState(StatesGroup):
    """
    Класс для хранения состояний.
    """
    age = State()
    growth = State()
    weight = State()


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



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
