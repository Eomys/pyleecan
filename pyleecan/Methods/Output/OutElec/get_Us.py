from numpy import array

from SciDataTool import DataTime

from ....Functions.Electrical.coordinate_transformation import dqh2n


def get_Us(self):
    """Return the fundamental stator voltage as DataND object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    Returns
    -------
    Us: DataND
        fundamental stator voltage
    """
    if self.Us is None:
        # Generate current according to Ud/Uq
        Usdqh = array([self.OP.get_Ud_Uq()["Ud"], self.OP.get_Ud_Uq()["Uq"], 0])

        Time = self.axes_dict["time"]

        angle_elec = Time.get_values(is_smallestperiod=True, normalization="angle_elec")
        qs = self.parent.simu.machine.stator.winding.qs
        stator_label = "phase_" + self.parent.simu.machine.stator.get_label()

        # Switch from dqh to abc referential
        Us = dqh2n(Usdqh, angle_elec, n=qs)

        self.Us = DataTime(
            name="Stator voltage",
            unit="V",
            symbol="Us",
            axes=[Time.copy(), self.axes_dict[stator_label].copy()],
            values=Us,
        )
    return self.Us
