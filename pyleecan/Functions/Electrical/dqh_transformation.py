import numpy as np

from SciDataTool import Data1D, DataFreq, DataTime, DataDual, DataND

from ...Functions.Winding.gen_phase_list import gen_name


def n2dqh_DataTime(data_n, is_dqh_rms=True, phase_dir=None):
    """n phases to dqh equivalent coordinate transformation of DataTime object

    Parameters
    ----------
    data_n : DataTime
        data object containing values over time and phase axes
    is_dqh_rms : boolean
        True to return dq currents in rms value (Pyleecan convention), False to return peak values
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    data_dqh : DataTime
        data object transformed in dqh frame

    """

    if phase_dir is None:
        # Check if input data object is compliant with dqh transformation
        # and get phase_dir from data object
        phase_dir = get_phase_dir_DataTime(data_n)
    else:
        # Only check if input data object is compliant with dqh transformation
        _check_data(data_n)

    if "angle_elec" not in data_n.axes[0].normalizations:
        raise Exception("Time axis should contain angle_elec normalization")

    # Get values for one time period converted in electrical angle and for all phases
    angle_elec = data_n.axes[0].get_values(
        normalization="angle_elec", is_oneperiod=True
    )
    data_n_val = data_n.get_along("time[oneperiod]", "phase")[data_n.symbol]

    # Convert values to dqh frame
    data_dqh_val = n2dqh(data_n_val, angle_elec, is_dqh_rms, phase_dir)

    # Get time axis on one period
    per_t, is_aper_t = data_n.axes[0].get_periodicity()
    per_t = int(per_t / 2) if is_aper_t else per_t
    Time = data_n.axes[0].get_axis_periodic(per_t, is_aper=False)

    # Create DQH axis
    axis_dq = Data1D(
        name="phase",
        unit="",
        values=["direct", "quadrature", "homopolar"],
        is_components=True,
    )

    # Get normalizations
    normalizations = dict()
    if data_n.normalizations is not None and len(data_n.normalizations) > 0:
        for key, val in data_n.normalizations.items():
            normalizations[key] = val.copy()

    # Create DataTime object in dqh frame
    data_dqh = DataTime(
        name=data_n.name + " in DQH frame",
        unit=data_n.unit,
        symbol=data_n.symbol,
        values=data_dqh_val,
        axes=[Time, axis_dq],
        normalizations=normalizations,
        is_real=data_n.is_real,
    )

    return data_dqh


def n2dqh(Z_n, angle_elec, is_dqh_rms=True, phase_dir=None):
    """n phases to dqh equivalent coordinate transformation

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phases values
    angle_elec : ndarray
        angle of the rotor coordinate system
    is_dqh_rms : boolean
        True to return dq currents in rms value (Pyleecan convention), False to return peak values
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    Z_dqh : ndarray
        transformed matrix (N x 3) of dqh equivalent values
    """

    if phase_dir is None:
        # Get phase_dir from Z_n
        phase_dir = get_phase_dir(Z_n)

    Z_dqh = abc2dqh(n2abc(Z_n, phase_dir), angle_elec)

    if is_dqh_rms:
        # Divide by sqrt(2) to go from (Id_peak, Iq_peak) to (Id_rms, Iq_rms)
        Z_dqh /= np.sqrt(2)

    return Z_dqh


def n2abc(Z_n, phase_dir=None):
    """n phase to 3 phases equivalent coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phase values
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    Z_abc : ndarray
        transformed matrix (N x 3) of 3 phases equivalent values (alpha-beta-gamma)

    """

    n = Z_n.shape[1]

    n_2_abc = comp_Clarke_transform(n, is_inv=False, phase_dir=phase_dir)

    Z_abc = np.matmul(Z_n, n_2_abc)

    return Z_abc


def abc2dqh(Z_abc, angle_elec):
    """alpha-beta-gamma to dqh coordinate transformation

    Parameters
    ----------
    Z_abc : ndarray
        matrix (N x 3) of alpha-beta-gamma - reference frame values
    angle_elec : ndarray
        angle of the rotor coordinate system

    Returns
    -------
    Z_dqh : ndarray
        transformed (dqh) values

    """

    if Z_abc.ndim == 1:
        Z_abc = Z_abc[None, :]

    sin_angle_elec = np.sin(angle_elec)
    cos_angle_elec = np.cos(angle_elec)

    Z_dqh = np.zeros((angle_elec.size, 3))

    # d-axis
    Z_dqh[:, 0] = Z_abc[:, 0] * cos_angle_elec + Z_abc[:, 1] * sin_angle_elec
    # q-axis
    Z_dqh[:, 1] = -Z_abc[:, 0] * sin_angle_elec + Z_abc[:, 1] * cos_angle_elec
    # Homopolar axis
    Z_dqh[:, 2] = Z_abc[:, 2]

    return Z_dqh


