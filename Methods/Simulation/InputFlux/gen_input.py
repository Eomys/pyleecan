# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.OutMag import OutMag
from pyleecan.Methods.Simulation.Input import InputError
from SciDataTool import DataND, DataLinspace, DataTime
from numpy import ndarray


def gen_input(self):
    """Generate the input for the structural module (magnetic output)

    Parameters
    ----------
    self : InputFlux
        An InputFlux object
    """

    output = OutMag()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InputFlux.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InputFlux.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InputFlux.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InputFlux.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )
    Na_tot = len(output.angle)

    if self.Br is None:
        raise InputError("ERROR: InFlux.Br missing")
    Br = self.Br.get_data()
    Time = DataLinspace(
        name="time",
        unit="s",
        symmetries={},
        initial=output.time[0],
        final=output.time[-1],
        number=Nt_tot,
    )
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=output.angle[0],
        final=output.angle[-1],
        number=Na_tot,
    )
    output.Br = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        values=Br,
    )
    if not isinstance(output.Br, DataND) or Br.shape != (Nt_tot, Na_tot):
        raise InputError(
            "ERROR: InputFlux.Br must be a matrix with the shape "
            + str((Nt_tot, Na_tot))
            + " (len(time), stator phase number), "
            + str(Br.shape)
            + " returned"
        )

    if self.Bt is not None:
        Bt = self.Bt.get_data()
        output.Bt = DataTime(
            name="Airgap tangential flux density",
            unit="T",
            symbol="B_t",
            axes=[Time, Angle],
            values=Bt,
        )
        if not isinstance(output.Bt, DataND) or Bt.shape != (Nt_tot, Na_tot):
            raise InputError(
                "ERROR: InputFlux.Bt must be a matrix with the shape "
                + str((Nt_tot, Na_tot))
                + " (len(time), rotor phase number), "
                + str(Bt.shape)
                + " returned"
            )
    else:
        output.Bt = None

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.mag = output
