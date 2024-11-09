import tests_12_3
import unittest
import inspect

suit = unittest.TestSuite()
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit)