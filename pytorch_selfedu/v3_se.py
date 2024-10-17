# Урок по 3-иу видео
# https://rutube.ru/video/6b82bca0de1bab615aac8434ea28e1f4/?playlist=567721&playlistPage=1

import torch
import numpy as np

# Проверка доступности CUDA (процессора видеокарты)
print(torch.cuda.is_available())

# Создем тензор многомерный массив
# состоящий из 3-х списков в каждом
# из которых содержится по 5-списков
# с 2-мя элементами
t1 = torch.Tensor(3, 5, 2)
print('t1 -', t1)
print('t1.dtype -', t1.dtype)

# Создем тензор многомерный массив с
# использованием функции - torch.tensor()
# состоящий из 3-х списков в каждом
# из которых содержится по 5-списков
# с 2-мя элементами, каждый из которых
# имеет тип - torch.float64, так же указан
# место хранения тензора (cpu)
t2 = torch.tensor([3, 5, 2], dtype=torch.float64)
print('t2 -', t2)
print('t2.dtype -', t2.dtype)

# Вывод кол-ва осей тензора
print('t1.dim() -', t1.dim())
# print(t2.size())

# Вывод размера тензора по каждой из осей
print('t1.size() -', t1.size())
print('t1.shape -', t2.shape)

# Создание тензора из numpy массива
d_np = np.array([[1, 2, 3], [4, 5, 6]])
# При изменении тензора будет изменятся массив-numpy,
# если использовать функцию - torch.from_numpy()
t3 = torch.from_numpy(d_np)
print('t3 -', t3)
print('t3.dtype -', t3.dtype)
# При изменении тензора будет массив-numpy будет неизменен,
# так как тензор делается на копии данных,
# если использовать функцию - torch.tensor()
t4 = torch.tensor(d_np)
print('t4 -', t4)
print('t4.dtype -', t4.dtype)

# Создание из тензора numpy-массива
d_np2 = t4.numpy()
print('type(d_np2) -', type(d_np2))
print('d_np2 -', d_np2)

# Преобразование данных в тензоре
# half(), float(), double(), short() ...
t5 = t1.float()
print('t5 -', t5)
print('t5.dtype -', t5.dtype)
