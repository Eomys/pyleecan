import numpy as np

from SciDataTool import Data1D, DataTime

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
    # Check if input data object is compliant with dqh transformation
    check_DataTime(data_n)

    if "angle_elec" not in data_n.axes[0].normalizations:
        raise Exception("Time axis should contain angle_elec normalization")

    # Get values for one time period converted in electrical angle and for all phases
    result = data_n.get_along("time[oneperiod]->angle_elec", "phase")
    data_n_val = result[data_n.symbol]
    angle_elec = result["time"]

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
    if data_n.normalizations is None or len(data_n.normalizations) == 0:
        normalizations = dict()
    else:
        normalizations = data_n.normalizations.copy()

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
    check_DataTime(data_dqh)

    if "angle_elec" not in data_dqh.axes[0].normalizations:
        raise Exception("Time axis should contain angle_elec normalization")

    # Get values for one time period converted in electrical angle and for all phases
    result = data_dqh.get_along("time[oneperiod]->angle_elec", "phase")
    data_dqh_val = result[data_dqh.symbol]
    angle_elec = result["time"]

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
    if data_dqh.normalizations is None or len(data_dqh.normalizations) == 0:
        normalizations = dict()
    else:
        normalizations = data_dqh.normalizations.copy()

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

    Z_dqh = abc2dqh(n2abc(Z_n, phase_dir), angle_elec)

    if is_dqh_rms:
        # Divide by sqrt(2) to go from (Id_peak, Iq_peak) to (Id_rms, Iq_rms)
        Z_dqh = Z_dqh / np.sqrt(2)

    return Z_dqh


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
        Z_n = Z_n * np.sqrt(2)

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
    check_DataTime(data_n)

    # Extract values from DataTime
    Z_n = data_n.get_along("time[oneperiod]", "phase")[data_n.symbol]

    # Get phase direction
    phase_dir = get_phase_dir(Z_n)

    return phase_dir


def get_phase_dir(Z_n):
    """Get the phase rotating direction of input n-phase quantity

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phase values

    Returns
    ----------
    phase_dir : int
        rotating direction of phases +/-1
    """

    # Get number of time steps and phase
    N, n = Z_n.shape

    # Shift first phase of +/- Nt/qs
    Z_n_p = np.roll(Z_n[:, 0], shift=int(N / n))
    Z_n_n = np.roll(Z_n[:, 0], shift=-int(N / n))

    # Find which shifted phase is closer to second phase
    is_trigo = np.sum(np.abs(Z_n_p - Z_n[:, 1])) > np.sum(np.abs(Z_n_n - Z_n[:, 1]))

    # phase_dir=+/-1
    phase_dir = int((-1) ** int(is_trigo))

    return phase_dir


def check_DataTime(data):
    """Check if input data object is compliant with dqh transformation

    Parameters
    ----------
    data : Data
        data object to check

    """

    if not isinstance(data, DataTime):
        raise Exception("Input object should be a DataTime object")
    if len(data.axes) != 2:
        raise Exception("DataTime object should contain two axes: time and phase")
    if data.axes[0].name != "time":
        raise Exception("DataTime object should contain time as first axis")
    if data.axes[1].name != "phase":
        raise Exception("DataTime object should contain phase as second axis")