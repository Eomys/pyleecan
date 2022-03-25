import numpy as np

from SciDataTool import Data1D, DataFreq
from SciDataTool.Functions.set_routines import union1d_tol

from ...Functions.Electrical.dqh_transformation import (
    _check_data,
    n2abc,
    abc2n,
)
from ...Functions.Winding.gen_phase_list import gen_name


def n2dqh_DataFreq(data_n, current_dir, felec, is_dqh_rms=True, phase_dir=None):
    """n phases to dqh equivalent coordinate transformation of DataFreq/DataTime object

    Parameters
    ----------
    data_n : DataFreq/DataTime
        data object containing values over freqs and phase axes
    is_dqh_rms : boolean
        True to return dq currents in rms value (Pyleecan convention), False to return peak values
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]

    Returns
    -------
    data_dqh : DataFreq
        data object transformed in dqh frame

    """

    if phase_dir is None:
        # Check if input data object is compliant with dqh transformation
        # and get phase_dir from data object
        phase_dir = get_phase_dir_DataFreq(data_n)
    else:
        # Only check if input data object is compliant with dqh transformation
        _check_data(data_n, is_freq=True)

    # Get values for one time period converted in electrical angle and for all phases
    result_n = data_n.get_along("freqs", "phase", is_squeeze=False)

    # Convert values to dqh frame
    Z_dqh, freqs_dqh = n2dqh(
        Z_n=result_n[data_n.symbol],
        freqs=result_n["freqs"],
        phase_dir=phase_dir,
        current_dir=current_dir,
        felec=felec,
        is_dqh_rms=is_dqh_rms,
    )

    # Create frequency axis
    norm_freq = dict()
    ax_freq = data_n.axes[0]
    if ax_freq.normalizations is not None and len(ax_freq.normalizations) > 0:
        for key, val in ax_freq.normalizations.items():
            norm_freq[key] = val.copy()
    Freqs = Data1D(name="freqs", unit="Hz", values=freqs_dqh, normalizations=norm_freq)

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

    # Create DataFreq object in dqh frame
    data_dqh = DataFreq(
        name=data_n.name + " in DQH frame",
        unit=data_n.unit,
        symbol=data_n.symbol,
        values=Z_dqh,
        axes=[Freqs, axis_dq],
        normalizations=normalizations,
        is_real=data_n.is_real,
    )

    return data_dqh


def n2dqh(Z_n, freqs, phase_dir, current_dir, felec, is_dqh_rms=True):
    """n phases to dqh equivalent coordinate transformation

    Parameters
    ----------
    Z_n : ndarray
        matrix (N x n) of n phases values
    freqs : ndarray
        frequency array in static frame [Hz]
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]
    is_dqh_rms : boolean
        True to return dq currents in rms value (Pyleecan convention), False to return peak values

    Returns
    -------
    Z_dqh : ndarray
        transformed matrix (N x 3) of dqh equivalent values
    freqs_dqh : ndarray
        frequency array in dqh frame [Hz]
    """

    Z_dqh, freqs_dqh = abc2dqh(n2abc(Z_n, phase_dir), freqs, current_dir, felec)

    if is_dqh_rms:
        # Divide by sqrt(2) to go from (Id_peak, Iq_peak) to (Id_rms, Iq_rms)
        Z_dqh /= np.sqrt(2)

    return Z_dqh, freqs_dqh


