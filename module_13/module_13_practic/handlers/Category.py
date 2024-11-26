import texts.category
from keyboards import catalog_kb, buy_kb


async def price(message):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await message.answer(texts.category.what_dyw, reply_markup=catalog_kb)


async def buy_m(call):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await call.message.answer(texts.category.Mgame, reply_markup=buy_kb)
    await call.answer()


async def buy_l(call):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await call.message.answer(texts.category.Lgame, reply_markup=buy_kb)
    await call.answer()


async def buy_xl(call):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await call.message.answer(texts.category.XLgame, reply_markup=buy_kb)
    await call.answer()


async def buy_other(call):
    """
    Функция вывода стоимости при нажатии на кнопку - 'Стоимость'.
    """
    await call.message.answer(texts.category.other, reply_markup=buy_kb)
    await call.answer()