def dqh2n_DataTime(data_dqh, n, is_n_rms=False, phase_dir=None):
    """dqh to n phase coordinate transformation of DataTime object

    Parameters
    ----------
    data_dqh : DataTime
        data object containing values over time in dqh frame
    n: int
        number of phases
    is_n_rms : boolean
        True to return n currents in rms value, False to return peak values (Pyleecan convention)
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    data_n : DataTime
        data object containing values over time and phase axes
    """

    # Check if input data object is compliant with dqh transformation
    _check_data(data_dqh)

    if "angle_elec" not in data_dqh.axes[0].normalizations:
        raise Exception("Time axis should contain angle_elec normalization")

    # Get values for one time period converted in electrical angle and for all phases
    angle_elec = data_dqh.axes[0].get_values(
        normalization="angle_elec", is_oneperiod=True
    )
    data_dqh_val = data_dqh.get_along("time[oneperiod]", "phase")[data_dqh.symbol]

    # Convert values to dqh frame
    data_n_val = dqh2n(data_dqh_val, angle_elec, n, is_n_rms, phase_dir)

    # Get time axis on one period
    per_t, is_aper_t = data_dqh.axes[0].get_periodicity()
    per_t = int(per_t / 2) if is_aper_t else per_t
    Time = data_dqh.axes[0].get_axis_periodic(per_t, is_aper=False)

    # Create DQH axis
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(n),
        is_components=True,
    )

    # Get normalizations
    normalizations = dict()
    if data_dqh.normalizations is not None and len(data_dqh.normalizations) > 0:
        for key, val in data_dqh.normalizations.items():
            normalizations[key] = val.copy()

    # Create DataTime object in dqh frame
    data_n = DataTime(
        name=data_dqh.name.replace(" in DQH frame", ""),
        unit=data_dqh.unit,
        symbol=data_dqh.symbol,
        values=data_n_val,
        axes=[Time, Phase],
        normalizations=normalizations,
        is_real=data_dqh.is_real,
    )

    return data_n


def dqh2n(Z_dqh, angle_elec, n, is_n_rms=False, phase_dir=None):
    """dqh to n phase coordinate transformation

    Parameters
    ----------
    Z_dqh : ndarray
        matrix (N x 3) of dqh phase values
    angle_elec : ndarray
        angle of the rotor coordinate system
    n: int
        number of phases
    is_n_rms : boolean
        True to return n currents in rms value, False to return peak values (Pyleecan convention)
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    Z_n : ndarray
        transformed matrix (N x n) of n phase values
    """

    Z_n = abc2n(dqh2abc(Z_dqh, angle_elec), n, phase_dir)

    if not is_n_rms:
        # Multiply by sqrt(2) to from (I_n_rms) to (I_n_peak)
        Z_n *= np.sqrt(2)

    return Z_n


def abc2n(Z_abc, n=3, phase_dir=None):
    """3 phase equivalent to n phase coordinate transformation, i.e. Clarke transformation

    Parameters
    ----------
    Z_abc : ndarray
        matrix (N x 3) of 3 phase equivalent values in alpha-beta-gamma frame
    n: int
        number of phases
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    Z_n : ndarray
        transformed matrix (N x n) of n phase values

    """

    # Inverse of Clarke transformation matrix
    ab_2_n = comp_Clarke_transform(n, is_inv=True, phase_dir=phase_dir)

    Z_n = np.matmul(Z_abc, ab_2_n)

    return Z_n


def dqh2abc(Z_dqh, angle_elec):
    """dqh to alpha-beta-gamma coordinate transformation

    Parameters
    ----------
    Z_dqh : ndarray
        matrix (N x 3) of dqh - reference frame values
    angle_elec : ndarray
        angle of the rotor coordinate system

    Returns
    -------
    Z_abc : ndarray
        transformed array

    """

    if Z_dqh.ndim == 1:
        Z_dqh = Z_dqh[None, :]

    sin_angle_elec = np.sin(angle_elec)
    cos_angle_elec = np.cos(angle_elec)

    Z_abc = np.zeros((angle_elec.size, 3))

    Z_abc[:, 0] = Z_dqh[:, 0] * cos_angle_elec - Z_dqh[:, 1] * sin_angle_elec
    Z_abc[:, 1] = Z_dqh[:, 0] * sin_angle_elec + Z_dqh[:, 1] * cos_angle_elec
    Z_abc[:, 2] = Z_dqh[:, 2]

    return Z_abc


