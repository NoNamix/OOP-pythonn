class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"


class Swimmer:
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def swim(self):
        return f"Swimming at {self.swim_speed} m/s"


class Bird:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self):
        return f"Flying at {self.fly_speed} m/s"


class Duck(Animal, Swimmer, Bird):
    def __init__(self, name, swim_speed, fly_speed):
        Animal.__init__(self, name)
        Swimmer.__init__(self, swim_speed)
        Bird.__init__(self, fly_speed)

    def make_sound(self):
        return "Quack!"


donald = Duck("Donald", 2, 10)
print(donald.name)  # Donald
print(donald.make_sound())  # Quack!
print(donald.swim())  # Swimming at 2 m/s
print(donald.fly())  # Flying at 10 m/s


