from numpy import pi
from SciDataTool import Data1D, DataLinspace, Norm_ref
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
    if self.time is None and N0 is None:
        raise InputError("ERROR: time and N0 can't be both None")

    # Get machine pole pair number
    p = machine.get_pole_pair_number()

    # Get electrical fundamental frequency
    f_elec = self.comp_felec()

    # Airgap radius
    Rag = machine.comp_Rgap_mec()

    # Setup normalizations for time and angle axes
    norm_time = {
        "elec_order": Norm_ref(ref=f_elec),
        "mech_order": Norm_ref(ref=f_elec / p),
    }
    if N0 is not None:
        norm_time["angle_rotor"] = Norm_ref(ref=1 / (360 * N0 / 60))

    norm_angle = {"space_order": Norm_ref(ref=p), "distance": Norm_ref(ref=1 / Rag)}

    # Create time axis
    if self.time is None:
        # Create time axis as a DataLinspace
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
        # Load time data
        time = self.time.get_data()
        self.Nt_tot = len(time)
        Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)

    # Create angle axis
    if self.angle is None:
        # Create angle axis as a DataLinspace
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            initial=0,
            final=2 * pi,
            number=self.Na_tot,
            include_endpoint=False,
            normalizations=norm_angle,
        )
    else:
        # Load angle data
        angle = self.angle.get_data()
        self.Na_tot = len(angle)
        Angle = Data1D(
            name="angle", unit="rad", values=angle, normalizations=norm_angle
        )

    return Time, Angle
