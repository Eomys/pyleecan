# -*- coding: utf-8 -*-

from ....Classes.OutMag import OutMag
from ....Methods.Simulation.Input import InputError
from SciDataTool import DataLinspace, DataTime, VectorField
from numpy import ndarray


def gen_input(self):
    """Generate the input for the structural module (magnetic output)

    Parameters
    ----------
    self : InFlux
        An InFlux object
    """

    output = OutMag()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InFlux.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: InFlux.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InFlux.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: InFlux.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )
    Na_tot = len(output.angle)

    if self.Br is None:
        raise InputError("ERROR: InFlux.Br missing")
    Br = self.Br.get_data()
    if not isinstance(Br, ndarray) or Br.shape != (Nt_tot, Na_tot):
        raise InputError(
            "ERROR: InFlux.Br must be a matrix with the shape "
            + str((Nt_tot, Na_tot))
            + " (len(time), stator phase number), "
            + str(Br.shape)
            + " returned"
        )
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
    Br_data = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        values=Br,
    )
    output.B = VectorField(
        name="Airgap flux density",
        components={"radial": Br_data}
    )

    if self.Bt is not None:
        Bt = self.Bt.get_data()
        if not isinstance(Bt, ndarray) or Bt.shape != (Nt_tot, Na_tot):
            raise InputError(
                "ERROR: InFlux.Bt must be a matrix with the shape "
                + str((Nt_tot, Na_tot))
                + " (len(time), rotor phase number), "
                + str(Bt.shape)
                + " returned"
            )
        Bt_data = DataTime(
            name="Airgap tangential flux density",
            unit="T",
            symbol="B_t",
            axes=[Time, Angle],
            values=Bt,
        )
        output.B.components["tangential"] = Bt_data

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.mag = output
