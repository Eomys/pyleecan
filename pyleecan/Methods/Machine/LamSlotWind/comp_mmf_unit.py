from numpy import zeros, ones, dot, squeeze

from SciDataTool import DataTime

from ....Classes.OPdq import OPdq

from ....Functions.Electrical.dqh_transformation import dqh2n
from ....Functions.Load.import_class import import_class

from ....Methods.Simulation.Input import CURRENT_DIR_REF, PHASE_DIR_REF, ROT_DIR_REF


def comp_mmf_unit(self, Na=None, Nt=None, felec=1, current_dir=None, phase_dir=None):
    """Compute the winding unit magnetomotive force for given inputs

    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization for offline computation
    Nt : int
        Time discretization for offline computation
    felec : float
        Stator current frequency to consider
    current_dir: int
        Stator current rotation direction +/-1
    phase_dir: int
        Stator winding phasor rotation direction +/-1

    Returns
    -------
    MMF_U : DataTime
        Unit magnetomotive force (Na,Nt)
    WF : DataTime
        Winding functions (qs,Na)

    """

    # Check that parent machine is not None
    if self.parent is None:
        raise Exception("Cannot calculate mmf unit if parent machine is None")
    else:
        machine = self.parent

    # Compute the winding function and mmf
    if self.winding is None:
        raise Exception("Cannot calculate mmf unit if winding is None")
    else:
        # Get stator winding number of phases
        qs = self.winding.qs

    if current_dir is None:
        current_dir = CURRENT_DIR_REF
    elif current_dir not in [-1, 1]:
        raise Exception("Cannot enforce current_dir other than +1 or -1")

    if phase_dir is None:
        phase_dir = PHASE_DIR_REF
    elif phase_dir not in [-1, 1]:
        raise Exception("Cannot enforce phase_dir other than +1 or -1")

    InputVoltage = import_class("pyleecan.Classes", "InputVoltage")
    input = InputVoltage(
        Na_tot=Na,
        Nt_tot=Nt,
        OP=OPdq(felec=felec),
        current_dir=current_dir,
        rot_dir=ROT_DIR_REF,  # rotor rotating dir has not impact on unit mmf
    )

    axes_dict = input.comp_axes(
        axes_list=["time", "angle", "phase_S", "phase_R"],
        machine=machine,
        is_periodicity_t=bool(Nt > 1),
        is_periodicity_a=bool(Na > 1),
        is_antiper_t=False,
        is_antiper_a=False,
    )

    # Compute winding function
    angle = axes_dict["angle"].get_values(is_oneperiod=True)
    per_a, _ = axes_dict["angle"].get_periodicity()
    wf = self.comp_wind_function(angle=angle, per_a=per_a)

    # Compute unit current function of time applying constant Id=1 Arms, Iq=Ih=0
    angle_elec = axes_dict["time"].get_values(
        is_oneperiod=True, normalization="angle_elec"
    )
    Idq = zeros((angle_elec.size, 3))
    Idq[:, 0] = ones(angle_elec.size)
    I = dqh2n(Idq, angle_elec, n=qs, is_n_rms=False, phase_dir=phase_dir)

    # Compute unit mmf
    mmf_u = squeeze(dot(I, wf))

    # Create a Data object

    MMF_U = DataTime(
        name="Overall MMF",
        unit="A",
        symbol="MMF",
        axes=[axes_dict["time"], axes_dict["angle"]],
        values=mmf_u,
    )

    WF = DataTime(
        name="Phase MMF",
        unit="A",
        symbol="MMF",
        axes=[axes_dict["angle"], axes_dict["phase_" + self.get_label()]],
        values=wf.T,
    )

    return MMF_U, WF