def abc2dqh(Z_abc, freqs, current_dir, felec):
    """alpha-beta-gamma to dqh coordinate transformation

    Parameters
    ----------
    Z_abc : ndarray
        matrix (N x 3) of phases values in abc static frame
    freqs : ndarray
        frequency array in static frame [Hz]
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]

    Returns
    -------
    Z_dqh : ndarray
        transformed matrix (N x 3) of dqh equivalent values
    freqs_dqh : ndarray
        frequency array in dqh frame [Hz]
    """

    # Create Frequency axes
    Freqs = Data1D(name="freqs", unit="Hz", values=freqs)
    Freqs0 = Data1D(name="freqs", unit="Hz", values=np.array([felec]))

    # Build DataFreq for Za and Zb
    df_a = DataFreq(axes=[Freqs], values=Z_abc[:, 0])
    df_b = DataFreq(axes=[Freqs], values=Z_abc[:, 1])

    # Build DataFreq for cos(angle_elec) / sin(angle_elec)
    df_cos = DataFreq(axes=[Freqs0], values=np.array([1]))
    df_sin = DataFreq(axes=[Freqs0], values=np.array([-current_dir * 1j]))
    df_sin_neg = DataFreq(axes=[Freqs0], values=np.array([current_dir * 1j]))

    # Calculate Zd in spectrum domain (Zd = Za*cos + Zb*sin)
    df_d = df_a.conv(df_cos)
    df_d = df_d.sum(df_b.conv(df_sin))

    # Calculate Zq in spectrum domain (Zq = -Za*sin + Zb*cos)
    df_q = df_a.conv(df_sin_neg)
    df_q = df_q.sum(df_b.conv(df_cos))

    # Merge frequencies
    freqs_dqh, Ifdq, Ifh = union1d_tol(df_d.axes[0].values, freqs, return_indices=True)

    # Rebuild dqh values
    Z_dqh = np.zeros((freqs_dqh.size, 3), dtype=complex)
    Z_dqh[Ifdq, 0] = df_d.values
    Z_dqh[Ifdq, 1] = df_q.values
    Z_dqh[Ifh, 2] = Z_abc[:, 2]  # Homopolar axis same as c axis

    # Only return non zero values
    Z_dqh_norm = np.linalg.norm(Z_dqh, axis=1)
    I0 = Z_dqh_norm > 1e-10

    return Z_dqh[I0, :], freqs_dqh[I0]


def dqh2n_DataFreq(data_dqh, n, current_dir, felec, is_n_rms=False, phase_dir=None):
    """dqh to n phase coordinate transformation of DataFreq object

    Parameters
    ----------
    data_dqh : DataFreq
        data object containing values over time in dqh frame
    n: int
        number of phases
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]
    is_n_rms : boolean
        True to return n currents in rms value, False to return peak values (Pyleecan convention)
    phase_dir: int
        direction of phase distribution: +/-1 (-1 clockwise) to enforce

    Returns
    -------
    data_n : DataFreq
        data object containing values over time and phase axes
    """

    # Check if input data object is compliant with dqh transformation
    _check_data(data_dqh, is_freq=True)

    # Get values for one time period converted in electrical angle and for all phases
    result_dqh = data_dqh.get_along("freqs", "phase", is_squeeze=False)

    # Convert values to dqh frame
    Z_abc, freqs_abc = dqh2n(
        Z_dqh=result_dqh[data_dqh.symbol],
        freqs=result_dqh["freqs"],
        phase_dir=phase_dir,
        current_dir=current_dir,
        felec=felec,
        n=n,
        is_n_rms=is_n_rms,
    )

    # Create frequency axis
    norm_freq = dict()
    ax_freq = data_dqh.axes[0]
    if ax_freq.normalizations is not None and len(ax_freq.normalizations) > 0:
        for key, val in ax_freq.normalizations.items():
            norm_freq[key] = val.copy()
    Freqs = Data1D(name="freqs", unit="Hz", values=freqs_abc, normalizations=norm_freq)

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

    # Create DataFreq object in dqh frame
    data_n = DataFreq(
        name=data_dqh.name.replace(" in DQH frame", ""),
        unit=data_dqh.unit,
        symbol=data_dqh.symbol,
        values=Z_abc,
        axes=[Freqs, Phase],
        normalizations=normalizations,
        is_real=data_dqh.is_real,
    )

    return data_n


def dqh2n(Z_dqh, freqs, current_dir, felec, n, phase_dir=None, is_n_rms=False):
    """dqh to n phase coordinate transformation

    Parameters
    ----------
    Z_dqh : ndarray
        matrix (N x 3) of dqh phase values
    freqs : ndarray
        frequency array in dqh frame [Hz]
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]
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
    freqs_abc : ndarray
        frequency array in static frame [Hz]
    """

    Z_abc, freqs_abc = dqh2abc(Z_dqh, freqs, current_dir, felec)

    Z_n = abc2n(Z_abc, n, phase_dir)

    if not is_n_rms:
        # Multiply by sqrt(2) to from (I_n_rms) to (I_n_peak)
        Z_n *= np.sqrt(2)

    return Z_n, freqs_abc


