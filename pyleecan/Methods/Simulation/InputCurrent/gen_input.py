from numpy import zeros, ones

from SciDataTool import DataTime

from ....Classes.InputVoltage import InputVoltage
from ....Classes.ElecLUTdq import ElecLUTdq

from ....Functions.Electrical.dqh_transformation import get_phase_dir, n2dqh_DataTime

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

    if outelec.axes_dict is not None and "time" in outelec.axes_dict:
        # Get time axis
        Time = outelec.axes_dict["time"]

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            if self.OP.get_Id_Iq()["Id"] is None and self.OP.get_Id_Iq()["Iq"] is None:
                if not isinstance(simu.elec, ElecLUTdq):
                    raise InputError(
                        "InputCurrent.Is, InputCurrent.OP.Id_ref, and InputCurrent.OP.Iq_ref missing"
                    )
            else:
                outelec.OP = self.OP
                outelec.Is = None
        else:
            Is_val = self.Is.get_data()
            Nt_per = Time.get_length(is_smallestperiod=True)
            Phase_S = outelec.axes_dict["phase_" + simu.machine.stator.get_label()]
            try:
                # Get phase_dir from Is
                phase_dir = get_phase_dir(Is_val, current_dir=outelec.current_dir)
                if phase_dir != outelec.phase_dir:
                    self.get_logger().warning(
                        "Enforcing outelec.phase_dir="
                        + str(phase_dir)
                        + " to comply with input current"
                    )
                    outelec.phase_dir = phase_dir
            except Exception:
                # Cannot calculate phase_dir
                self.get_logger().warning(
                    "phase_dir cannot be calculated, please make sure that input.phase_dir="
                    + str(outelec.phase_dir)
                    + " is compliant with enforced currents"
                )
            try:
                # Creating the data object
                Is = DataTime(
                    name="Stator current",
                    unit="A",
                    symbol="I_s",
                    axes=[Time, Phase_S],
                    values=Is_val,
                )
            except Exception:
                raise InputError(
                    "InputCurrent.Is must be a matrix with the shape "
                    + str((Nt_per, qs))
                    + " (len(time), stator phase number), "
                    + str(Is_val.shape)
                    + " returned"
                )
            # Compute corresponding Id/Iq reference
            Idq = n2dqh_DataTime(
                Is,
                is_dqh_rms=True,
                phase_dir=outelec.phase_dir,
            )
            Idq_mean = Idq.get_along("time=mean", "phase")[Is.symbol]
            # Store currents in OutElec
            outelec.OP.set_Id_Iq(Idq_mean[0], Idq_mean[1])
            outelec.Is = Is

        if self.Is_harm is not None:
            # Enforce current harmonics
            # TODO: merge Is_harm and Is_fund
            outelec.Is_harm = self.Is_harm.get_data()

    # Load and check if Ir is needed
    if qr > 0:
        Nt_per = Time.get_length(is_smallestperiod=True)
        Phase_R = outelec.axes_dict["phase_" + simu.machine.rotor.get_label()]
        qr_per = Phase_R.get_length(is_smallestperiod=True)
        if hasattr(self.OP, "If_ref"):  # WRSM case
            Ir_val = ones((Nt_per, qr_per)) * self.OP.If_ref
        elif self.Ir is None:
            Ir_val = zeros((Nt_per, qr_per))
        else:
            Ir_val = self.Ir.get_data()
            if Ir_val.ndim == 1:
                # time axis is squeeze, putting it back to first dimension
                Ir_val = Ir_val[None, :]
            if Ir_val.shape[1] > qr_per:
                Ir_val = Ir_val[:, :qr_per]
                self.get_logger().info(
                    "Restrict input rotor bar currents to smallest spatial periodicity"
                )

        try:
            Ir = DataTime(
                name="Rotor current",
                unit="A",
                symbol="Ir",
                axes=[Time, Phase_R],
                values=Ir_val,
            )
        except Exception:
            raise InputError(
                "InputCurrent.Ir must be a matrix with the shape "
                + str((Nt_per, qr_per))
                + " (len(time), rotor phase number), "
                + str(Ir_val.shape)
                + " returned"
            )

        outelec.Ir = Ir

    if outelec.PWM is not None:
        Udq_dict = outelec.OP.get_Ud_Uq()
        Ud_ref, Uq_ref = Udq_dict["Ud"], Udq_dict["Uq"]
        # Check PWM phase voltage consistency in current driven mode
        if outelec.PWM.U0 is not None or Ud_ref is not None or Uq_ref is not None:
            if outelec.PWM.U0 is not None:
                self.get_logger().warning(
                    "Neglecting U0 given as input of PWM object since voltage will be calculated"
                )
            if Ud_ref is not None or Uq_ref is not None:
                self.get_logger().warning(
                    "Neglecting Ud_ref/Uq_ref given as input since voltage will be calculated"
                )
        # Set all voltages to None since they will be calculated by Electrical model
        outelec.PWM.U0 = None
        outelec.PWM.Phi0 = None
        outelec.OP.Ud_ref = None
        outelec.OP.Uq_ref = None
