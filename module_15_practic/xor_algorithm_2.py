import torch

# Функция активации (ступенчатая)
def activation_function(x):
    return 1 if x >= 0 else 0

# Класс персептрона XOR
class PerceptronXor:
    def __init__(self, num_inputs):
        # Инициализация весов случайными значениями
        self.weights = torch.rand(num_inputs, dtype=torch.float64)
        # Инициализация смещения случайным значением
        self.bias = torch.rand(1, dtype=torch.float64)

    # Функция, вычисляющая выход персептрона
    def feed_forward(self, inputs):
        # return activation_function(torch.sum(torch.tensor([self.h_p1.feed_forward(inputs), self.h_p2.feed_forward(inputs) * (-1)]) * self.weights) + self.bias)
        print('weights - ', self.weights)
        print('bias - ', self.bias)


        # return activation_function(torch.sum(torch.tensor([self.h_p1.feed_forward(inputs), -self.h_p2.feed_forward(inputs)]) * self.weights) + self.bias)
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



# Обучение на исключающей дизъюнкции (XOR)
if __name__ == "__main__":
    # Создание выходнонго персептрона с двумя входами
    out_perceptron = PerceptronXor(2)

    # Обучающие данные
    training_inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float64)
    training_outputs = torch.tensor([0, 1, 1, 0], dtype=torch.float64)  # Логическая операция ИЛИ

    # Обучение второго скрытого персептрона
    for i in range(10):
        print('-' * 5, i, '-' * 5)
        for inputs, target in zip(training_inputs, training_outputs):
            out_perceptron.train(inputs, target, 0.1)
        print('-' * 14)
        
    # Проверка второго скрытого обученного персептрона
    print('-' * 20)
    print('-----  XOR (0, 1, 1, 0)  -----')

    for inputs, target in zip(training_inputs, training_outputs):
        output = out_perceptron.feed_forward(inputs)
        print(f"Входы: {inputs.tolist()} Выход: {int(output)}")
    print('-' * 20)
