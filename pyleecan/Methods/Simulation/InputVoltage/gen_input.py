from SciDataTool import Norm_ref
from numpy import ndarray, arange, searchsorted, ceil

from ....Classes.OutElec import OutElec
from ....Classes.Simulation import Simulation
from ....Classes.OPdq import OPdq
from ....Classes.OPslip import OPslip
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
    output.elec.OP = self.OP

    # Set rotor rotation direction
    if self.rot_dir not in [-1, 1]:
        # Enforce rotor rotation direction to -1
        logger.info("Enforcing rotor rotating direction to -1: clockwise rotation")
        self.rot_dir = -1
    outgeo.rot_dir = self.rot_dir

    # Set current rotation direction
    if self.current_dir not in [-1, 1]:
        # Enforce current rotation direction to 1
        logger.info("Enforcing current rotating direction to 1: clockwise rotation")
        self.current_dir = 1
    outgeo.current_dir = self.current_dir

    # Check if stator magnetomotive force direction is consistent with rotor direction
    mmf_dir = simu.machine.stator.comp_mmf_dir(felec=1, current_dir=self.current_dir)
    if mmf_dir != -self.rot_dir:
        logger.debug(
            "Reverse current rotation direction so that stator mmf rotates in same direction as rotor"
        )
        self.current_dir = -self.current_dir

    # Set rotor initial angular position
    if self.angle_rotor_initial in [0, None]:
        # Calculate initial position according to machine properties
        self.angle_rotor_initial = simu.machine.comp_angle_offset_initial()
    output.geo.angle_offset_initial = self.angle_rotor_initial

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
        felec = self.OP.get_felec()
        rot_dir = outgeo.rot_dir
        qs = simu.machine.stator.winding.qs
        self.PWM.f = felec
        self.PWM.qs = qs
        self.PWM.rot_dir = rot_dir
        self.PWM.duration = 1 / felec
        self.PWM.typePWM = 8
        self.PWM.Vdc1 *= 2  # In comp_PWM, max is Vdc1/2
        # Compute sampling frequency (even multiple of fswi + close to 2*fmax)
        mult = arange(1, 100)
        ind = searchsorted(2 * mult * self.PWM.fswi, 2 * self.PWM.fmax, side="right")
        self.PWM.fs = 2 * mult[ind] * self.PWM.fswi
        # Generate PWM signal
        Uabc, _, _, _, time = self.PWM.get_data(is_norm=False)
        # Create DataTime object
        self.time = time
        Time = self.comp_axis_time(
            simu.machine.get_pole_pair_number(),
            per_t=1,
            is_antiper_t=False,
            output=output,
        )
        Phase = self.comp_axis_phase(simu.machine.stator)
        outelec.Us_PWM = DataTime(
            name="Stator voltage",
            symbol="U_s",
            unit="V",
            axes=[Time, Phase],
            values=Uabc,
        )
