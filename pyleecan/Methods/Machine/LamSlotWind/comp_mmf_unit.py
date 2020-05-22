# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import pi, linspace, zeros, ones, sqrt, dot, array, squeeze
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.check_parent import check_parent


def comp_mmf_unit(self, Na=2048, Nt=50):
    """Compute the winding Unit magnetomotive force

    Parameters
    ----------
    self : LamSlotWind
        an LamSlotWind object
    Na : int
        Space discretization for offline computation (otherwise use out.elec.angle)
    Nt : int
        Time discretization for offline computation (otherwise use out.elec.time)
    Returns
    -------
    mmf_unit : SciDataTool.Classes.DataND.DataND
        Unit magnetomotive force (Na)
    """

    # Check if the lamination is within an output object
    is_out = check_parent(self, 3)

    # Check if the result is already available
    if is_out and self.parent.parent.parent.elec.mmf_unit is not None:
        return self.parent.parent.parent.elec.mmf_unit

    # Define the space dicretization
    if is_out and self.parent.parent.parent.elec.angle is not None:
        # Use Electrical module discretization
        angle = self.parent.parent.parent.elec.angle
        Na = angle.size
        time = self.parent.parent.parent.elec.time
        Nt = time.size
    else:
        angle = linspace(0, 2 * pi, Na, endpoint=False)
        time = linspace(0, 1 / 50, Nt, endpoint=False)  # freq = 50Hz

    # Compute the winding function and mmf
    wf = self.comp_wind_function(angle=angle)
    qs = self.winding.qs

    # Compute unit mmf
    Idq = zeros((Nt, 2))
    Idq[:, 0] = ones(Nt)
    I = dq2n(Idq, 0, n=qs)
    mmf_u = squeeze(dot(I, wf))

    # Create a Data object
    Time = Data1D(name="time", unit="s", values=time)
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=0,
        final=2 * pi,
        number=Na,
        include_endpoint=False,
    )
    MMF = DataTime(
        name="Unit MMF",
        unit="p.u.",
        symbol="Magnitude",
        axes=[Time, Angle],
        values=mmf_u,
    )

    if is_out:  # Store the result if the Output is available
        self.parent.parent.parent.elec.mmf_unit = MMF
    return MMF
