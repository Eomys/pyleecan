from numpy import isnan

from ....Classes.OPdq import OPdq


def set_OP_from_array(self, OP_matrix, type_OP_matrix=1, index=0):
    """Extract the Operating Point from an OP_matrix

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    OP_matrix : ndarray
        Operating Point matrix (cf VarLoadCurrent)
    type_OP_matrix : int
        Select which kind of OP_matrix is used 0: (N0,I0,Phi0,T,P), 1:(N0,Id,Iq,T,P)
    index : int
        To select the line of the OP_matrix to use (default=0)
    """

    # Check OP_matrix
    assert len(OP_matrix.shape) == 2
    assert OP_matrix.shape[1] <= 5
    assert index < OP_matrix.shape[0]
    assert type_OP_matrix in [0, 1]

    if type_OP_matrix == 1:
        if self.OP is None:
            self.OP = OPdq()
        self.OP.Id_ref = OP_matrix[index, 1]
        self.OP.Iq_ref = OP_matrix[index, 2]
    else:
        if self.OP is None:
            self.OP = OPdq()
        self.set_Id_Iq(I0=OP_matrix[index, 1], Phi0=OP_matrix[index, 2])
    self.OP.N0 = OP_matrix[index, 0]
    if OP_matrix.shape[1] > 3:
        if isnan(OP_matrix[index, 3]):
            self.OP.Tem_av_ref = None
        else:
            self.OP.Tem_av_ref = OP_matrix[index, 3]
    if OP_matrix.shape[1] > 4:
        if isnan(OP_matrix[index, 4]):
            self.OP.Pem_av_ref = None
        else:
            self.OP.Pem_av_ref = OP_matrix[index, 4]
