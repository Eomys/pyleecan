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

    # Load and check alpha_rotor and N0
    if self.angle_rotor is None and self.N0 is None:
        raise InputError(
            "ERROR: InputCurrent.angle_rotor and InputCurrent.N0 can't be None at the same time"
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
                "ERROR: InputCurrent.angle_rotor should be a vector of the same length as time, "
                + str(output.angle_rotor.shape)
                + " shape found, "
                + str(self.Nt_tot)
                + " expected"
            )

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
    if self.Pem_av_ref is not None:
        output.Pem_av_ref = self.Pem_av_ref
    if simu.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    # Save the Output in the correct place
    simu.parent.elec = outelec
