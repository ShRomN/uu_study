class Product:
    """
    Класс продукта.
    """
    def __init__(self, name:str, weight:float, category:str):
        """
        Конструктор класса Product.
        :param name: название продукта;
        :param weight: общий вес товара;
        :param category: категория товара.
        """
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """
        Метод получения строкового представления объекта.
        """
        return f'{self.name}, {self.weight}, {self.category}'
    
    def __eq__(self, other):
        """
        Перегрузка оператора ==.
        """
        return hash(self) == hash(other)

    def __hash__(self):
        """
        Перегрузка функции __hash__.
        """
        return hash((self.name, self.weight, self.category))


class Shop:
    """
    Класс магазина.
    """
    def __init__(self):
        """
        Конструктор класса Shop.
        """
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Метод считывает все данные из файла с продуктами и возвращает их в виде строки.
        """
        file = open(self.__file_name, 'r')
        out_s = file.read()
        file.close()
        return out_s

    def add(self, *products):
        """
        Метод добавляет новые продукты в файл.
        :param products: параметры с продуктами.
        """
        exist_products = self.get_products()

        # На случай дубликатов
        products = set(products)

        file = open(self.__file_name, 'a')
        for p in products:
            if str(p) in exist_products:
                print(f'Продукт {str(p)} уже есть в магазине')
            else:
                file.write(f'{str(p)}\n')

        file.close()
    

# Тестовые данные
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
