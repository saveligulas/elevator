import textwrap

from colorama import Fore
from colorama import Back
from colorama import Style


class Floor:
    def __init__(self, level):
        self.level = level
        self.waiting_humans = []
        self.transported_humans = []

    def __eq__(self, other):
        if isinstance(other, Floor):
            return other.level == self.level
        return False

    def __lt__(self, other):
        if isinstance(other, Floor):
            return self.level < other.level
        raise NotImplemented

    def __str__(self):
        return (f"Floor Level: {self.level} "
                f"\n     {Back.LIGHTRED_EX}{Fore.BLACK}Waiting:{Back.RESET}{Fore.RESET} {{{', '.join(str(obj) for obj in self.waiting_humans)}}} "
                f"\n     {Back.LIGHTGREEN_EX}{Fore.BLACK}Arrived:{Back.RESET}{Fore.RESET} {{{', '.join(str(obj) for obj in self.transported_humans)}}}")

    def add_wait(self, human):
        self.waiting_humans.append(human)

    def remove_wait(self):
        self.waiting_humans.clear()

    def add_transport(self, human):
        self.transported_humans.append(human)
