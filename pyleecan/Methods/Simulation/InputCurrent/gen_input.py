from numpy import ndarray, pi, mean, zeros

from ....Classes.Simulation import Simulation

from ....Methods.Simulation.Input import InputError

from ....Functions.Electrical.coordinate_transformation import n2dq
from ....Functions.Winding.gen_phase_list import gen_name
from ....Classes.InputVoltage import InputVoltage

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

    # Get output
    if simu.parent is not None:
        output = simu.parent
    else:
        raise InputError("Simulation object should be inside an Output object")

    # Call InputVoltage.gen_input()
    InputVoltage.gen_input(self)

    # Get outputs
    outgeo = output.geo
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
                axes=[Time, outgeo.axes_dict["phase"]],
                values=Is,
            )
            # Compute corresponding Id/Iq reference
            Idq = n2dq(
                outelec.Is.values,
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
            axes=[Time, Phase],
            values=Ir,
        )
