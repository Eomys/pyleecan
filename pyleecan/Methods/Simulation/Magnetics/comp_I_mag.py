from numpy import transpose


def comp_I_mag(self, output, Time):
    """Compute the currents on both stator and rotor laminations for given Magnetics time axis
    Phase currents are divided by the number of parallel circuits per pole and per phase to account
    for actual current in slot conductors

    Parameters
    ----------
    self : Magnetics
        an Magnetics object
    output: Output
        An Output object
    Time : Data
        Time vector on which to interpolate currents stored in OutElec

    Returns
    -------
    Is_val: ndarray
        Stator current matrix accounting for magnetic periodicities [qs_pera,len(time)]
    Ir_val: ndarray
        Rotor current matrix accounting for magnetic periodicities [qr_pera,len(time)]
    """

    logger = self.get_logger()

    # Extract time vector
    time = Time.get_values(is_smallestperiod=True)

    # Get laminations
    stator = output.simu.machine.stator
    rotor = output.simu.machine.rotor

    # Get stator current from electrical output
    if (
        self.is_mmfs
        and hasattr(stator, "winding")
        and stator.winding is not None
        and stator.winding.conductor is not None
    ):
        # Get Data object on magnetic Time axis
        Is = output.elec.get_Is(Time=Time)

        # Get the number of parallel circuit per phase of winding
        if hasattr(stator.winding, "Npcp") and stator.winding.Npcp is not None:
            Npcp = stator.winding.Npcp
        else:
            logger.warning("Enforcing Npcp=1 at stator side")
            Npcp = 1

        # Interpolate stator currents on input time vector
        Is_val = transpose(
            Is.get_along(
                "time=axis_data",
                "phase",
                axis_data={"time": time},
                is_squeeze=False,
            )[Is.symbol]
            / Npcp
        )

    else:
        Is_val = None

    # Get rotor current from electrical output
    if (
        self.is_mmfr
        and output.elec.Ir is not None
        and hasattr(rotor, "winding")
        and rotor.winding is not None
        and rotor.winding.conductor is not None
    ):
        # Get Data object
        Ir = output.elec.Ir

        # Get the number of parallel circuit per phase of winding
        if hasattr(rotor.winding, "Npcp") and rotor.winding.Npcp is not None:
            Npcp = rotor.winding.Npcp
        else:
            logger.warning("Enforcing Npcp=1 at rotor side")
            Npcp = 1

        if len(Ir.get_axes("phase")[0].symmetries) > 0 and self.is_periodicity_a:
            str_phase = "phase[oneperiod]"
        else:
            str_phase = "phase"

        # Interpolate stator currents on input time vector
        Ir_val = transpose(
            Ir.get_along(
                "time=axis_data",
                str_phase,
                axis_data={"time": time},
                is_squeeze=False,
            )[Ir.symbol]
            / Npcp
        )

    else:
        Ir_val = None

    return Is_val, Ir_val
