from datetime import datetime
from multiprocessing import Pool, Process

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


    # ---------  Многопроцессный-2  ---------
    '''
    При создании вручную 4-х процессов (под каждый файл)
    работает быстрее чем при использовании Pool объекта.
    Примерные показатели времени:
    0:00:18.415831 - Линейный вызов
    0:00:31.000598 - Многопроцессный
    0:00:06.710454 - Многопроцессный-2
    '''
    start_t3 = datetime.now()

    p1 = Process(target=read_info, args=(filenames[0],))
    p2 = Process(target=read_info, args=(filenames[1],))
    p3 = Process(target=read_info, args=(filenames[2],))
    p4 = Process(target=read_info, args=(filenames[3],))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_t3 = datetime.now()

    # Вывод времени выполнения
    print(end_t3 - start_t3)
