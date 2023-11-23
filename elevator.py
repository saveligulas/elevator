from colorama import Back, Fore

from direc import Direction


class Elevator:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
        self.floor = None
        self.orders = []
        self.direction = Direction.UP
        self.load_count = 0
        self.run_count = [0, 0]

    def __getitem__(self, human):
        return self.passengers[human]

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return (f"{Back.LIGHTCYAN_EX}{Fore.BLACK} Elevator Floor Level:{Back.RESET}{Fore.RESET} {self.floor.level} \n"
                f"           {Back.LIGHTMAGENTA_EX}{Fore.BLACK}Passengers:{Back.RESET}{Fore.RESET} {', '.join(str(obj) for obj in self.passengers)}")

    def append_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def switch_direction(self):
        self.direction = (
            Direction.DOWN
            if self.direction == Direction.UP
            else Direction.UP
        )

    def move_up(self, floors):
        if self.floor.level != len(floors) - 1:
            self.floor = floors[self.floor.level + 1]
            self.run_count[1] = self.run_count[1] + 1

    def move_down(self, floors):
        if self.floor.level != 0:
            self.floor = floors[self.floor.level - 1]
            self.run_count[0] = self.run_count[0] + 1

    def load(self):
        for human in self.floor.waiting_humans:
            self.passengers.append(human)
        self.floor.remove_wait()
        self.load_count += 1

    def unload(self):
        humans_to_unload = []
        for i in range(len(self.passengers)):
            human = self.passengers[i]
            if human.desired_floor.level == self.floor.level:
                self.floor.add_transport(human)
                humans_to_unload.append(i)

        self.passengers = [self.passengers[i] for i in range(len(self.passengers)) if i not in humans_to_unload]

