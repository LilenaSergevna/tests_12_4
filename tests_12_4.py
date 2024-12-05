import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            tst=Runner("Тест",-10)
            sum=0
            for i in range(10):
                tst.walk()
            self.assertEqual(tst.distance,50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            tst=Runner(123)
            sum=0
            for i in range(10):
                tst.run()
            self.assertEqual(tst.distance,100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge (self):
        tst_1=Runner("Тест 1")
        tst_2=Runner("Тест 2")
        sum=0
        for i in range(10):
            tst_1.walk()
            tst_2.run()
        self.assertNotEqual(tst_1.distance,tst_2.distance)

if __name__=="__main__":
    unittest.main

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)
t = Tournament(101, first, second)
print(t.start())