import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print(f"{self.name} is studying")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print(f"{self.name} is sleeping")
        self.gladness += 3

    def to_chill(self):
        print(f"{self.name} is chilling")
        if self.money >= 10:
            self.gladness += 5
            self.progress -= 0.1
            self.money -= 10
        else:
            print(f"{self.name} does not have enough money to chill!")

    def to_work(self):
        print(f"{self.name} is working")
        self.money += 20
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print(f"{self.name} was cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print(f"{self.name} is in depression…")
            self.alive = False
        elif self.progress > 5:
            print(f"{self.name} passed externally…")
            self.alive = False
        elif self.money < 0:
            print(f"{self.name} is bankrupt! Need to work.")
            self.to_work()

    def end_of_day(self):
        print(f"{self.name} - Gladness: {self.gladness}, Progress: {round(self.progress, 2)}, Money: {self.money}")

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:+^50}")

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


students = [Student(name="Nick"), Student(name="Kate"), Student(name="Bohdan")]
for day in range(365):
    for student in students:
        if student.alive:
            student.live(day)
