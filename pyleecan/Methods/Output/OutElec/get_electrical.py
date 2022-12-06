from numpy import zeros, abs as np_abs, argmin, array

from SciDataTool import DataTime, DataFreq, Data1D

from ....Functions.Electrical.dqh_transformation import dqh2n_DataTime, n2dqh_DataTime
from ....Functions.Electrical.dqh_transformation_freq import (
    n2dqh_DataFreq,
    dqh2n_DataFreq,
)


def get_electrical(
    self,
    data_dict,
    Time=None,
    is_dqh=False,
    is_fund_only=False,
    is_harm_only=False,
    is_freq=None,
):
    """Generic getter to return voltage/current as DataND object

    Parameters
    ----------
    self : OutElec
        an OutElec object
    data_dict: str
        Requested quantity ('U_s': stator voltage, 'I_s': stator current)
    Time : Data
        Time axis
    is_dqh : bool
        True to rotate in DQH frame
    is_fund_only : bool
        True to return only fundamental component
    is_harm_only : bool
        True to return only components at higher frequencies than fundamental component
    is_freq: bool
        True to calculate dqh transformation in frequency domain

    Returns
    -------
    obj: DataND
        Requested quantity
    """

    if is_fund_only and is_harm_only:
        raise Exception("is_fund_only and is_harm_only cannot be both True")

    # Get object from OutElec
    quantity = data_dict["symbol"].replace("_", "")
    obj = getattr(self, quantity)

    # Get requested quantity in data_dict
    if obj is None:

        if Time is None:
            Time = self.axes_dict["time"]

        lamination = self.parent.simu.machine.get_lam_by_label(data_dict["lam_label"])

        # Recalculate quantity
        qs = lamination.winding.qs
        phase_label = "phase_" + data_dict["lam_label"]
        Phase = self.axes_dict[phase_label].copy()
        if is_freq:
            N = 1
            Freqs = Data1D(
                name="freqs",
                symbol="",
                unit="Hz",
                normalizations=Time.normalizations.copy(),
                is_components=Time.is_components,
                values=array([0]),
            )
            axes_list = [Freqs, Phase]
            DataClass = DataFreq
        else:
            N = Time.get_length(is_smallestperiod=True)
            Time_bis = Time.copy()
            is_aper = False
            if "antiperiod" in Time_bis.symmetries:
                is_aper = True
                Time_bis.symmetries["period"] = Time_bis.symmetries.pop("antiperiod")
            axes_list = [Time_bis, Phase]
            DataClass = DataTime

        # Generate quantity according to Ad/Aq, Ah=0
        if (
            data_dict["Ad"] is not None
            and data_dict["Aq"] is not None
            and (data_dict["Ad"] != 0 or data_dict["Aq"] != 0)
        ):
            # Generate constant dqh values along time
            A_val = zeros((N, 3))
            A_val[:, 0] = data_dict["Ad"]
            A_val[:, 1] = data_dict["Aq"]
        else:
            # Enforce zero values in quantity
            A_val = zeros((N, qs))

        A_dqh = DataClass(
            name=data_dict["name"],
            unit=data_dict["unit"],
            symbol=data_dict["symbol"],
            axes=axes_list,
            values=A_val,
        )

        # Check requested referential
        if is_dqh:
            obj = A_dqh
        elif is_freq:
            obj = dqh2n_DataFreq(
                A_dqh,
                n=qs,
                current_dir=self.current_dir,
                felec=self.OP.felec,
                is_n_rms=False,
                phase_dir=self.phase_dir,
            )
        else:
            obj = dqh2n_DataTime(A_dqh, n=qs, is_n_rms=False, phase_dir=self.phase_dir)
            if is_aper:
                obj.axes[0].symmetries["antiperiod"] = obj.axes[0].symmetries.pop(
                    "period"
                )

    else:

        if Time is not None:
            # Interpolate values on Time vector
            obj = obj.get_data_along(
                "time=axis_data", "phase", axis_data={"time": Time.get_values()}
            )

        if is_dqh:
            # Convert to DQH frame
            if is_freq:
                obj = n2dqh_DataFreq(
                    obj,
                    is_dqh_rms=True,
                    phase_dir=self.phase_dir,
                    current_dir=self.current_dir,
                    felec=self.OP.get_felec(),
                )
            else:
                obj = n2dqh_DataTime(obj, is_dqh_rms=True, phase_dir=self.phase_dir)

    if is_fund_only or is_harm_only:

        if Time is None and not is_dqh:
            # Copy object to leave original object unchanged
            obj = obj.copy()

        # Fundamental is at felec in ABC frame, 0Hz in dqh frame
        felec = (1 - int(is_dqh)) * self.OP.get_felec()
        # Get data object with quantity harmonics higher than fundamental component
        obj = obj.get_data_along("freqs", "phase")
        # Get index of fundamental frequency
        Freqs = obj.axes[0]
        freqs = Freqs.get_values()
        ifund = argmin(np_abs(freqs - felec))

        if is_fund_only:
            # Keep only fundamental frequency
            Freqs_fund = Data1D(
                name=Freqs.name,
                symbol=Freqs.symbol,
                unit=Freqs.unit,
                normalizations=Freqs.normalizations,
                is_components=Freqs.is_components,
                values=array([freqs[ifund]]),
            )
            obj.axes[0] = Freqs_fund
            obj.values = obj.values[ifund, ...]

        elif is_harm_only:
            # Find all indices
            iharm = [ii for ii in range(freqs.size) if ii != ifund]
            # Remove fundamental frequency component
            Freqs_harm = Data1D(
                name=Freqs.name,
                symbol=Freqs.symbol,
                unit=Freqs.unit,
                normalizations=Freqs.normalizations,
                is_components=Freqs.is_components,
                values=freqs[iharm],
            )
            obj.axes[0] = Freqs_harm
            obj.values = obj.values[iharm, ...]

    return obj
