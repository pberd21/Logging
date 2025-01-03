import logging
from runner import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest:
    def test_walk(self):
        """Тест метода walk."""
        try:
            # Создание объекта с отрицательной скоростью
            runner = Runner(name="TestRunner", speed=-1)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        """Тест метода run."""
        try:
            # Создание объекта с некорректным типом имени
            runner = Runner(name=123, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")


if __name__ == "__main__":
    # Запуск тестов
    test = RunnerTest()
    test.test_walk()
    test.test_run()
