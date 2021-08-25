from numpy import ndarray

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation
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
    output = OutElec()

    # Set discretization
    Time, Angle = self.comp_axes(simu.machine)
    output.Time = Time
    output.Angle = Angle

    output.N0 = self.N0
    output.felec = self.comp_felec()  # TODO introduce set_felec(slip)

    if self.U0_ref is None and self.Ud_ref and self.Uq_ref:
        raise Exception("U0_ref, Ud_ref, and Uq_refcannot be all None in InputVoltage")

    output.U0_ref = self.U0_ref

    # Generate Us
    # if qs > 0:
    # TODO
    #     if self.Is is None:
    #         if self.Id_ref is None and self.Iq_ref is None:
    #             raise InputError(
    #                 "ERROR: InputVoltage.Is, InputVoltage.Id_ref, and InputVoltage.Iq_ref missing"
    #             )
    #         else:
    #             output.Id_ref = self.Id_ref
    #             output.Iq_ref = self.Iq_ref
    #             output.Is = None
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
    #         output.Is = DataTime(
    #             name="Stator current",
    #             unit="A",
    #             symbol="Is",
    #             axes=[Phase, Time],
    #             values=transpose(Is),
    #         )
    #         # Compute corresponding Id/Iq reference
    #         Idq = n2dq(
    #             transpose(output.Is.values),
    #             2 * pi * output.felec * output.Time.get_values(is_oneperiod=False),
    #             n=qs,
    #             is_dq_rms=True,
    #         )
    #         output.Id_ref = mean(Idq[:, 0])
    #         output.Iq_ref = mean(Idq[:, 1])  # TODO use of mean has to be documented

    # Load and check alpha_rotor and N0
    if self.angle_rotor is None and self.N0 is None:
        raise InputError(
            "InputVoltage.angle_rotor and InputVoltage.N0 can't be None at the same time"
        )
    if self.angle_rotor is not None:
        output.angle_rotor = self.angle_rotor.get_data()
        if (
            not isinstance(output.angle_rotor, ndarray)
            or len(output.angle_rotor.shape) != 1
            or output.angle_rotor.size != self.Nt_tot
        ):
            # angle_rotor should be a vector of same length as time
            raise InputError(
                "InputVoltage.angle_rotor should be a vector of the same length as time, "
                + str(output.angle_rotor.shape)
                + " shape found, "
                + str(self.Nt_tot)
                + " expected"
            )

    simu.parent.elec.slip_ref = self.slip_ref

    if self.rot_dir is None or self.rot_dir not in [-1, 1]:
        # Enforce default rotation direction
        # simu.parent.geo.rot_dir = None
        pass  # None is already the default value
    else:
        simu.parent.geo.rot_dir = self.rot_dir

    if self.angle_rotor_initial is None:
        # Enforce default initial position
        output.angle_rotor_initial = 0
    else:
        output.angle_rotor_initial = self.angle_rotor_initial

    if self.Tem_av_ref is not None:
        output.Tem_av_ref = self.Tem_av_ref

    if simu.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    # Save the Output in the correct place
    simu.parent.elec = output
