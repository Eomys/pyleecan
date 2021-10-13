from numpy import ndarray, pi

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation

from ....Methods.Simulation.Input import InputError
from ....Functions.Electrical.coordinate_transformation import n2dqh, n2dqh_DataTime
from ....Functions.Winding.gen_phase_list import gen_name

from SciDataTool import Data1D, DataLinspace, DataTime


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
    else:
        raise InputError(
            self.__class__.__name__ + " object should be inside a Simulation object"
        )

    # Get output
    if simu.parent is not None:
        output = simu.parent
    else:
        raise InputError("Simulation object should be inside an Output object")

    # Create the correct Output object
    outelec = OutElec()
    output.elec = outelec
    outgeo = output.geo

    # Calculate electrical frequency and/or speed depending on inputs
    outelec.felec = self.comp_felec()

    # Replace N0=0 by 0.1 rpm
    if self.N0 == 0:
        self.N0 = 0.1
        self.get_logger().debug("Updating N0 from 0 [rpm] to 0.1 [rpm] in gen_input")

    outelec.N0 = self.N0

    if self.U0_ref is None and self.Ud_ref and self.Uq_ref:
        raise Exception("U0_ref, Ud_ref, and Uq_ref cannot be all None in InputVoltage")

    outelec.U0_ref = self.U0_ref
    outelec.Ud_ref = self.Ud_ref
    outelec.Uq_ref = self.Uq_ref
    outelec.slip_ref = self.slip_ref

    # Load and check alpha_rotor and N0
    if self.angle_rotor is None and self.N0 is None:
        raise InputError("angle_rotor and N0 can't be None at the same time")

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

    # Calculate time, angle and phase axes and store them in OutGeo
    outgeo.axes_dict = self.comp_axes(
        axes_list=["time", "angle"],
        is_periodicity_a=False,
        is_periodicity_t=False,
    )

    # Create time axis for electrical model including periodicity
    outelec.axes_dict = self.comp_axes(
        axes_list=["time", "phase_S", "phase_R"],
        axes_dict_in=outgeo.axes_dict,
        is_periodicity_t=False,
    )

    # Generate PWM signal
    if self.PWM is not None:
        # Fill generator with simu data
        felec = self.comp_felec
        rot_dir = output.get_rot_dir()
        qs = simu.machine.stator.winding.qs
        self.PWM.f = felec
        self.fs = self.PWM.fmax * 2.56  # Shanon based sampling frequency (with margin)
        self.PWM.duration = 1 / felec
        # Generate PWM signal
        Uabc, modulation, _, carrier, time = self.PWM.get_data()
        # Create DataTime object
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=time[-1],
            number=len(time),
            include_endpoint=True,
        )
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )
        Uabc_data = DataTime(
            name="Stator voltage",
            symbol="U_{abc}",
            unit="V",
            axes=[Time, Phase],
            values=Uabc,
        )
        # Rotate to DQH frame
        Udqh = n2dqh_DataTime(
            Uabc_data, 2 * pi * felec * time, n=qs, rot_dir=rot_dir, is_dq_rms=True
        )
        # fft
        Udqh_freq = Udqh.time_to_freq()
        # Store
        outelec.Us_harm = Udqh_freq
