import unittest
import logging
from runner import Runner

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s - %(message)s"

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)
            runner.walk()
            self.assertEqual(runner.distance, -5) 
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    def test_run(self):
        try:
            runner = Runner(123, 10)
            runner.run()
            self.assertEqual(runner.distance, 20) 
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

if __name__ == "__main__":
    unittest.main()