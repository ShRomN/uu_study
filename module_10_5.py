from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    """
    Функция построчного считывания файла в массив.
    :param name: название файла для чтения.
    """
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data = file.readlines()
    
    return all_data


# Тестовые данные
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # ---------  Линейный вызов  ----------
    start_t = datetime.now()

    for f_name in filenames:
        read_info(f_name)

    end_t = datetime.now()

    # Вывод времени выполнения
    print(end_t - start_t)


    # ---------  Многопроцессный  ---------
    start_t2 = datetime.now()


    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_t2 = datetime.now()

    # Вывод времени выполнения
    print(end_t2 - start_t2)
