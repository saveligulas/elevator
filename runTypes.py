from enum import Enum


class RunType(Enum):
    """
    Enum representing the Run Type of your Building.

    Attributes:
        UNTIL_COMPLETE: Will run until idle without creating new humans
        RUN_CYCLES: Will run for a set amount of cycles without creating new humans
        RUN_CYCLES_WITH_NEW_HUMANS: Will run for a set amount cycles with new humans
        USE_CUSTOM_LOOP: Will not loop your code and run it once

        (Experimental! Do not use a big wave size)
        RUN_UNTIL_COMPLETE_WITH_NEW_HUMANS: Will run until idle with creating new humans

    """
    UNTIL_COMPLETE = 0
    RUN_CYCLES = 1
    RUN_CYCLES_WITH_NEW_HUMANS = 2
    RUN_UNTIL_COMPLETE_WITH_NEW_HUMANS = 3
    USE_CUSTOM_LOOP = 4
