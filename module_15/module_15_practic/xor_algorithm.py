import torch

def activation_function(x):
    """
    Ступенчатая функция активации.
    :param x: проверяемое значение.
    :return: 1 если x >= 0 иначе 0.
    """
    return 1 if x >= 0 else 0

class Perceptron:
    """
    Класс описывающий персептрон для AND и OR.
    """
    def __init__(self, num_inputs):
        """
        Конструктор класса Perceptron.
        :param num_inputs: количество входных сигналов.
        """
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        # Инициализация смещения случайным значением
        self.bias = torch.rand(1, dtype=torch.float64)

    def feed_forward(self, inputs):
        """
        Метод вычисляющий выходное значение персептрона на основании
        входных данных (inputs) с использованием функции активации.
        Атрибуты:
        :param inputs: входные данные.
        :return: значение пропущенное через функцию активации (1 или 0).
        """
        return activation_function(torch.sum(inputs * self.weights) + self.bias)

    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        """
        Метод обучения персептрона на основании входных данных (inputs) и 
        целевых значений с корректировкой весов в соответствии с
        шагом обучения (learning_rate).
        Атрибуты:
        :param inputs: входные данные;
        :param target: целевое значение;
        :param learning_rate: шаг обучения.
        """
        # Вычисляем выходное значение персептрона с текущими весами
        output = self.feed_forward(inputs)
        # Вычисляем расхождение текущего значение с целевым значением
        error = target - output

        # Обновление весов
        self.weights += error * inputs * learning_rate
        # Обновление смещения
        self.bias += error * learning_rate


# Класс персептрона XOR
class PerceptronXor:
    """
    Класс описывающий персептрон для XOR.
    """
    def __init__(self, num_inputs, h_p1, h_p2):
        """
        Конструктор класса PerceptronXor.
        :param num_inputs: количество входных сигналов;
        :param h_p1: объект скрытого слоя - обученный персептрон AND;
        :param h_p2: объект скрытого слоя - обученный персептрон OR.
        """
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        # Зададим отрицательный знак для второго веса (для лучшего обучения)
        self.weights[1] *= -1
        # Инициализация смещения случайным значением
        self.bias = torch.rand(1, dtype=torch.float64)
        # Инициализация персептронов скрытого слоя
        self.h_p1 = h_p1
        self.h_p2 = h_p2

    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        """
        Метод вычисляющий выходное значение персептрона XOR на основании
        входных данных (inputs) с использованием обученных персептронов
        скрытого слоя и функции активации.
        Атрибуты:
        :param inputs: входные данные.
        :return: значение пропущенное через функцию активации (1 или 0).
        """
        # print('AND - ', self.h_p1.feed_forward(inputs))
        # print('OR - ', self.h_p2.feed_forward(inputs))
        # print('weights - ', self.weights)
        # print('bias - ', self.bias)
        return activation_function(torch.sum(torch.tensor([self.h_p2.feed_forward(inputs), self.h_p1.feed_forward(inputs)]) * self.weights) + self.bias)
    

    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        """
        Метод обучения персептрона на основании входных данных (inputs) и 
        целевых значений с корректировкой весов в соответствии с
        шагом обучения (learning_rate).
        Атрибуты:
        :param inputs: входные данные;
        :param target: целевое значение;
        :param learning_rate: шаг обучения.
        """
        # Вычисляем выходное значение персептрона с текущими весами
        output = self.feed_forward(inputs)
        # Вычисляем расхождение текущего значение с целевым значением
        error = target - output

        # Обновление весов
        self.weights += error * inputs * learning_rate
        # Обновление смещения
        self.bias += error * learning_rate


# # Класс персептрона XOR (вариант - 2 с подобоанными весами и смещением без обучения)
# class PerceptronXor:
#     """
#     Класс описывающий персептрон для XOR.
#     """
#     def __init__(self, h_p1, h_p2):
#         """
#         Конструктор класса PerceptronXor.
#         :param h_p1: объект скрытого слоя - обученный персептрон AND;
#         :param h_p2: объект скрытого слоя - обученный персептрон OR.
#         """
#         # Инициализация весов расчитанными значениями
#         self.weights = torch.tensor([-1, 1], dtype=torch.float64)
#         # Инициализация смещения расчитанными значениями
#         self.bias = torch.tensor([-0.5,], dtype=torch.float64)
#         # Инициализация персептронов скрытого слоя
#         self.h_p1 = h_p1
#         self.h_p2 = h_p2

#     def feed_forward(self, inputs):
#         """
#         Метод вычисляющий выходное значение персептрона XOR на основании
#         входных данных (inputs) с использованием обученных персептронов
#         скрытого слоя и функции активации.
#         Атрибуты:
#         :param inputs: входные данные.
#         :return: значение пропущенное через функцию активации (1 или 0).
#         """
#         return activation_function(torch.sum(torch.tensor([self.h_p1.feed_forward(inputs), self.h_p2.feed_forward(inputs)]) * self.weights) + self.bias)



# Обучение на исключающей дизъюнкции (XOR)
if __name__ == "__main__":
    # -------------  Создание первого скрытого персептрона с двумя входами  -------------
    h_perceptron_1 = Perceptron(2)

    # Обучающие данные
    training_inputs_1 = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float64)
    training_outputs_1 = torch.tensor([1, 0, 0, 0], dtype=torch.float64)  # Логическая операция И

    # Обучение первого скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_1, training_outputs_1):
            h_perceptron_1.train(inputs, target)

    # Проверка обученного первого скрытого обученного персептрона
    print('-----  И (1, 0, 0, 0)  -----')
    for inputs, target in zip(training_inputs_1, training_outputs_1):
        output = h_perceptron_1.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 30)
    # -----------------------------------------------------------------------------------

    # -------------  Создание второго скрытого персептрона с двумя входами  -------------
    h_perceptron_2 = Perceptron(2)

    # Обучающие данные
    training_inputs_2 = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float64)
    training_outputs_2 = torch.tensor([1, 1, 1, 0], dtype=torch.float64)  # Логическая операция ИЛИ

    # Обучение второго скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_2, training_outputs_2):
            h_perceptron_2.train(inputs, target)

    # Проверка обученного второго скрытого обученного персептрона
    print('-----  ИЛИ (1, 1, 1, 0)  -----')
    for inputs, target in zip(training_inputs_2, training_outputs_2):
        output = h_perceptron_2.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 30)
    # -----------------------------------------------------------------------------------

    # -------------  Создание выходнонго персептрона (XOR) с двумя входами  -------------
    out_perceptron = PerceptronXor(2, h_perceptron_1, h_perceptron_2)

    # Обучающие данные
    training_inputs_3 = torch.tensor([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=torch.float64)
    training_outputs_3 = torch.tensor([0, 1, 1, 0], dtype=torch.float64)  # Логическая операция ИЛИ

    # Обучение второго скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_3, training_outputs_3):
            out_perceptron.train(inputs, target, 0.1)

    # Проверка второго скрытого обученного персептрона
    print('-----  XOR (0, 1, 1, 0)  -----')
    for inputs, target in zip(training_inputs_3, training_outputs_3):
        output = out_perceptron.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 30)
    # -----------------------------------------------------------------------------------
