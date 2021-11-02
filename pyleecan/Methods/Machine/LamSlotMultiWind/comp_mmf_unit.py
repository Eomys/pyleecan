from ....Functions.Load.import_class import import_class


def comp_mmf_unit(self, Na, Nt, felec=1, current_dir=None, phase_dir=None):
    """Compute the winding Unit magnetomotive force

    Parameters
    ----------
    self : LamSlotMultiWind
        an LamSlotMultiWind object
    Na : int
        Space discretization for offline computation (otherwise use out.elec.angle)
    Nt : int
        Time discretization for offline computation (otherwise use out.elec.time)
    felec : float
        Stator current frequency to consider
    current_dir: int
        Stator current rotation direction +/-1
    phase_dir: int
        Stator winding phasor rotation direction +/-1

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
        self, Na=Na, Nt=Nt, felec=felec, current_dir=current_dir, phase_dir=phase_dir
    )

    return MMF_U, WF
