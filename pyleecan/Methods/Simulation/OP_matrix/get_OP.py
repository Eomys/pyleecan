from ....Classes.OPdq import OPdq
from ....Classes.OPslip import OPslip


def get_OP(self, index, type_OP=0):
    """Return the OP at the corresponding index

    Parameters
    ----------
    self : OP_matrix
        OP_matrix object to extrat the OP from
    index : int
        Index of the OP to extract
    type_OP : int
        0 OPdq, 1 OPslip

    Returns
    -------
    OP : OP
        OP object
    """

    if type_OP == 0:
        OP = OPdq()
    else:
        OP = OPslip()

    if self.N0 is not None:
        OP.N0 = self.N0[index]
    if self.Id_ref is not None and self.Iq_ref is not None:
        OP.set_Id_Iq(Id=self.Id_ref[index], Iq=self.Iq_ref[index])
    if self.Ud_ref is not None and self.Uq_ref is not None:
        OP.set_Ud_Uq(Ud=self.Ud_ref[index], Uq=self.Uq_ref[index])
    if self.Tem_av_ref is not None:
        OP.Tem_av_ref = self.Tem_av_ref[index]
    if self.Pem_av_ref is not None:
        OP.Pem_av_ref = self.Pem_av_ref[index]
    if self.slip_ref is not None:
        OP.Pem_av_ref = self.slip_ref[index]

    return OP
