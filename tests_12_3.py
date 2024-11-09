import module_12_2 as m_12_2
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):

        cls.all_results = {}
    def setUp(self):
        self.usein = m_12_2.Runner("Усэйн", 10)
        self.andrey = m_12_2.Runner("Андрей", 9)
        self.nick = m_12_2.Runner("Ник", 3)
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race_usein_nick(self):
        tournament = m_12_2.Tournament(93, self.usein, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_nick(self):
        tournament = m_12_2.Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race_usein_andrey_nick(self):
        tournament = m_12_2.Tournament(90, self.usein, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(False, '')
    def test_walk(self):
        runner = m_12_2.Runner("Runner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    @unittest.skipIf(False, '')
    def test_run(self):
        runner = m_12_2.Runner("Runner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    @unittest.skipIf(False, '')
    def test_challenge(self):
        runner1 = m_12_2.Runner("Runner3")
        runner2 = m_12_2.Runner("Runner4")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()