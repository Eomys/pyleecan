from numpy import isnan

from ....Classes.OPdq import OPdq
from ....Classes.OPslip import OPslip


def set_OP_from_array(self, OP_matrix, type_OP_matrix, index=0, is_output_power=True):
    """Extract the Operating Point from an OP_matrix
    Parameters
    ----------
    self : InputVoltage
        An InputVoltage object
    OP_matrix : ndarray
        Operating Point matrix (cf VarLoadCurrent)
    type_OP_matrix : int
        Select which kind of OP_matrix is used 0: (N0,U0,Phi0,T,P), 1:(N0,Ud,Uq,T,P)
    index : int
        To select the line of the OP_matrix to use (default=0)
    is_output_power: bool
        True if power given in OP_matrix is the output power, False if it is the input power
    """

    # Check OP_matrix
    assert len(OP_matrix.shape) == 2
    assert OP_matrix.shape[1] <= 5
    assert index < OP_matrix.shape[0]
    assert type_OP_matrix in [0, 1, 2]

    if self.OP is None:
        if type_OP_matrix in [0, 1]:
            self.OP = OPdq()
        elif type_OP_matrix == 2:
            self.OP = OPslip()

    if type_OP_matrix == 0:
        self.set_U0_UPhi0(U0=OP_matrix[index, 1], UPhi0=OP_matrix[index, 2])

    elif type_OP_matrix == 1:
        self.set_Ud_Uq(Ud=OP_matrix[index, 1], Uq=OP_matrix[index, 2])

    elif type_OP_matrix == 2:
        self.OP.set_U0_UPhi0(U0=OP_matrix[index, 1], UPhi0=0)
        self.OP.slip_ref = OP_matrix[index, 2]

    self.OP.N0 = OP_matrix[index, 0]

    if OP_matrix.shape[1] > 3:
        if isnan(OP_matrix[index, 3]):
            self.OP.Tem_av_ref = None
        else:
            self.OP.Tem_av_ref = OP_matrix[index, 3]
    if OP_matrix.shape[1] > 4:
        if isnan(OP_matrix[index, 4]):
            self.OP.Pem_av_ref = None
        elif is_output_power:
            self.OP.Pem_av_ref = OP_matrix[index, 4]
        else:
            self.OP.Pem_av_in = OP_matrix[index, 4]
