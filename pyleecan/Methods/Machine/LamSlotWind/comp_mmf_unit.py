# -*- coding: utf-8 -*-
from numpy import pi, linspace, zeros, ones, dot, squeeze
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.check_parent import check_parent


def comp_mmf_unit(self, Na=None, Nt=None, freq=1):
    """Compute the winding Unit magnetomotive force

    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization for offline computation (otherwise use out.elec.angle)
    Nt : int
        Time discretization for offline computation (otherwise use out.elec.time)
    freq : float
        Stator current frequency to consider

    Returns
    -------
    mmf_unit : SciDataTool.Classes.DataND.DataND
        Unit magnetomotive force (Na)
    """

    # Check if the lamination is within an output object
    is_out = check_parent(self, 3)

    # Get stator winding number of phases
    qs = self.winding.qs

    # Get spatial symmetry
    per_a, _, _, _ = self.comp_periodicity()

    # Check if the result is already available and that requested size is the same as stored data
    if (
        is_out
        and self.parent.parent.parent.elec.mmf_unit is not None
        and Nt is not None
        and Na is not None
    ):
        if self.parent.parent.parent.elec.mmf_unit.values.shape == (Nt, Na):
            return self.parent.parent.parent.elec.mmf_unit

    # Define the space dicretization
    if Na is None and is_out and self.parent.parent.parent.elec.angle is not None:
        # Use Electrical module discretization
        angle = self.parent.parent.parent.elec.angle
        Na = angle.size
    else:
        angle = linspace(0, 2 * pi / per_a, Na, endpoint=False)

    # Define the time dicretization
    if Nt is None and is_out and self.parent.parent.parent.elec.time is not None:
        # Use Electrical module discretization
        time = self.parent.parent.parent.elec.time
        freq = self.parent.parent.parent.elec.felec
        Nt = time.size
    else:
        time = linspace(0, 1 / freq, Nt, endpoint=False)

    # Compute the winding function and mmf
    wf = self.comp_wind_function(angle=angle, per_a=per_a)

    # Compute unit current function of time applying constant Id=1 Arms, Iq=0
    Idq = zeros((Nt, 2))
    Idq[:, 0] = ones(Nt)
    I = dq2n(Idq, 2 * pi * freq * time, n=qs, is_n_rms=False)

    # Compute unit mmf
    mmf_u = squeeze(dot(I, wf))

    # Create a Data object
    Time = Data1D(name="time", unit="s", values=time)
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={"angle": {"period": per_a}},
        initial=0,
        final=2 * pi / per_a,
        number=Na,
        include_endpoint=False,
    )
    MMF = DataTime(
        name="Unit MMF",
        unit="p.u.",
        symbol="Magnitude",
        axes=[Time, Angle],
        values=mmf_u,
        symmetries={"angle": {"period": per_a}},
    )

    if is_out:  # Store the result if the Output is available
        self.parent.parent.parent.elec.mmf_unit = MMF

    return MMF
