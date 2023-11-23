from build import Building


# Do not delete or rename this function
# RunTime will automatically loop this function in regard to the set RunType until Elevator goes Idle
def elevator_logic_2(b: Building):
    for i in range(b.actual_floor(), b.max_floor()):
        b.move_up()
        b.load()

    for i in range(b.max_floor()):
        b.move_down()
        b.load()


def elevator_logic(b: Building):
    while not b.can_go_idle():

        if b.someone_has_destination() or b.someone_is_waiting():
            b.load()

        if b.has_passengers_or_waiters_to_go_up():
            b.move_up()
        else:
            b.move_down()


def elevator_logic_sample(b: Building):
    while b.has_waiters_to_go_up() or b.has_passengers_to_go_up():
        b.move_up()
        if b.someone_has_destination() or b.someone_is_waiting():
            b.load()
    while b.has_waiters_to_go_down() or b.has_waiters_to_go_down():
        b.move_down()
        if b.someone_has_destination() or b.someone_is_waiting():
            b.load()


