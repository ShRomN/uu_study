import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import *

import handlers.Start
import handlers.Category


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


dp.message_handler(commands=['start'])(handlers.Start.start)
dp.message_handler(text=['О нас'])(handlers.Start.info)

dp.message_handler(text=['Стоимость'])(handlers.Category.price)
dp.callback_query_handler(text=['medium'])(handlers.Category.buy_m)
dp.callback_query_handler(text=['big'])(handlers.Category.buy_l)
dp.callback_query_handler(text=['mega'])(handlers.Category.buy_xl)
dp.callback_query_handler(text=['other'])(handlers.Category.buy_other)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
