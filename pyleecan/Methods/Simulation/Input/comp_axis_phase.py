from SciDataTool import Data1D


def comp_axis_phase(self, lamination, per_a=None, Phase_in=None):
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

        if len(name_phase) > 0:

            # Creating the data object
            Phase = Data1D(
                name="phase",
                unit="",
                values=name_phase,
                is_components=True,
            )

    return Phase
