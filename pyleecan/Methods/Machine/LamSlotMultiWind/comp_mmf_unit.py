# -*- coding: utf-8 -*-
from numpy import pi, linspace, zeros, ones, dot, squeeze
from SciDataTool import Data1D, DataTime, Norm_ref
from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name
from pyleecan.Classes.Winding import Winding


def comp_mmf_unit(self, Na=None, Nt=None, freq=1):
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

    Returns
    -------
    MMF_U : SciDataTool.Classes.DataND.DataND
        Unit magnetomotive force (Na,Nt)
    WF : SciDataTool.Classes.DataND.DataND
        Winding functions (qs,Na)

    """

    # Get stator winding number of phases
    qs = self.winding.qs

    # Get number of pole pairs
    p = self.get_pole_pair_number()

    # Get spatial symmetry
    per_a, _ = self.comp_periodicity_spatial()

    # Define the space dicretization
    angle = linspace(0, 2 * pi / per_a, Na, endpoint=False)

    # Define the time dicretization
    time = linspace(0, 1 / freq, Nt, endpoint=False)

    # Compute the winding function and mmf
    if self.winding is None or self.winding.conductor is None:
        wf = zeros((qs, Na))
    else:
        wf = self.comp_wind_function(angle=angle, per_a=per_a)

    # Compute unit current function of time applying constant Id=1 Arms, Iq=0
    Idq = zeros((Nt, 2))
    Idq[:, 0] = ones(Nt)
    I = dq2n(Idq, 2 * pi * freq * time, n=qs, is_n_rms=False)

    # Compute unit mmf
    mmf_u = squeeze(dot(I, wf))

    # Create a Data object
    Time = Data1D(name="time", unit="s", values=time)
    Angle = Data1D(
        name="angle",
        unit="rad",
        symmetries={"period": per_a},
        values=angle,
        normalizations={"space_order": Norm_ref(ref=self.get_pole_pair_number())},
    )
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs),
        is_components=True,
    )
    MMF_U = DataTime(
        name="Total MMF",
        unit="A",
        symbol="Magnitude",
        axes=[Time, Angle],
        values=mmf_u,
    )

    WF = DataTime(
        name="Phase MMF",
        unit="A",
        symbol="Magnitude",
        axes=[Phase, Angle],
        values=wf,
    )

    return MMF_U, WF
