from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation

from ....Functions.Simulation.create_from_axis import create_from_axis

from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    # get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError("InputCurrent object should be inside a Simulation object")

    outelec = OutElec()
    outgeo = simu.parent.geo

    outelec.N0 = self.N0
    outelec.felec = self.comp_felec()

    # Set time and angle full axes in geometry output
    Time, Angle = self.comp_axes(simu.machine)
    outgeo.axes_dict = {"time": Time, "angle": Angle}

    # Create time axis in electrical output without periodicity
    # TODO: account for pole periodicity
    Time_elec = Time.copy()
    Time_elec, _ = create_from_axis(
        axis_in=Time,
        per=1,  # int(2 * simu.machine.get_pole_pair_number()),
        is_aper=False,  # True,
        is_include_per=False,  # True,
        is_remove_aper=True,  # False,
    )
    outelec.axes_dict = {"time": Time_elec}

    # Initialize outelec at None
    outelec.Id_ref = None
    outelec.Iq_ref = None
    outelec.Ud_ref = None
    outelec.Uq_ref = None
    outelec.Is = None
    outelec.Ir = None

    # Load and check voltage and currents
    if self.Ud_ref is not None and self.Uq_ref is not None:
        outelec.Ud_ref = self.Ud_ref
        outelec.Uq_ref = self.Uq_ref
        simu.elec.eec.parameters["Ud"] = self.Ud_ref
        simu.elec.eec.parameters["Uq"] = self.Uq_ref
        if self.Id_ref is not None and self.Iq_ref is not None:
            outelec.Id_ref = self.Id_ref
            outelec.Iq_ref = self.Iq_ref
        else:
            outelec.Id_ref = 1
            outelec.Iq_ref = 1
    elif self.Id_ref is not None and self.Iq_ref is not None:
        outelec.Id_ref = self.Id_ref
        outelec.Iq_ref = self.Iq_ref
    else:
        raise InputError("Id/Iq or Ud/Uq missing")

    # Load and check rot_dir
    if self.rot_dir is None or self.rot_dir not in [-1, 1]:
        # Enforce default rotation direction
        outgeo.rot_dir = -1
    else:
        outgeo.rot_dir = self.rot_dir

    if simu.parent is None:
        raise InputError("The Simulation object must be in an outelec object to run")

    # Save the Output in the correct place
    simu.parent.elec = outelec
