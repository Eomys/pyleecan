from numpy import ndarray

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation

from ....Functions.Simulation.create_from_axis import create_from_axis

from ....Methods.Simulation.Input import InputError

# from ....Functions.Electrical.coordinate_transformation import n2dq
# from SciDataTool import Data1D, DataTime
# from ....Functions.Winding.gen_phase_list import gen_name


def gen_input(self):
    """Generate the input for the electrical module (electrical output filled with voltage)

    Parameters
    ----------
    self : InputVoltage
        An InputVoltage object
    """

    # Get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError("InputVoltage object should be inside a Simulation object")

    # Create the correct Output object
    outelec = OutElec()
    outgeo = simu.parent.geo

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

    outelec.N0 = self.N0
    outelec.felec = self.comp_felec()  # TODO introduce set_felec(slip)

    if self.U0_ref is None and self.Ud_ref and self.Uq_ref:
        raise Exception("U0_ref, Ud_ref, and Uq_refcannot be all None in InputVoltage")

    outelec.U0_ref = self.U0_ref

    outelec.slip_ref = self.slip_ref

    # Generate Us
    # if qs > 0:
    # TODO
    #     if self.Is is None:
    #         if self.Id_ref is None and self.Iq_ref is None:
    #             raise InputError(
    #                 "ERROR: InputVoltage.Is, InputVoltage.Id_ref, and InputVoltage.Iq_ref missing"
    #             )
    #         else:
    #             outelec.Id_ref = self.Id_ref
    #             outelec.Iq_ref = self.Iq_ref
    #             outelec.Is = None
    #     else:
    #         Is = self.Is.get_data()
    #         if not isinstance(Is, ndarray) or Is.shape != (self.Nt_tot, qs):
    #             raise InputError(
    #                 "ERROR: InputVoltage.Is must be a matrix with the shape "
    #                 + str((self.Nt_tot, qs))
    #                 + " (len(time), stator phase number), "
    #                 + str(Is.shape)
    #                 + " returned"
    #             )
    #         # Creating the data object
    #         Phase = Data1D(
    #             name="phase",
    #             unit="",
    #             values=gen_name(qs),
    #             is_components=True,
    #         )
    #         outelec.Is = DataTime(
    #             name="Stator current",
    #             unit="A",
    #             symbol="Is",
    #             axes=[Phase, Time],
    #             values=transpose(Is),
    #         )
    #         # Compute corresponding Id/Iq reference
    #         Idq = n2dq(
    #             transpose(outelec.Is.values),
    #             2 * pi * outelec.felec * outelec.axes_dict["time"].get_values(is_oneperiod=False),
    #             n=qs,
    #             is_dq_rms=True,
    #         )
    #         outelec.Id_ref = mean(Idq[:, 0])
    #         outelec.Iq_ref = mean(Idq[:, 1])  # TODO use of mean has to be documented

    # Load and check alpha_rotor and N0
    if self.angle_rotor is None and self.N0 is None:
        raise InputError(
            "InputVoltage.angle_rotor and InputVoltage.N0 can't be None at the same time"
        )
    if self.angle_rotor is not None:
        outelec.angle_rotor = self.angle_rotor.get_data()
        if (
            not isinstance(outelec.angle_rotor, ndarray)
            or len(outelec.angle_rotor.shape) != 1
            or outelec.angle_rotor.size != self.Nt_tot
        ):
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "InputVoltage.angle_rotor should be a vector of the same length as time, "
                + str(outelec.angle_rotor.shape)
                + " shape found, "
                + str(self.Nt_tot)
                + " expected"
            )

    if self.rot_dir is not None:
        if self.rot_dir in [-1, 1]:
            # Enforce user-defined rotation direction
            outgeo.rot_dir = self.rot_dir
        else:
            # Enforce calculation of rotation direction
            outgeo.rot_dir = None

    if self.angle_rotor_initial is None:
        # Enforce default initial position
        outelec.angle_rotor_initial = 0
    else:
        outelec.angle_rotor_initial = self.angle_rotor_initial

    if self.Tem_av_ref is not None:
        outelec.Tem_av_ref = self.Tem_av_ref

    if simu.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    # Save the Output in the correct place
    simu.parent.elec = outelec