def dqh2abc(Z_dqh, freqs, current_dir, felec):
    """dqh to alpha-beta-gamma coordinate transformation

    Parameters
    ----------
    Z_dqh : ndarray
        matrix (N x 3) of dqh - reference frame values
    freqs : ndarray
        frequency array in dqh frame [Hz]
    current_dir: int
        direction of current waveform: +/-1 (-1 clockwise) to enforce
    felec: float
        fundamental electrical frequency [Hz]

    Returns
    -------
    Z_abc : ndarray
        transformed array
    freqs_abc : ndarray
        frequency array in static frame [Hz]
    """

    # Create Frequency axes
    Freqs = Data1D(name="freqs", unit="Hz", values=freqs)
    Freqs0 = Data1D(name="freqs", unit="Hz", values=np.array([felec]))

    # Build DataFreq for Zd and Zq
    df_d = DataFreq(axes=[Freqs], values=Z_dqh[:, 0])
    df_q = DataFreq(axes=[Freqs], values=Z_dqh[:, 1])

    # Build DataFreq for cos(angle_elec) / sin(angle_elec)
    df_cos = DataFreq(axes=[Freqs0], values=np.array([1]))
    df_sin = DataFreq(axes=[Freqs0], values=np.array([-current_dir * 1j]))
    df_sin_neg = DataFreq(axes=[Freqs0], values=np.array([current_dir * 1j]))

    # Calculate Za with convolution (Za = Zd*cos - Zq*sin)
    df_a = df_d.conv(df_cos)
    df_a = df_a.sum(df_q.conv(df_sin_neg))

    # Calculate Zb with convolution (Zb = Zd*sin + Zq*cos)
    df_b = df_d.conv(df_sin)
    df_b = df_b.sum(df_q.conv(df_cos))

    # Merge frequencies
    freqs_abc, Ifab, Ifc = union1d_tol(
        df_a.axes[0].values, freqs, return_indices=True, tol=1e-4, is_abs_tol=False
    )

    # Rebuild abc values
    Z_abc = np.zeros((freqs_abc.size, 3), dtype=complex)
    Z_abc[Ifab, 0] = df_a.values
    Z_abc[Ifab, 1] = df_b.values
    Z_abc[Ifc, 2] = Z_dqh[:, 2]  # c axis same as homopolar axis

    # Only return non zero values
    Z_abc_norm = np.linalg.norm(Z_abc, axis=1)
    I0 = Z_abc_norm > 1e-10

    return Z_abc[I0, :], freqs_abc[I0]


def get_phase_dir_DataFreq(data_n):
    """Get the phase rotating direction of input n-phase DataFreq object

    Parameters
    ----------
    data_n : DataFreq
        data object containing values over time and phase axes

    Returns
    -------
    phase_dir : int
        rotating direction of phases +/-1
    """

    # Check if input data object is compliant with dqh transformation
    _check_data(data_n, is_freq=True)

    # Extract values from DataFreq
    Z_n = data_n.get_along("freqs", "phase", is_squeeze=False)[data_n.symbol]

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

    # Get index of maximum component
    Imax = np.argmax(np.linalg.norm(Z_n, axis=-1))

    # Get phase angle for all phases
    angle_Zn_max = np.unwrap(np.angle(Z_n[Imax, :]) - np.angle(Z_n[Imax, 0]))

    # Differentiate phase angle between phases and taking sign
    phase_shift_sign = np.unique(np.sign(np.diff(angle_Zn_max)))

    if phase_shift_sign.size == 1 and int(phase_shift_sign[0]) in [-1, 1]:
        # phase_dir / current_dir has the sign of phase shift angle
        phase_dir = current_dir * int(phase_shift_sign[0])
    else:
        raise Exception("Cannot calculate phase_dir, please put phase_dir as input")

    return phase_dir
