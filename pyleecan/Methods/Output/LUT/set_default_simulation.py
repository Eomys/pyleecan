from ....Functions.Load.import_class import import_class


def set_default_simulation(self, machine, OP_matrix, type_OP_matrix=1, name=None):
    """Set the default simulation to compute the LUT

    Parameters
    ----------
    self : LUT
        A LUT object
    machine : Machine
        The machine to use in the simulation
    OP_matrix : ndarray
        OP_matrix to use for VarLoadCurrent
    type_OP_matrix : int
        0: N0, I0, Phi0; 1: N0, Id, Iq
    name : str
        Name of the simulation
    """

    # Dynamic import to avoid loop
    Simu1 = import_class("pyleecan.Classes", "Simu1")
    InputCurrent = import_class("pyleecan.Classes", "InputCurrent")
    VarLoadCurrent = import_class("pyleecan.Classes", "VarLoadCurrent")
    OPdq = import_class("pyleecan.Classes", "OPdq")
    MagFEMM = import_class("pyleecan.Classes", "MagFEMM")
    PostLUT = import_class("pyleecan.Classes", "PostLUT")

    if name is None:
        name = "comp_LUT_" + machine.name
    simu = Simu1(name=name, machine=machine)

    # Definition of the input
    simu.input = InputCurrent(
        Nt_tot=8 * 12,
        Na_tot=8 * 200,
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),  # Will be overwritten
    )

    # Set varspeed simulation
    simu.var_simu = VarLoadCurrent(
        type_OP_matrix=type_OP_matrix,
        OP_matrix=OP_matrix,
        is_keep_all_output=True,
        stop_if_error=True,
    )
    simu.input.set_OP_from_array(OP_matrix, type_OP_matrix=type_OP_matrix)

    # Define second simu for FEMM comparison
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Postprocessing
    simu.var_simu.postproc_list = [PostLUT(is_save_LUT=True)]

    # Set simu in LUT
    self.simu = simu
