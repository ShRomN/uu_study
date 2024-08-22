import os, time

directory = '.'
# Используем os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # Применяем os.path.join для формирования полного пути к файлу
        filepath = os.path.join(root, file)
        # Используем os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Используем os.path.getsize для получения размера файла
        filesize = os.path.getsize(filepath)
        # Используем os.path.dirname для получения родительской директории файла
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        