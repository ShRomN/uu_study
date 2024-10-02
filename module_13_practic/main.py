import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *
from keyboards import *
import texts


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    """
    Стартовая функция реагирующая на команду start
    выводящяя пользователю приветственное сообщение
    и разметку клавиатуры.
    """
    await message.answer(texts.start, reply_markup=start_kb)


@dp.message_handler(text=['О нас'])
async def info(message):
    """
    Функция вывода информации при нажатии на кнопку - 'О нас'.
    """
    await message.answer(texts.about, reply_markup=start_kb)


@dp.message_handler(text=['Стоимость'])
async def price(message):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await message.answer(texts.what_dyw, reply_markup=catalog_kb)










if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
