from ....Functions.Load.import_class import import_class


def comp_mmf_unit(self, Na, Nt, felec=1, rot_dir=-1, N0=1000):
    """Compute the winding Unit magnetomotive force

    Parameters
    ----------
    self : LamSlotMultiWind
        an LamSlotMultiWind object
    Na : int
        Space discretization for offline computation (otherwise use out.elec.angle)
    Nt : int
        Time discretization for offline computation (otherwise use out.elec.time)
    freq : float
        Stator current frequency to consider
    rot_dir : int
        Rotation direction (+/- 1)

    Returns
    -------
    MMF_U : SciDataTool.Classes.DataND.DataND
        Unit magnetomotive force (Na,Nt)
    WF : SciDataTool.Classes.DataND.DataND
        Winding functions (qs,Na)

    """

    # Call method of LamSlotWind
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")

    MMF_U, WF = LamSlotWind.comp_mmf_unit(
        self, Na=Na, Nt=Nt, felec=felec, rot_dir=rot_dir, N0=N0
    )

    return MMF_U, WF
