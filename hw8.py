import random
import logging
import time

logging.basicConfig(filename="simulation.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def error_logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in function {func.__name__}: {e}")
            raise
    return wrapper

class Pet:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
        self.happiness = 50
        self.hungry = 50

    def play(self):
        logging.info(f"{self.name} is playing!")
        self.happiness += 5
        self.hungry -= 5

    def feed(self):
        logging.info(f"{self.name} is eating!")
        self.hungry += 10

    def status(self):
        logging.info(f"{self.name} ({self.type}) - Happiness: {self.happiness}, Hunger: {self.hungry}")

class Student:
    def __init__(self, name, pet=None):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
        self.pet = pet

    @error_logger
    def to_study(self):
        logging.info(f"{self.name} is studying")
        self.progress += 0.12
        self.gladness -= 3

    @error_logger
    def to_sleep(self):
        logging.info(f"{self.name} is sleeping")
        self.gladness += 3

    @error_logger
    def to_chill(self):
        logging.info(f"{self.name} is chilling")
        if self.money >= 10:
            self.gladness += 5
            self.progress -= 0.1
            self.money -= 10
            if self.pet:
                self.pet.play()
        else:
            logging.warning(f"{self.name} does not have enough money to chill!")

    @error_logger
    def to_work(self):
        logging.info(f"{self.name} is working")
        self.money += 20
        self.gladness -= 2

    @error_logger
    def is_alive(self):
        if self.progress < -0.5:
            logging.info(f"{self.name} was cast out…")
            self.alive = False
        elif self.gladness <= 0:
            logging.info(f"{self.name} is in depression…")
            self.alive = False
        elif self.progress > 5:
            logging.info(f"{self.name} passed externally…")
            self.alive = False
        elif self.money < 0:
            logging.info(f"{self.name} is bankrupt! Need to work.")
            self.to_work()

    @error_logger
    def end_of_day(self):
        logging.info(f"{self.name} - Gladness: {self.gladness}, Progress: {round(self.progress, 2)}, Money: {self.money}")
        if self.pet:
            self.pet.status()

    @timing_decorator
    @error_logger
    def live(self, day):
        day_log = f"Day {day} of {self.name}'s life"
        logging.info(day_log)

        if self.money < 10:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_work()

        self.end_of_day()
        self.is_alive()

@timing_decorator
def test_function():
    time.sleep(0.5)

pet1 = Pet(name="Fluffy", type_="Cat")
pet2 = Pet(name="Buddy", type_="Dog")

students = [Student(name="Nick", pet=pet1), Student(name="Kate", pet=pet2), Student(name="Bohdan")]

for day in range(365):
    for student in students:
        if student.alive:
            student.live(day)

test_function()
