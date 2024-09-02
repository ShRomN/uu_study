from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    """
    Функция записи слов в файл.
    :param word_count: количество записываемых слов;
    :param file_name: название файла, куда будут записываться слова.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}')

    sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


# Тестовые данные
# ----  Работа функции в один поток (последовательно)  ----
# Засекаем время начала выполнения
st_without_t = datetime.now()

# Выполнение функции в один поток
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Засекаем время окончания выполнения
et_without_t = datetime.now()
# Выводим время работы
print('Работа без потоков:', et_without_t - st_without_t)

# -------  Работа функции в 4 потока (параллельно)  -------
# Создаем объекты потоков
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

# Засекакм время начала выполнения
st_with_t = datetime.now()

# Запускаем потоки на исполнение
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# Дожидаемся выполнения потоков
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

# Засекаем время окончания выполнения
et_with_t = datetime.now()
# Выводим время работы
print('Работа потоков:', et_with_t - st_with_t)
