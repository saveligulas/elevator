from build import Building
from codeCreationBench import elevator_logic, elevator_logic_2
from human import Human
from runTypes import RunType


class RunTime:
    def __init__(self, building: Building):
        self._building_stories = building.max_floor()
        self._building_humans = len(building.get_inhabitants())
        self._building = building

    def reset(self):
        self._building = Building(Human.get_humans(self._building_humans), self._building_stories)

    def run_and_print(self, run_type: RunType, cycle_size=1, wave_cycle=1, wave_size=1, abort_counter=1000):
        print(f"Initial Building State: \n"
              f"{self._building.get_all_floors()} \n"
              f"{self._building.get_elevator()} \n"
              f"{self._building.get_elevator_run_info()} \n\n\n")

        if run_type == RunType.USE_CUSTOM_LOOP:
            elevator_logic(self._building)

        if run_type == RunType.UNTIL_COMPLETE:
            while not self._building.can_go_idle():
                elevator_logic(self._building)

        if run_type == RunType.RUN_CYCLES:
            for i in range(cycle_size):
                elevator_logic(self._building)

        if run_type == RunType.RUN_CYCLES_WITH_NEW_HUMANS:
            for i in range(1, cycle_size + 1):
                if i % wave_cycle == 0:
                    self._building.simulate_new_cycle(wave_size)
                elevator_logic(self._building)

        if run_type == RunType.RUN_UNTIL_COMPLETE_WITH_NEW_HUMANS:
            counter = 0
            while not self._building.can_go_idle():
                counter += 1
                if counter % wave_cycle == 0:
                    self._building.simulate_new_cycle(wave_size)
                if counter == abort_counter:
                    break
                elevator_logic(self._building)

        print(f"Final Building State: \n"
              f"{self._building.get_all_floors()} \n"
              f"{self._building.get_elevator()} \n"
              f"{self._building.get_elevator_run_info()}")

    def run_and_print_2(self, run_type: RunType, cycle_size=1, wave_cycle=1, wave_size=1, abort_counter=1000):
        print(f"Initial Building State: \n"
              f"{self._building.get_all_floors()} \n"
              f"{self._building.get_elevator()} \n"
              f"{self._building.get_elevator_run_info()} \n\n\n")

        if run_type == RunType.USE_CUSTOM_LOOP:
            elevator_logic_2(self._building)

        if run_type == RunType.UNTIL_COMPLETE:
            while not self._building.can_go_idle():
                elevator_logic_2(self._building)

        if run_type == RunType.RUN_CYCLES:
            for i in range(cycle_size):
                elevator_logic_2(self._building)

        if run_type == RunType.RUN_CYCLES_WITH_NEW_HUMANS:
            for i in range(1, cycle_size + 1):
                if i % wave_cycle == 0:
                    self._building.simulate_new_cycle(wave_size)
                elevator_logic_2(self._building)

        if run_type == RunType.RUN_UNTIL_COMPLETE_WITH_NEW_HUMANS:
            counter = 0
            while not self._building.can_go_idle():
                counter += 1
                if counter % wave_cycle == 0:
                    self._building.simulate_new_cycle(wave_size)
                if counter == abort_counter:
                    break
                elevator_logic_2(self._building)

        print(f"Final Building State: \n"
              f"{self._building.get_all_floors()} \n"
              f"{self._building.get_elevator()} \n"
              f"{self._building.get_elevator_run_info()}")
