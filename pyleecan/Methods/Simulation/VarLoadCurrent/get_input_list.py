from ....Classes.InputVoltage import InputVoltage
from ....Classes.Simulation import Simulation
from ....Classes.OPdq import OPdq


def get_input_list(self):
    """Return a list of InputCurrent to set the Operating point"""

    # Check that the object has the correct type
    assert isinstance(self.parent, Simulation)
    ref_simu = self.parent
    assert isinstance(ref_simu.input, InputVoltage)

    OP_list = self.OP_matrix.get_OP_list()
    N_simu = len(OP_list)

    # Generate initial input_list
    ref_input = ref_simu.input.copy()
    input_list = [ref_input.copy() for ii in range(N_simu)]

    # Set default time vector (enforce definition Nt_tot, Nrev)
    if ref_input.Nt_tot is None:
        Nt_tot = len(ref_input.time.get_data())
    else:
        Nt_tot = ref_input.Nt_tot
    Nrev = ref_input.Nrev
    # Update OP according to OP_matrix
    for ii in range(N_simu):
        input_list[ii].OP = OP_list[ii]
        # Edit time vector
        input_list[ii].time = None
        input_list[ii].Nt_tot = Nt_tot
        input_list[ii].Nrev = Nrev

    return input_list