def comp_Clarke_transform(n, is_inv=False, phase_dir=None):
    """Compute Clarke transformation for given number of phases and rotating direction of phases

    Parameters
    ----------
    n : int
        number of phases
    is_inv: bool
        False to return Clarke transform, True to return inverse of Clarke transform
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce


    Returns
    -------
    mat : ndarray
        Clarke transform matrix of size (n, 3)
    """

    if phase_dir not in [-1, 1]:
        raise Exception("Cannot enforce phase_dir other than +1 or -1")

    # Phasor depending on fundamental field rotation direction
    phasor = np.linspace(0, phase_dir * 2 * np.pi * (n - 1) / n, n)

    # Clarke transformation matrix
    if is_inv:
        mat = np.vstack((np.cos(phasor), -np.sin(phasor), np.ones(n)))
    else:
        mat = 2 / n * np.column_stack((np.cos(phasor), -np.sin(phasor), np.ones(n) / 2))

    return mat


def get_phase_dir_DataTime(data_n):
    """Get the phase rotating direction of input n-phase DataTime object

    Parameters
    ----------
    data_n : DataTime
        data object containing values over time and phase axes

    Returns
    -------
    phase_dir : int
        rotating direction of phases +/-1
    """

    # Check if input data object is compliant with dqh transformation
    _check_data(data_n)

    # Extract values from DataTime
    Z_n = data_n.get_along("time[oneperiod]", "phase")[data_n.symbol]

    # Get current_dir
    current_dir = int(np.sign(data_n.axes[0].normalizations["angle_elec"].ref))

    # Get phase direction
    phase_dir = get_phase_dir(Z_n, current_dir)

    return phase_dir


def get_phase_dir(Z_n, current_dir):
    """Get the phase rotating direction of input n-phase quantity by looking at phase of maximum component

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phase values
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce

    Returns
    ----------
    phase_dir : int
        rotating direction of phases +/-1
    """

    # Get number of time steps and phase
    N, n = Z_n.shape

    # Get Fourier transform for all phases
    TF_Zn = np.fft.fft(Z_n, axis=0)[: int(N / 2), :]

    # Get index of maximum component
    Imax = np.argmax(np.linalg.norm(TF_Zn, axis=-1))

    # Get phase angle for all phases
    angle_Zn_max = np.unwrap(np.angle(TF_Zn[Imax, :]) - np.angle(TF_Zn[Imax, 0]))

    # Differentiate phase angle between phases and taking sign
    phase_shift_sign = np.unique(np.sign(np.diff(angle_Zn_max)))

    if phase_shift_sign.size == 1:
        # phase_dir / current_dir has the sign of phase shift angle
        phase_dir = current_dir * int(phase_shift_sign[0])
    else:
        raise Exception("Cannot calculate phase_dir, please put phase_dir as input")

    return phase_dir


def _check_data(data, is_freq=False):
    """Check if input Data object is compliant with dqh transformation

    Parameters
    ----------
    data : Data
        data object to check

    """

    if not isinstance(data, (DataTime, DataFreq, DataDual, DataND)):
        raise Exception(
            "Input object should be a DataTime, DataFreq or DataDual object"
        )

    elif isinstance(data, DataTime):
        _check_DataTime(data)

    elif isinstance(data, DataFreq):
        _check_DataFreq(data)

    elif isinstance(data, DataDual):
        if is_freq:
            data.axes = data.axes_df
            data.values = data.values_df
            _check_DataFreq(data)

        else:
            data.axes = data.axes_dt
            data.values = data.values_dt
            _check_DataTime(data)

    elif isinstance(data, DataND):
        try:
            _check_DataTime(data)
        except Exception:
            _check_DataFreq(data)


def _check_DataTime(data):
    """Check if input DataTime object is compliant with dqh transformation

    Parameters
    ----------
    data : DataTime
        DataTimes object to check

    """
    if len(data.axes) != 2:
        raise Exception("DataTime object should contain two axes: time and phase")
    if data.axes[0].name != "time":
        raise Exception("DataTime object should contain time as first axis")
    if data.axes[1].name != "phase":
        raise Exception("DataTime object should contain phase as second axis")


def _check_DataFreq(data):
    """Check if input DataFreq object is compliant with dqh transformation

    Parameters
    ----------
    data : DataFreq
        DataFreq object to check

    """
    if len(data.axes) != 2:
        raise Exception("DataFreq object should contain two axes: freqs and phase")
    if data.axes[0].name != "freqs":
        raise Exception("DataFreq object should contain freqs as first axis")
    if data.axes[1].name != "phase":
        raise Exception("DataFreq object should contain phase as second axis")
