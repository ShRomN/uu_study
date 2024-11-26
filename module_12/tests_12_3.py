import unittest
from runner_and_tournament import Runner, Tournament

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
        rn1 = Runner('Пешеход_1')
        
        for _ in range(10):
            rn1.walk()

        self.assertEqual(rn1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Метод тестирования работы метода run объекта класса Runner.
        """
        rn2 = Runner('Бегун_2')
        
        for _ in range(10):
            rn2.run()

        self.assertEqual(rn2.distance, 100)
    
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


class TournamentTest(unittest.TestCase):
    """
    Класс тестирования работы класса Tournament.
    """
    is_frozen = True

    @classmethod
    def setUpClass(self):
        """
        Метод формирования начальных установок для тестирования.
        """
        self.all_results = {}


    def setUp(self):
        """
        Метод инициализации объектов при каждом запуске одного из тестов.
        """
        self.rn1 = Runner('Усэйн', 10)
        self.rn2 = Runner('Андрей', 9)
        self.rn3 = Runner('Ник', 3)

    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        """
        Метод тестирования работы первого турнира класса Tournament.
        """
        trmnt1 = Tournament(90, self.rn1, self.rn3)
        self.all_results['test_tournament_1'] = trmnt1.start()
        self.assertTrue(self.all_results['test_tournament_1'][max(self.all_results['test_tournament_1'])] == self.rn3)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        """
        Метод тестирования работы второго турнира класса Tournament.
        """
        trmnt2 = Tournament(90, self.rn2, self.rn3)
        self.all_results['test_tournament_2'] = trmnt2.start()
        self.assertTrue(self.all_results['test_tournament_2'][max(self.all_results['test_tournament_2'])] == self.rn3)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        """
        Метод тестирования работы третьего турнира класса Tournament.
        """
        trmnt3 = Tournament(90, self.rn1, self.rn2, self.rn3)
        self.all_results['test_tournament_3'] = trmnt3.start()
        self.assertTrue(self.all_results['test_tournament_3'][max(self.all_results['test_tournament_3'])] == self.rn3)
