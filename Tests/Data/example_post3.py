from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53


def example_post3(xoutput):
    """var_simu post_proc"""

    if xoutput.simu.machine.stator.slot.W0 == 3:
        xoutput.simu.machine.rotor.hole = [HoleM51()]
    elif xoutput.simu.machine.stator.slot.W0 == 4:
        xoutput.simu.machine.rotor.hole = [HoleM52()]
    elif xoutput.simu.machine.stator.slot.W0 == 5:
        xoutput.simu.machine.rotor.hole = [HoleM53()]
