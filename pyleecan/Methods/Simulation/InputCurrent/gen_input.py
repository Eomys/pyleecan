from numpy import ndarray, pi, mean, transpose, zeros

from ....Classes.Simulation import Simulation

from ....Methods.Simulation.Input import InputError

from ....Functions.Electrical.coordinate_transformation import n2dq
from ....Functions.Winding.gen_phase_list import gen_name

from SciDataTool import Data1D, DataTime


def gen_input(self):
    """Generate the input for the magnetic module (electrical output)

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    # Get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError("InputCurrent object should be inside a Simulation object")

    # Call InputVoltage.gen_input()
    super(type(self), self).gen_input()

    # Get electrical output
    outelec = simu.parent.elec

    # Number of winding phases for stator/rotor
    qs = len(simu.machine.stator.get_name_phase())
    qr = len(simu.machine.rotor.get_name_phase())

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
            Phase = Data1D(
                name="phase",
                unit="",
                values=gen_name(qs),
                is_components=True,
            )
            outelec.Is = DataTime(
                name="Stator current",
                unit="A",
                symbol="Is",
                axes=[Phase, Time],
                values=transpose(Is),
            )
            # Compute corresponding Id/Iq reference
            Idq = n2dq(
                transpose(outelec.Is.values),
                2 * pi * outelec.felec * Time.get_values(is_oneperiod=False),
                n=qs,
                is_dq_rms=True,
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
        # Creating the data object
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qr),
            is_components=True,
        )
        outelec.Ir = DataTime(
            name="Rotor current",
            unit="A",
            symbol="Ir",
            axes=[Phase, Time],
            values=transpose(Ir),
        )

    # Save the Output in the correct place
    simu.parent.elec = outelec
