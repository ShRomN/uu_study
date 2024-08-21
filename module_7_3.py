from re import findall

class WordsFinder:
    """
    Класс WordsFinder.
    """
    def __init__(self, *args):
        """
        Конструктор класса Product.
        :param args: кортеж параметров с именами файлов.
        """
        self.file_names = args

    def get_all_words (self):
        """
        Метод получения словаря с именем файла в качестве ключа и списком слов в качестве значения.
        :return: словаря с именем файла в качестве ключа и списком слов в качестве значения.
        """
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                all_words[file_name] = findall(r"[a-zA-Zа-яА-Я']+", file.read().lower())

        return all_words

    def find(self, word):
        """
        Метод поиска слова по файлам.
        :param word: искомое слово в файлах;
        :return: словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
        """
        # for fn, words in self.get_all_words().items():

        return dict(map(lambda x: (x[0], x[1].index(word.lower()) + 1), self.get_all_words().items()))

    def count(self, word):
        """
        Метод подсчета кол-ва повторений искомого слова.
        :param word: искомое слово в файлах;
        :return: словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
        """
        return dict(map(lambda x: (x[0], x[1].count(word.lower())), self.get_all_words().items()))


# Тестовые данные
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
