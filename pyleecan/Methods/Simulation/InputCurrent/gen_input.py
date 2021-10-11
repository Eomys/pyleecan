from numpy import ndarray, mean, zeros

from ....Methods.Simulation.Input import InputError

from ....Functions.Electrical.coordinate_transformation import n2dqh
from ....Classes.InputVoltage import InputVoltage

from SciDataTool import Data1D, DataTime


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
            if self.Id_ref is None and self.Iq_ref is None:
                raise InputError(
                    "InputCurrent.Is, InputCurrent.Id_ref, and InputCurrent.Iq_ref missing"
                )
            else:
                outelec.Id_ref = self.Id_ref
                outelec.Iq_ref = self.Iq_ref
                outelec.Is = None
        else:
            Is = self.Is.get_data()
            if not isinstance(Is, ndarray) or Is.shape != (self.Nt_tot, qs):
                raise InputError(
                    "InputCurrent.Is must be a matrix with the shape "
                    + str((self.Nt_tot, qs))
                    + " (len(time), stator phase number), "
                    + str(Is.shape)
                    + " returned"
                )
            # Creating the data object
            outelec.Is = DataTime(
                name="Stator current",
                unit="A",
                symbol="I_s",
                axes=[Time, outelec.axes_dict["phase_S"]],
                values=Is,
            )
            # Compute corresponding Id/Iq reference
            Idq = n2dqh(
                outelec.Is.values,
                Time.get_values(is_oneperiod=False, normalization="angle_elec"),
                is_dqh_rms=True,
            )
            outelec.Id_ref = mean(Idq[:, 0])
            outelec.Iq_ref = mean(Idq[:, 1])

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            Ir = zeros((self.Nt_tot, qr))
        else:
            Ir = self.Ir.get_data()
        if not isinstance(Ir, ndarray) or Ir.shape != (self.Nt_tot, qr):
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
            axes=[Time, outelec.axes_dict["phase_R"]],
            values=Ir,
        )
