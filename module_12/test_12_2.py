from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    """
    Класс тестирования работы класса Tournament.
    """
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

    @classmethod
    def tearDownClass(self):
        """
        Метод вывода результатов тестирования по окончанию всех тестов.
        """
        print(*self.all_results.values(), sep='\n')
        
    def test_tournament_1(self):
        """
        Метод тестирования работы первого турнира класса Tournament.
        """
        trmnt1 = Tournament(90, self.rn1, self.rn3)
        self.all_results['test_tournament_1'] = trmnt1.start()
        self.assertTrue(self.all_results['test_tournament_1'][max(self.all_results['test_tournament_1'])] == self.rn3)
        
    def test_tournament_2(self):
        """
        Метод тестирования работы второго турнира класса Tournament.
        """
        trmnt2 = Tournament(90, self.rn2, self.rn3)
        self.all_results['test_tournament_2'] = trmnt2.start()
        self.assertTrue(self.all_results['test_tournament_2'][max(self.all_results['test_tournament_2'])] == self.rn3)

    def test_tournament_3(self):
        """
        Метод тестирования работы третьего турнира класса Tournament.
        """
        trmnt3 = Tournament(90, self.rn1, self.rn2, self.rn3)
        self.all_results['test_tournament_3'] = trmnt3.start()
        self.assertTrue(self.all_results['test_tournament_3'][max(self.all_results['test_tournament_3'])] == self.rn3)


if __name__ == '__main__':
    unittest.main()
