import torch

# Функция активации (ступенчатая)
def activation_function(x):
    return 1 if x >= 0 else 0

# Класс персептрона
class Perceptron:
    def __init__(self, num_inputs):
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        self.bias = torch.rand(1, dtype=torch.float64)  # Инициализация смещения случайным значением

    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        return activation_function(torch.sum(inputs * self.weights) + self.bias)

    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        output = self.feed_forward(inputs)
        error = target - output

        # Вывод входов, выходов и ошибки
        # print(f"Входы: {inputs.tolist()} Выход: {int(output)} Ошибка: {error}")

        # Обновление весов и смещения
        self.weights += error * inputs * learning_rate
        self.bias += error * learning_rate


# Класс персептрона 2
class PerceptronXor:
    def __init__(self, num_inputs, h_p1, h_p2):
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        self.bias = torch.rand(1, dtype=torch.float64)  # Инициализация смещения случайным значением
        self.h_p1 = h_p1
        self.h_p2 = h_p2

    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        # return activation_function(torch.sum(torch.tensor([self.h_p1.feed_forward(inputs), self.h_p2.feed_forward(inputs) * (-1)]) * self.weights) + self.bias)
        print(self.h_p1.feed_forward(inputs))
        print(self.h_p2.feed_forward(inputs))

        return activation_function(torch.sum(torch.tensor([self.h_p1.feed_forward(inputs), -self.h_p2.feed_forward(inputs)]) * self.weights) + self.bias)

    # Функция обучения персептрона
    def train(self, inputs, target, learning_rate=0.1):
        output = self.feed_forward(inputs)
        error = target - output

        # Вывод входов, выходов и ошибки
        # print(f"Входы: {inputs.tolist()} Выход: {int(output)} Ошибка: {error}")

        # Обновление весов и смещения
        self.weights += error * inputs * learning_rate
        self.bias += error * learning_rate


# Обучение на исключающей дизъюнкции (XOR)
if __name__ == "__main__":
    # Создание первого скрытого персептрона с двумя входами
    h_perceptron_1 = Perceptron(2)

    # Обучающие данные
    training_inputs_1 = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float64)
    training_outputs_1 = torch.tensor([1, 0, 0, 0], dtype=torch.float64)  # Логическая операция И

    # Обучение первого скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_1, training_outputs_1):
            h_perceptron_1.train(inputs, target)

    # Проверка первого скрытого обученного персептрона
    print('-' * 20)
    print('-----  И (1, 0, 0, 0)  -----')

    for inputs, target in zip(training_inputs_1, training_outputs_1):
        output = h_perceptron_1.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 20)



    # Создание второго скрытого персептрона с двумя входами
    h_perceptron_2 = Perceptron(2)

    # Обучающие данные
    training_inputs_2 = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float64)
    training_outputs_2 = torch.tensor([1, 1, 1, 0], dtype=torch.float64)  # Логическая операция ИЛИ

    # Обучение второго скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_2, training_outputs_2):
            h_perceptron_2.train(inputs, target)

    # Проверка второго скрытого обученного персептрона
    print('-' * 20)
    print('-----  ИЛИ (1, 1, 1, 0)  -----')

    for inputs, target in zip(training_inputs_2, training_outputs_2):
        output = h_perceptron_2.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 20)

    # Создание выходнонго персептрона с двумя входами
    out_perceptron = PerceptronXor(2, h_perceptron_1, h_perceptron_2)

    # Обучающие данные
    training_inputs_3 = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float64)
    training_outputs_3 = torch.tensor([0, 1, 1, 0], dtype=torch.float64)  # Логическая операция ИЛИ

    # Обучение второго скрытого персептрона
    for _ in range(10):
        for inputs, target in zip(training_inputs_3, training_outputs_3):
            out_perceptron.train(inputs, target)

    # Проверка второго скрытого обученного персептрона
    print('-' * 20)
    print('-----  XOR (0, 1, 1, 0)  -----')

    for inputs, target in zip(training_inputs_3, training_outputs_3):
        output = out_perceptron.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 20)
