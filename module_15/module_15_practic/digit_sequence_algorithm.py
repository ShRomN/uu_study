import torch

# Функция активации (ступенчатая)
def activation_function(x):
    """
    Ступенчатая функция округления.
    :param x: проверяемое значение.
    :return: округленное значение.
    """
    # return 0 if torch.round(x) <= 1 else 1
    return int(torch.round(x))

class Perceptron:
    """
    Класс описывающий персептрон для определения числа в последовательности.
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
        :return: значение пропущенное через функцию активации.
        """
        return activation_function(torch.sum(inputs * self.weights) + self.bias)

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

        # Вывод входов, выходов и ошибки
        print(f"Входы: {inputs.tolist()} | Выход: {int(output)} | Ошибка: {int(error)}")

        # Обновление весов
        self.weights += error * inputs * learning_rate
        # Обновление смещения
        self.bias += error * learning_rate


# Основная функция
if __name__ == "__main__":
    # Создание персептрона с тремя входами
    perceptron = Perceptron(3)

    # Генерация последовательности из 25 целых десятичных чисел от 0 до 1
    sequence = torch.randint(0, 2, (25,), dtype=torch.float64)
    print(type(sequence))

    # Вывод сгенерированной последовательности
    print("Сгенерированная последовательность:")
    for i, item in enumerate(sequence):
        # print(type(item))
        # print(item.item())

        print(f"Число {i + 1}: {int(item.item())}")

    # Обучение персептрона для каждых трех чисел в последовательности в нескольких циклах 
    total_error = 0
    epochs = 10
    for _ in range(epochs):
        for i in range(3, len(sequence)):
            input_data = torch.tensor([sequence[i - 3].item(), sequence[i - 2].item(), sequence[i - 1].item()])
            target = sequence[i].item()
            perceptron.train(input_data, target)
            total_error += abs(target - perceptron.feed_forward(input_data))

    average_train_error = total_error / ((len(sequence) - 3) * epochs)
    print(f"Средняя ошибка обучения: {average_train_error:.2f}")

    # Проверка обученного персептрона
    print("Проверка обученного персептрона:")
    total_error = 0
    for i in range(3, len(sequence)):
        input_data = torch.tensor([sequence[i - 3].item(), sequence[i - 2].item(), sequence[i - 1].item()])
        target = sequence[i].item()
        output = perceptron.feed_forward(input_data)
        error = abs(target - output)
        total_error += error
        print(f"Входы: {input_data.tolist()} | Ожидаемый вывод: {int(target)} | Предсказанный вывод: {int(output)} | Ошибка: {int(error)}")

    average_test_error = total_error / (len(sequence) - 3)
    print(f"Средняя ошибка обучения: {average_train_error:.2f}")
