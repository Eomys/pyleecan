from ....Classes.InputPower import InputPower
from ....Classes.Simulation import Simulation
from ....Classes.OPdq import OPdq


def get_input_list(self):
    """Return a list of InputCurrent to set the Operating point"""

    # Check that the object has the correct type
    assert isinstance(self.parent, Simulation)
    ref_simu = self.parent
    assert isinstance(ref_simu.input, InputPower)

    OP_matrix = self.OP_matrix
    N_simu = OP_matrix.shape[0]

    # Generate initial input_list
    ref_input = ref_simu.input.copy()
    input_list = [ref_input.copy() for ii in range(N_simu)]

    # Set default time vector (enforce definition Nt_tot, Nrev)
    if ref_input.Nt_tot is None:
        Nt_tot = len(ref_input.time.get_data())
    else:
        Nt_tot = ref_input.Nt_tot

    # Update OP according to OP_matrix
    for ii in range(N_simu):
        input_list[ii].OP = OPdq()
        input_list[ii].OP.N0 = OP_matrix[ii, 0]
        # Edit time vector
        input_list[ii].time = None
        input_list[ii].Nt_tot = Nt_tot
        input_list[ii].Nrev = ref_input.Nrev

        if self.OP_matrix.shape[1] > 3:
            input_list[ii].OP.Tem_av_ref = OP_matrix[ii, 3]
        if self.OP_matrix.shape[1] > 4:
            input_list[ii].OP.Pem_av_ref = self.OP_matrix[ii, 4]

    return input_list
