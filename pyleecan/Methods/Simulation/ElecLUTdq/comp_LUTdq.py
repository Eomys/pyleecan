from numpy import meshgrid, linspace, zeros

from ....Classes.LUTdq import LUTdq


def comp_LUTdq(self):
    """Compute Look up table function of Id / Iq

    Parameters
    ----------
    self : ElecLUTdq
        a ElecLUTdq object

    Returns
    ----------
    LUT : LUTdq
        Calculated look-up table
    """

    if self.LUT_simu is None:
        raise Exception("Cannot calculate LUTdq if self.LUT_simu is None")
    else:
        simu = self.LUT_simu.copy()

    N_OP = self.n_Id * self.n_Iq
    N0 = self.parent.input.OP.N0

    Id, Iq = meshgrid(
        linspace(self.Id_min, self.Id_max, self.n_Id),
        linspace(self.Iq_min, self.Iq_max, self.n_Iq),
    )
    OP_matrix = zeros((N_OP, 3))
    OP_matrix[:, 0] = N0
    OP_matrix[:, 1] = Id.ravel()
    OP_matrix[:, 2] = Iq.ravel()

    simu.machine = self.parent.machine
    simu.var_simu.OP_matrix = OP_matrix
    simu.input.set_OP_from_array(type_OP_matrix=1, OP_matrix=OP_matrix)

    LUT = LUTdq(simu=simu)

    LUT.simu.run()

    return LUT
