import asyncio

async def start_strongman(name, power):
    """
    Функция имитирующая подъем 5-ти шаров силачем.
    :param name: имя силача;
    :param power: подъёмная мощность силача.
    """
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}' )

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    """
    Функция проведения турнира силачей.
    """
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    
    # Ожидание выполнения задач
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
