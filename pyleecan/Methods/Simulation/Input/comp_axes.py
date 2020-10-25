from numpy import pi
from SciDataTool import Data1D, DataLinspace
from ....Methods.Simulation.Input import InputError


def comp_axes(self, machine, N0=None):
    """Compute simulation axes, i.e. space DataObject including (anti)-periodicity
    and time DataObject including (anti)-periodicity and accounting for rotating speed
    and number of revolutions

    Parameters
    ----------
    self : Input
        an Input object
    machine : Machine
        a Machine object
    N0 : float
        rotating speed [rpm]


    Returns
    -------
    Time : DataLinspace
        Time axis including (anti)-periodicity and accounting for rotating speed and number of revolutions
    Angle : DataLinspace
        Angle axis including (anti)-periodicity

    """

    # Time axis
    norm_time = {
        "elec_order": self.comp_felec(),
        "mech_order": self.comp_felec(),
    }
    if self.time is None:
        if N0 is None:
            raise InputError("ERROR: time and N0 can't be both None")

        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=60 / N0 * self.Nrev,
            number=self.Nt_tot,
            include_endpoint=False,
            normalizations=norm_time,
        )
    else:
        # Load and check time
        time = self.time.get_data()
        self.Nt_tot = len(time)
        Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)

    # Angle axis
    norm_space = {"space_order": machine.get_pole_pair_number()}
    if self.angle is None:
        # Create angle vector as a linspace
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            initial=0,
            final=2 * pi,
            number=self.Na_tot,
            include_endpoint=False,
            normalizations=norm_space,
        )
    else:
        # Load angle data
        angle = self.angle.get_data()
        self.Na_tot = len(angle)
        Angle = Data1D(
            name="angle", unit="rad", values=angle, normalizations=norm_space
        )

    return Time, Angle
