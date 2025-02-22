class IterableObject:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += 1

for num in IterableObject(1, 5):
    print(num)

#Задание2

import logging

logging.basicConfig(filename="calculator.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def safe_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            logging.info(f"Expression: {expression}, Result: {result}")
            return result
        except ZeroDivisionError:
            logging.error("Error: Division by zero")
            return "Error: Division by zero"
        except Exception as e:
            logging.error(f"Error: {e}")
            return f"Error: {e}"
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

print(calculate("10 + 5"))
print(calculate("10 / 0"))
print(calculate("2 ** 10"))

#Задание3

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
        self.day = 0

    def to_study(self):
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        self.gladness += 3

    def to_chill(self):
        if self.money >= 10:
            self.gladness += 5
            self.progress -= 0.1
            self.money -= 10
        else:
            return f"{self.name} does not have enough money to chill!"

    def to_work(self):
        self.money += 20
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5 or self.gladness <= 0:
            self.alive = False
        elif self.progress > 5:
            self.alive = False
        elif self.money < 0:
            self.to_work()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.alive:
            raise StopIteration

        self.day += 1
        if self.money < 10:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        else:
            random.choice([self.to_study, self.to_sleep, self.to_chill, self.to_work])()

        self.is_alive()
        return f"Day {self.day}: {self.name} - Progress: {self.progress:.2f}, Money: {self.money}, Gladness: {self.gladness}"

student = Student("Nick")
for day_info in student:
    print(day_info)
