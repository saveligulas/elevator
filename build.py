from typing import List

from colorama import Fore, Back

from elevator import Elevator
from floor import Floor
import random

from human import Human


def _random_int_excluding(start, end, exclude):
    value = random.randint(start, end - 1)
    while value == exclude:
        value = random.randint(start, end - 1)
    return value


class Building:
    def __init__(self, inhabitants, stories):
        self._inhabitants: List[Human] = inhabitants
        self._elevator = Elevator()
        self._floors = [Floor(level) for level in range(stories)]
        self._elevator.floor = self._floors[0]
        self._assign_inhabitants_to_elevator_and_floors()

    def _assign_inhabitants_to_elevator_and_floors(self):
        for inhabitant in self._inhabitants:
            if random.choice([True, False]):
                inhabitant.desired_floor = self._floors[random.randint(1, len(self._floors) - 1)]
                self._elevator.append_passenger(inhabitant)
            else:
                floor_to_assign = random.randint(1, len(self._floors) - 1)
                inhabitant.desired_floor = self._floors[_random_int_excluding(0, len(self._floors), floor_to_assign)]
                self._floors[floor_to_assign].add_wait(inhabitant)

    def _assign_inhabitants_to_floors(self):
        for inhabitant in self._inhabitants:
            floor_to_assign = random.randint(0, len(self._floors) - 1)
            inhabitant.desired_floor = self._floors[_random_int_excluding(0, len(self._floors), floor_to_assign)]
            self._floors[floor_to_assign].add_wait(inhabitant)

    def get_inhabitants(self):
        return self._inhabitants

    def min_floor(self):
        return self._floors[0].level

    def max_floor(self):
        return self._floors[-1].level

    def move_up(self):
        self._elevator.move_up(self._floors)

    def move_down(self):
        self._elevator.move_down(self._floors)

    def load(self):
        self._elevator.load()
        self._elevator.unload()

    def has_passengers_or_waiters_to_go_up(self):
        for human in self._elevator.passengers:
            if human.desired_floor.level > self._elevator.floor.level:
                return True
        for floor in self._floors[self._elevator.floor.level:]:
            if floor.waiting_humans:
                return True
        return False

    def has_passengers_to_go_up(self):
        for human in self._elevator.passengers:
            if human.desired_floor.level > self._elevator.floor.level:
                return True
        return False

    def has_passengers_to_go_down(self):
        for human in self._elevator.passengers:
            if human.desired_floor.level < self._elevator.floor.level:
                return True
        return False

    def has_waiters_to_go_up(self):
        for floor in self._floors[self._elevator.floor.level:]:
            if floor.waiting_humans:
                return True
        return False

    def has_waiters_to_go_down(self):
        for floor in self._floors[:self._elevator.floor.level]:
            if floor.waiting_humans:
                return True
        return False

    def get_elevator(self):
        return str(self._elevator)

    def get_elevator_run_info(self):
        return (f"Up-Moves: {self._elevator.run_count[1]} | Down-Moves: {self._elevator.run_count[0]} | Loading and Unloading: {self._elevator.load_count}\n"
                f"{Fore.BLACK}{Back.GREEN if self.no_false_transportations() else Back.RED}No Transportation Errors{Fore.RESET}{Back.RESET}")

    def get_all_floors(self):
        return "\n".join(str(obj) for obj in self._floors)

    def actual_floor(self):
        return self._elevator.floor.level

    def someone_has_destination(self):
        for human in self._elevator.passengers:
            if self._elevator.floor == human.desired_floor:
                return True
        return False

    def someone_is_waiting(self):
        if self._elevator.floor.waiting_humans:
            return True
        return False

    def can_go_idle(self):
        can_wait = True
        for floor in self._floors:
            if floor.waiting_humans:
                can_wait = False
        if self._elevator.passengers:
            can_wait = False
        return can_wait

    def simulate_new_cycle(self, amount):
        self._inhabitants = Human.get_humans(amount)
        self._assign_inhabitants_to_floors()

    def no_false_transportations(self):
        for floor in self._floors:
            for human in floor.transported_humans:
                if human.desired_floor.level != floor.level:
                    return False
        return True

