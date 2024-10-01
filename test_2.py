from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


api=''
with open('bot_key.txt', 'r') as f_key:
    api=f_key.readline()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



kb = ReplyKeyboardMarkup()
btn_1 = KeyboardButton(text='Информация')
btn_2 = KeyboardButton(text='Начало')

kb.add(btn_1)
kb.add(btn_2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer('Информация о боте')

# kb.row, bb.insert




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

