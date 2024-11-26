import unittest
import logging
from rt_with_exceptions import Runner, Tournament

class RunnerTest(unittest.TestCase):
    """
    Класс тестирования работы класса Runner.
    """
    is_frozen = False
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')    
    def test_walk(self):
        """
        Метод тестирования работы метода walk объекта класса Runner.
        """
        try:
            rn1 = Runner('Пешеход_1', -5)
            
            for _ in range(10):
                rn1.walk()

            self.assertEqual(rn1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        
        except Exception as e:
            logging.warning('Неверная скорость для Runner')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Метод тестирования работы метода run объекта класса Runner.
        """
        try:
            rn2 = Runner(12)
            
            for _ in range(10):
                rn2.run()

            self.assertEqual(rn2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')
    
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        Метод тестирования совместной работы методов run и walk объекта класса Runner.
        """
        rn3 = Runner('Спортсмен_3')
        
        for _ in range(10):
            rn3.run()
            rn3.walk()

        self.assertNotEqual(rn3.distance, 100)


if __name__=='__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename='runner_tests.log',
        filemode='w',
        encoding='utf-8',
        format='%(asctime)s | %(levelname)s | %(message)s | модуль из которого был вызов записи в лог - %(module)s | строка вызова записи в лог файл - %(lineno)s'
    )
    unittest.main()
