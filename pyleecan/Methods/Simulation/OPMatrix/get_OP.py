from ....Classes.OPdq import OPdq
from ....Classes.OPdqf import OPdqf
from ....Classes.OPslip import OPslip


def get_OP(self, index):
    """Return the OP at the corresponding index

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object to extrat the OP from
    index : int
        Index of the OP to extract

    Returns
    -------
    OP : OP
        OP object
    """

    if self.has_slip():
        OP = OPslip()
    elif self.If_ref is not None:
        OP = OPdqf()
    else:
        OP = OPdq()

    if self.N0 is not None:
        OP.N0 = self.N0[index]
    if self.Id_ref is not None and self.Iq_ref is not None:
        OP.set_Id_Iq(Id=self.Id_ref[index], Iq=self.Iq_ref[index])
    if self.Ud_ref is not None and self.Uq_ref is not None:
        OP.set_Ud_Uq(Ud=self.Ud_ref[index], Uq=self.Uq_ref[index])
    if self.Tem_av_ref is not None:
        OP.Tem_av_ref = self.Tem_av_ref[index]
    if self.Pem_av_ref is not None:
        if self.is_output_power in [None, True]:
            OP.Pem_av_ref = self.Pem_av_ref[index]
        else:
            OP.Pem_av_in = self.Pem_av_ref[index]
    if self.slip_ref is not None:
        OP.slip_ref = self.slip_ref[index]
    if self.If_ref is not None:
        OP.If_ref = self.If_ref[index]

    return OP
