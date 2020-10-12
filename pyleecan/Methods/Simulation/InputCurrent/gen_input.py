# -*- coding: utf-8 -*-

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation
from ....Methods.Simulation.Input import InputError
from numpy import ndarray, linspace, pi, mean, transpose
from ....Functions.Electrical.coordinate_transformation import n2dq
from SciDataTool import Data1D, DataTime
from ....Functions.Winding.gen_phase_list import gen_name


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
        raise InputError(
            "ERROR: InputCurrent object should be inside a Simulation object"
        )

    # Create the correct Output object
    output = OutElec()

    # Set discretization
    Time, Angle = self.comp_axes(simu.machine, self.N0)
    output.time = Time
    output.angle = Angle

    # Number of winding phases for stator/rotor
    qs = len(simu.machine.stator.get_name_phase())
    qr = len(simu.machine.rotor.get_name_phase())

    output.N0 = self.N0
    output.felec = self.comp_felec()  # TODO introduce set_felec(slip)

    # Load and check Is
    if qs > 0:
        if self.Is is None:
            if self.Id_ref is None and self.Iq_ref is None:
                raise InputError(
                    "ERROR: InputCurrent.Is, InputCurrent.Id_ref, and InputCurrent.Iq_ref missing"
                )
            else:
                output.Id_ref = self.Id_ref
                output.Iq_ref = self.Iq_ref
                output.Is = None
        else:
            Is = self.Is.get_data()
            if not isinstance(Is, ndarray) or Is.shape != (self.Nt_tot, qs):
                raise InputError(
                    "ERROR: InputCurrent.Is must be a matrix with the shape "
                    + str((self.Nt_tot, qs))
                    + " (len(time), stator phase number), "
                    + str(Is.shape)
                    + " returned"
                )
            # Creating the data object
            Phase = Data1D(
                name="phase",
                unit="",
                values=gen_name(qs, is_add_phase=True),
                is_components=True,
            )
            output.Is = DataTime(
                name="Stator current",
                unit="A",
                symbol="Is",
                axes=[Phase, Time],
                values=transpose(Is),
            )
            # Compute corresponding Id/Iq reference
            Idq = n2dq(
                transpose(output.Is.values),
                2 * pi * output.felec * output.time.get_values(is_oneperiod=False),
                is_dq_rms=True,
            )
            output.Id_ref = mean(Idq[:, 0])
            output.Iq_ref = mean(Idq[:, 1])  # TODO use of mean has to be documented

    # Load and check Ir is needed
    if qr > 0:
        if self.Ir is None:
            raise InputError("ERROR: InputCurrent.Ir missing")
        else:
            Ir = self.Ir.get_data()
            if not isinstance(Ir, ndarray) or Ir.shape != (self.Nt_tot, qr):
                raise InputError(
                    "ERROR: InputCurrent.Ir must be a matrix with the shape "
                    + str((self.Nt_tot, qr))
                    + " (len(time), rotor phase number), "
                    + str(Ir.shape)
                    + " returned"
                )
            # Creating the data object
            Phase = Data1D(
                name="phase",
                unit="",
                values=gen_name(qr, is_add_phase=True),
                is_components=True,
            )
            output.Ir = DataTime(
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
        simu.parent.geo.rot_dir = None
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
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    # Save the Output in the correct place
    simu.parent.elec = output
