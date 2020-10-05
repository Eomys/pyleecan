from numpy import pi
from SciDataTool import Data1D, DataLinspace


def comp_axes(self, machine, N0):
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
    # Compute machine (anti)-periodicities in time and space domains
    per_a, is_aper_a, per_t, is_aper_t = machine.comp_periodicity()

    # Time axis
    if self.time is None:
        # Create time vector as a linspace

        # Time axis including (anti)-periodicity and accounting for rotating speed and number of revolutions
        if is_aper_t:
            per_t = 2 * per_t
            dict_per_t = {"antiperiod": per_t}
        else:
            dict_per_t = {"period": per_t}

        Time = DataLinspace(
            name="time",
            unit="s",
            symmetries={"time": dict_per_t},
            initial=0,
            final=60 / N0 * self.Nrev / per_t,
            number=round(self.Nt_tot / per_t),
            include_endpoint=False,
        )
    else:
        # Load and check time
        time = self.time.get_data()
        self.Nt_tot = len(time)
        Time = Data1D(name="time", unit="s", values=time)

    # Angle axis
    if self.angle is None:
        # Create angle vector as a linspace

        # Angle axis including (anti)-periodicity
        if is_aper_a:
            per_a = 2 * per_a
            dict_per_a = {"antiperiod": per_a}
        else:
            dict_per_a = {"period": per_a}

        Angle = DataLinspace(
            name="angle",
            unit="rad",
            symmetries={"angle": dict_per_a},
            initial=0,
            final=2 * pi / per_a,
            number=round(self.Na_tot / per_a),
            include_endpoint=False,
        )
    else:
        # Load angle data
        angle = self.angle.get_data()
        self.Na_tot = len(angle)
        Angle = Data1D(name="angle", unit="rad", values=angle)

    return Time, Angle
