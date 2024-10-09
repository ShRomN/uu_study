import texts.start
from keyboards import start_kb

async def start(message):
    """
    Стартовая функция реагирующая на команду start
    выводящяя пользователю приветственное сообщение
    и разметку клавиатуры.
    """
    await message.answer(texts.start.start, reply_markup=start_kb)


async def info(message):
    """
    Функция вывода информации при нажатии на кнопку - 'О нас'.
    """
    await message.answer(texts.start.about, reply_markup=start_kb)
