from ....Classes.Simulation import Simulation
from ....Classes.InputCurrent import InputCurrent


def get_input_list(self):
    """Return a list of InputCurrent to set the Operating point"""

    # Check that the object has the correct type
    assert isinstance(self.parent, Simulation)
    ref_simu = self.parent
    assert isinstance(ref_simu.input, InputCurrent)
    N_simu = self.OP_matrix.shape[0]

    # Generate initial input_list
    ref_input = ref_simu.input.copy()
    input_list = [ref_input.copy() for ii in range(N_simu)]

    # Set default time vector (enforce definition Nt_tot, Nrev)
    if ref_input.Nt_tot is None:
        Nt_tot = len(ref_input.time.get_data())
    else:
        Nt_tot = ref_input.Nt_tot
    if ref_input.Nrev is None:
        Nrev = 1
    else:
        Nrev = ref_input.Nrev
    # Update OP according to OP_matrix
    for ii in range(N_simu):
        input_list[ii].N0 = self.OP_matrix[ii, 0]
        # Edit time vector
        input_list[ii].time = None
        input_list[ii].Nt_tot = Nt_tot
        input_list[ii].Nrev = Nrev
        if self.type_OP_matrix == 0:  # I0, Phi0
            input_list[ii].set_Id_Iq(
                I0=self.OP_matrix[ii, 1], Phi0=self.OP_matrix[ii, 2]
            )
        else:  # Id/Iq
            input_list[ii].Id_ref = self.OP_matrix[ii, 1]
            input_list[ii].Iq_ref = self.OP_matrix[ii, 2]
        if self.is_torque:
            input_list[ii].Tem_av_ref = self.OP_matrix[ii, 3]
        if self.is_power and self.OP_matrix.shape[1] > 4:
            input_list[ii].P_ref = self.OP_matrix[ii, 4]

    return input_list
