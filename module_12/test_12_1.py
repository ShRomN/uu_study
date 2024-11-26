from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    """
    Класс тестирования работы класса Runner.
    """
    def test_walk(self):
        """
        Метод тестирования работы метода walk объекта класса Runner.
        """
        rn1 = Runner('Пешеход_1')
        
        for _ in range(10):
            rn1.walk()

        # self.assertEqual(rn1.distance, 51)
        self.assertEqual(rn1.distance, 50)


    def test_run(self):
        """
        Метод тестирования работы метода run объекта класса Runner.
        """
        rn2 = Runner('Бегун_2')
        
        for _ in range(10):
            rn2.run()

        self.assertEqual(rn2.distance, 100)

    def test_challenge(self):
        """
        Метод тестирования совместной работы методов run и walk объекта класса Runner.
        """
        rn3 = Runner('Спортсмен_3')
        
        for _ in range(10):
            rn3.run()
            rn3.walk()

        self.assertNotEqual(rn3.distance, 100)


if __name__ == '__main__':
    unittest.main()
