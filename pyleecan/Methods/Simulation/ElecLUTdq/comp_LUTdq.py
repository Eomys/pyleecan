from numpy import meshgrid, linspace, zeros

from ....Classes.PostLUT import PostLUT

from ....Functions.load import import_class


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

    Simu1 = import_class("pyleecan.Classes", "Simu1")
    OPdq = import_class("pyleecan.Classes", "OPdq")
    VarLoadCurrent = import_class("pyleecan.Classes", "VarLoadCurrent")
    InputCurrent = import_class("pyleecan.Classes", "InputCurrent")

    if self.mag_model is None:
        raise Exception("Cannot calculate LUTdq if self.mag_model is None")
    else:
        mag_model = self.mag_model.copy()

    if self.loss_model is None:
        loss_model = None
    else:
        loss_model = self.loss_model.copy()

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

    simu = Simu1(
        machine=self.parent.machine,
        input=InputCurrent(OP=OPdq(N0=N0)),
        var_simu=VarLoadCurrent(
            type_OP_matrix=1,
            OP_matrix=OP_matrix,
            postproc_list=[PostLUT(is_store_LUT=True, is_save_LUT=False)],
            is_keep_all_output=True,
        ),
        mag=mag_model,
        loss=loss_model,
    )
    simu.input.set_OP_from_array(type_OP_matrix=1, OP_matrix=OP_matrix)

    out = simu.run()

    LUT = out.simu.var_simu.postproc_list[0].LUT

    LUT.Phi_dqh_mean = zeros((N_OP, 3))
    for ii, out_ii in enumerate(out.output_list):
        LUT.Phi_dqh_mean[ii, 0] = out_ii.elec.eec.Phid
        LUT.Phi_dqh_mean[ii, 1] = out_ii.elec.eec.Phiq

    return LUT
