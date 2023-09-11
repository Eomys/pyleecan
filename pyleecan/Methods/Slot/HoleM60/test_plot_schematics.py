import pytest

 

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods import ParentMissingError
from pyleecan.Classes.LamHole import LamHole
from plot_schematics import plot_schematics
from pyleecan.Classes.Magnet import Magnet

 

from numpy import pi
from time import sleep
from matplotlib import pyplot as plt

 
mag = {0: Magnet(), 1: Magnet()}
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.8,
        W1=10e-3,
        W2=10e-2,
        W3=5e-3,
        H0=3e-3,
        H1=5e-3,
    )
)
test_obj.hole[0].set_magnet_by_id(0, Magnet())
test_obj.hole[0].set_magnet_by_id(1, Magnet())
test_obj.hole[0].magnet_dict = dict()
test_obj.hole[0].magnet_dict["magnet_" + str(0)] = Magnet(type_magnetization=1)
 

if __name__ == "__main__":
    plot_schematics(test_obj.hole[0])
    plt.show()
    sleep(60)