def test_function():
    """
    Тестовая функция
    """
    def inner_function():
        """
        Внутренняя функция
        """
        print("Я в области видимости функции test_function")
    
    # Вызов функции inner_function внутри функции test_function
    inner_function()


# Вызов функции test_function
test_function()

# Попытка вызывать inner_function вне функции test_function
# inner_function()
