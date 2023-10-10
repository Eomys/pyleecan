import pytest
from os.path import join
from numpy import pi
from pyleecan.Classes.OPdq import OPdq
import matplotlib.pyplot as plt

from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

M400_50A = load(join(DATA_DIR, "Material", "M400-50A.json"))
Copper1 = load(join(DATA_DIR, "Material", "Copper1.json"))

machine = MachineDFIM(shaft=None, frame=None)
machine.stator = LamSlotWind(
    L1=0.85, Rint=0.2, Rext=0.3, is_stator=True, is_internal=False, mat_type=M400_50A
)
machine.rotor = LamSlotWind(
    L1=0.85, Rint=0.1, Rext=0.195, is_stator=False, is_internal=True, mat_type=M400_50A
)
winding = Winding(qs=3, Nlayer=2, p=2, conductor=CondType11(cond_mat=Copper1))
machine.stator.slot = SlotW22(
    Zs=12,
    W0=pi / 24,
    W2=pi / 12,
    H0=10e-3,
    H2=50e-3,
)
machine.rotor.slot = SlotW22(
    Zs=12,
    W0=pi / 24,
    W2=pi / 12,
    H0=10e-3,
    H2=50e-3,
)
machine.stator.winding = winding
machine.rotor.winding = winding

machine_list = [machine]

# SlotW11 In/Out
machine11 = machine.copy()
machine11.stator.slot = SlotW11(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, R1=4e-3, H2=50e-3
)
machine11.rotor.slot = SlotW11(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, R1=4e-3, H2=50e-3
)
machine_list.append(machine11)

# SlotW14 In/Out
machine14 = machine.copy()
machine14.stator.slot = SlotW14(Zs=12, W0=10e-3, H0=20e-3, H1=0, W3=20e-3, H3=50e-3)
machine14.rotor.slot = SlotW14(Zs=12, W0=10e-3, H0=20e-3, H1=0, W3=20e-3, H3=50e-3)
machine_list.append(machine14)

# SlotW21 In/Out
machine21 = machine.copy()
machine21.stator.slot = SlotW21(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, H2=50e-3
)
machine21.rotor.slot = SlotW21(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, H2=50e-3
)
machine_list.append(machine21)

# SlotW22 In/Out H0=0 + W0 == W2
machine22 = machine.copy()
machine22.stator.slot.H0 = 0
machine22.rotor.slot.H0 = 0
machine22.rotor.slot.W0 = machine22.rotor.slot.W2
machine_list.append(machine22)

# SlotW23 In/Out
machine23 = machine.copy()
machine23.stator.slot = SlotW23(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, H2=50e-3
)
machine23.rotor.slot = SlotW23(
    Zs=12, W0=10e-3, H0=20e-3, H1=0, W1=40e-3, W2=40e-3, H2=50e-3
)
machine_list.append(machine23)

# SlotW25 In/Out
machine25 = machine.copy()
machine25.stator.slot = SlotW25(Zs=12, W4=80e-3, H1=20e-3, W3=20e-3, H2=50e-3)
machine25.rotor.slot = SlotW25(Zs=12, W4=80e-3, H1=20e-3, W3=20e-3, H2=50e-3)
machine_list.append(machine25)

# SlotW29 In/Out
machine29 = machine.copy()
machine29.stator.slot = SlotW29(
    Zs=12, W0=5e-3, W1=5e-3, W2=30e-3, H0=10e-3, H1=10e-3, H2=50e-3
)
machine29.rotor.slot = SlotW29(
    Zs=12, W0=5e-3, W1=5e-3, W2=30e-3, H0=10e-3, H1=10e-3, H2=50e-3
)
machine_list.append(machine29)

# SlotW29 In/Out with strange parameters (H1=0 and W1=W2)
machine292 = machine.copy()
machine292.stator.slot = SlotW29(
    Zs=12, W0=5e-3, W1=30e-3, W2=30e-3, H0=10e-3, H1=0, H2=50e-3
)
machine292.rotor.slot = SlotW29(
    Zs=12, W0=5e-3, W1=30e-3, W2=30e-3, H0=10e-3, H1=0, H2=50e-3
)
machine_list.append(machine292)


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SingleOP
@pytest.mark.parametrize("test_machine", machine_list)
def test_FEMM_fast_draw(test_machine, is_plot=False):
    """Test to check that the fast draw method works on machine with overlapping winding/slot lines
    When a slot have a double layer tangential winding and that a line perfectly overlap the
    opening/active zone the copy/rotate method of fast draw fails (the closing line is missing):

    ###############
    #      #      #
    #      #      #
    #      #      #
    #      #      #
    #      #      #
    ####       ####  <=
       #       #

    The reason is that FEMM selects the surface to copy rotate by selecting all the lines of the surface
    by selecting the closest line to the center of the line. As the slot and winding line overlap
    there are in fact two lines to select and if the slot line is longer that the winding line, then
    only the slot line is copy/rotate and the winding surface is not closed !
    Ex: SlotW22 with W0 < W2*0.75

    The issue was solved by making sur that build_geometry returns the correct number of lines
    """

    test_machine.name = str(type(test_machine.rotor.slot).__name__)
    if is_plot:

        test_machine.plot()
        test_machine.plot(is_max_sym=True)
        plt.show()
    simu = Simu1(name="test_fast_draw", machine=test_machine)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2 ** 6,
        Nt_tot=1,
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=False,
        is_fast_draw=True,
        Kmesh_fineness=0.5,
    )
    simu.elec = None
    simu.force = None

    out = simu.run()


# To run it without pytest
if __name__ == "__main__":
    test_FEMM_fast_draw(machine22, is_plot=True)
    for test_machine in machine_list:
        test_FEMM_fast_draw(test_machine, is_plot=True)
    print("Done")
