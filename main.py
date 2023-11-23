from build import Building
from human import Human
from runTypes import RunType
from testing import RunTime

building = Building(Human.get_humans(50), 20)

run_time = RunTime(building)
run_time_2 = RunTime(building)

run_time.run_and_print(RunType.USE_CUSTOM_LOOP)
# print("\n \n \n Run Time: 2 \n")
# run_time.run_and_print_2(RunType.UNTIL_COMPLETE)

# Examples:
# run_time.run_and_print(RunType.RUN_UNTIL_COMPLETE_WITH_NEW_HUMANS, wave_cycle=10, wave_size=1, abort_counter=100)
# run_time.run_and_print(RunType.RUN_CYCLES_WITH_NEW_HUMANS, cycle_size=100, wave_cycle=10, wave_size=1)
# run_time.run_and_print(RunType.RUN_CYCLES, cycle_size=5)

