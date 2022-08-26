from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_indices


def comp_axis_phase(self, lamination, per_a=None, is_apera=None, Phase_in=None):
    """Compute phase axes for given lamination

    Parameters
    ----------
    self : Input
        an Input object
    lamination: Lamination
        a Lamination object
    per_a : int
        time periodicity
    Phase_in: Data
        Input phase axis

    Returns
    -------
    Phase: Data
        Requested phase axis
    """

    Phase = None

    if Phase_in is not None:
        Phase = Phase_in.copy()

    else:
        name_phase = lamination.get_name_phase()

        if len(name_phase) > 1:

            if per_a is not None and is_apera is not None:
                sym_dict = dict()
                if is_apera:
                    per_a *= 2
                    sym_dict["antiperiod"] = per_a
                elif per_a > 1:
                    sym_dict["period"] = per_a

                # Creating the data object
                Phase = DataLinspace(
                    name="phase",
                    unit="rad",
                    initial=0,
                    final=2 * pi / per_a,
                    number=int(len(name_phase) / per_a),
                    include_endpoint=False,
                    symmetries=sym_dict,
                    normalizations={"bar_id": Norm_indices()},
                    is_overlay=True,
                    # filter={"Phase": []},
                )
            else:
                # Creating the data object
                Phase = Data1D(
                    name="phase",
                    unit="rad",
                    values=name_phase,
                    is_components=True,
                    is_overlay=True,
                    filter={"Phase": []},
                )
        elif len(name_phase) == 1:
            # Creating the data object
            Phase = DataLinspace(
                name="phase",
                unit="rad",
                initial=0,
                final=2 * pi,
                number=1,
                include_endpoint=False,
                normalizations={"bar_id": Norm_indices()},
                is_overlay=True,
                # filter={"Phase": []},
            )

    return Phase
