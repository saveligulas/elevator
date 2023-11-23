from random import Random

from faker import Faker

from floor import Floor

fake = Faker()
random = Random()


class Human:
    def __init__(self, name=None, age=None):
        if name is None:
            self.name = fake.name()
        else:
            self.name = name

        if age is None:
            self.age = random.randint(1, 99)

        self.desired_floor: Floor = Floor(-1)

    def __str__(self):
        return f"{self.name} ({self.desired_floor.level})"

    @staticmethod
    def get_humans(amount):
        return [Human() for i in range(amount)]
