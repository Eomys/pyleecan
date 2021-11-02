from numpy import mean as np_mean, zeros

from SciDataTool import DataTime

from ....Classes.InputVoltage import InputVoltage

from ....Functions.Electrical.dqh_transformation import n2dqh, get_phase_dir

from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    # Call InputVoltage.gen_input()
    InputVoltage.gen_input(self)

    # Get simulation and outputs
    simu = self.parent
    output = simu.parent
    outelec = output.elec

    # Number of winding phases for stator/rotor
    if simu.machine is not None:
        qs = len(simu.machine.stator.get_name_phase())
        qr = len(simu.machine.rotor.get_name_phase())
    else:
        qs = 0
        qr = 0

    # Get time axis
    Time = outelec.axes_dict["time"]

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            if self.OP.Id_ref is None and self.OP.Iq_ref is None:
                raise InputError(
                    "InputCurrent.Is, InputCurrent.OP.Id_ref, and InputCurrent.OP.Iq_ref missing"
                )
            else:
                outelec.OP = self.OP
                outelec.Is = None
        else:
            Is = self.Is.get_data()
            # Get phase_dir from Is
            phase_dir = get_phase_dir(Is)
            if phase_dir != outelec.phase_dir:
                self.get_logger().warning(
                    "Enforcing outelec.phase_dir="
                    + str(phase_dir)
                    + " to comply with input current"
                )
                outelec.phase_dir = phase_dir
            if Is.shape != (self.Nt_tot, qs):
                raise InputError(
                    "InputCurrent.Is must be a matrix with the shape "
                    + str((self.Nt_tot, qs))
                    + " (len(time), stator phase number), "
                    + str(Is.shape)
                    + " returned"
                )
            # Creating the data object
            stator_label = "phase_" + simu.machine.stator.get_label()
            outelec.Is = DataTime(
                name="Stator current",
                unit="A",
                symbol="I_s",
                axes=[Time, outelec.axes_dict[stator_label]],
                values=Is,
            )
            # Compute corresponding Id/Iq reference
            Idq = n2dqh(
                outelec.Is.values,
                Time.get_values(is_oneperiod=False, normalization="angle_elec"),
                is_dqh_rms=True,
                phase_dir=outelec.phase_dir,
            )
            outelec.OP.set_Id_Iq(np_mean(Idq[:, 0]), np_mean(Idq[:, 1]))

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            Ir = zeros((self.Nt_tot, qr))
        else:
            Ir = self.Ir.get_data()
        if Ir.shape != (self.Nt_tot, qr):
            raise InputError(
                "InputCurrent.Ir must be a matrix with the shape "
                + str((self.Nt_tot, qr))
                + " (len(time), rotor phase number), "
                + str(Ir.shape)
                + " returned"
            )

        outelec.Ir = DataTime(
            name="Rotor current",
            unit="A",
            symbol="Ir",
            axes=[Time, outelec.axes_dict["phase_" + simu.machine.rotor.get_label()]],
            values=Ir,
        )
