from numpy import arange, searchsorted, angle

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation

from ....Methods.Simulation.Input import (
    CURRENT_DIR_REF,
    ROT_DIR_REF,
    InputError,
    PHASE_DIR_REF,
)


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

    logger = self.get_logger()

    # Create the correct Output object
    outelec = OutElec()
    output.elec = outelec
    outgeo = output.geo

    # Replace N0=0 by 0.1 rpm
    if self.OP.N0 == 0:
        self.OP.N0 = 0.1
        logger.debug("Updating N0 from 0 [rpm] to 0.1 [rpm] in gen_input")
    # Check that felec/N0 can be computed
    self.OP.get_felec()
    outelec.OP = self.OP

    # Set rotor rotation direction
    if self.rot_dir is None:
        self.rot_dir = ROT_DIR_REF
    elif self.rot_dir not in [-1, 1]:
        raise Exception("Cannot enforce rot_dir other than +1 or -1")
    outgeo.rot_dir = self.rot_dir

    # Set current rotation direction
    if self.current_dir is None:
        self.current_dir = CURRENT_DIR_REF
    elif self.current_dir not in [-1, 1]:
        raise Exception("Cannot enforce current_dir other than +1 or -1")
    outelec.current_dir = self.current_dir

    # Set phase rotation direction
    if self.phase_dir is None:
        self.phase_dir = PHASE_DIR_REF
    elif self.phase_dir not in [-1, 1]:
        raise Exception("Cannot enforce phase_dir other than +1 or -1")
    outelec.phase_dir = self.phase_dir

    # Check if stator magnetomotive force direction is consistent with rotor direction
    mmf_dir = simu.machine.stator.comp_mmf_dir(
        current_dir=self.current_dir, phase_dir=self.phase_dir
    )
    if mmf_dir != -self.rot_dir:
        # Switch phase direction to reverse rotation direction
        self.phase_dir = -self.phase_dir
        logger.info(
            "Reverse the two last stator current phases to reverse rotation direction of stator mmf fundamental according to rotor direction"
        )
    outelec.phase_dir = self.phase_dir

    # Set rotor initial angular position
    if self.angle_rotor_initial in [0, None]:
        # Calculate initial position according to machine properties
        self.angle_rotor_initial = simu.machine.comp_angle_rotor_initial()
    output.geo.angle_rotor_initial = self.angle_rotor_initial

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
        is_periodicity_a=self.is_periodicity_a,
        is_periodicity_t=self.is_periodicity_t,
    )

    # Generate PWM signal
    if self.PWM is not None:
        outelec.PWM = self.PWM.copy()
        Udq_dict = outelec.OP.get_Ud_Uq()
        Ud_ref, Uq_ref = Udq_dict["Ud"], Udq_dict["Uq"]
        # Check PWM phase voltage consistency in voltage driven mode
        if Ud_ref is not None or Uq_ref is not None:
            U0c = Ud_ref + 1j * Uq_ref
            if (
                self.PWM.U0 is not None
                and outelec.PWM.Phi0 is not None
                and (outelec.PWM.U0 != abs(U0c) or outelec.PWM.Phi0 != angle(U0c))
            ):
                logger.warning("Enforcing PWM.U0 = Ud_ref + jUq_ref")
            outelec.PWM.U0 = abs(U0c)
            outelec.PWM.Phi0 = angle(U0c)
        # Fill generator with simu data
        felec = self.OP.get_felec()
        qs = simu.machine.stator.winding.qs
        outelec.PWM.f = felec
        outelec.PWM.qs = qs
        outelec.PWM.phase_dir = outelec.phase_dir
        outelec.PWM.current_dir = outelec.current_dir
        # Take sampling frequency as 2*fmax to catch fmax components
        outelec.PWM.fs = 2 * outelec.PWM.fmax
        # Set PWM duration as 2*p times the electrical period (to increase frequency resolution)
        outelec.PWM.duration = 2 * simu.machine.get_pole_pair_number() / felec
