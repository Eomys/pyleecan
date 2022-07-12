from numpy import exp, pi
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from ....definitions import config_dict
from ....Functions.init_fig import init_fig
from ....Functions.labels import decode_label, HOLEM_LAB, LAM_LAB


def _plot_arrow_mag(
    self,
    ax=None,
    sym=1,
    alpha=0,
    delta=0,
):
    """Plot the magnetization direction as arrow on top of the lamination
    (meant to be called by LamHole.plot)

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the arrow
    sym : int
        Symmetry factor (1= plot full machine, 2= half of the machine...)
    alpha : float
        angle for rotation (Default value = 0) [rad]
    delta : complex
        complex for translation (Default value = 0)
    """

    for hole in self.hole_north:
        H = hole.comp_height()
        mag_dict = hole.comp_magnetization_dict()
        for magnet_name, mag_dir in mag_dict.items():
            # Get the correct surface
            mag_surf = None
            mag_id = int(magnet_name.split("_")[-1])
            mag = hole.get_magnet_by_id(mag_id)
            if mag is not None:
                for surf in hole.build_geometry():
                    label_dict = decode_label(surf.label)
                    if (
                        HOLEM_LAB in label_dict["surf_type"]
                        and label_dict["T_id"] == mag_id
                    ):
                        mag_surf = surf
                        break
                # Create arrow coordinates
                Zh = hole.Zh
                for ii in range(int(Zh / sym / 2)):
                    off = 0  # All north
                    if mag is not None and mag.type_magnetization == 3:
                        off -= pi / 2
                    Z1 = (mag_surf.point_ref + delta) * exp(
                        1j * (ii * 4 * pi / Zh + pi / Zh + alpha)
                    )
                    Z2 = (
                        mag_surf.point_ref + delta + H / 5 * exp(1j * (mag_dir + off))
                    ) * exp(1j * (ii * 4 * pi / Zh + pi / Zh + alpha))
                    ax.annotate(
                        text="",
                        xy=(Z2.real, Z2.imag),
                        xytext=(Z1.real, Z1.imag),
                        arrowprops=dict(arrowstyle="->", linewidth=1, color="b"),
                    )

    for hole in self.hole_south:
        H = hole.comp_height()
        mag_dict = hole.comp_magnetization_dict()
        for magnet_name, mag_dir in mag_dict.items():
            # Get the correct surface
            mag_surf = None
            mag_id = int(magnet_name.split("_")[-1])
            mag = hole.get_magnet_by_id(mag_id)
            if mag is not None:
                for surf in hole.build_geometry():
                    label_dict = decode_label(surf.label)
                    if (
                        HOLEM_LAB in label_dict["surf_type"]
                        and label_dict["T_id"] == mag_id
                    ):
                        mag_surf = surf
                        break
                # Create arrow coordinates
                Zh = hole.Zh
                for ii in range(int(Zh / sym / 2)):
                    off = pi  # All north
                    if mag is not None and mag.type_magnetization == 3:
                        off -= pi / 2
                    Z1 = (mag_surf.point_ref + delta) * exp(
                        1j * (ii * 4 * pi / Zh + 3 * pi / Zh + alpha)
                    )
                    Z2 = (
                        mag_surf.point_ref + delta + H / 5 * exp(1j * (mag_dir + off))
                    ) * exp(1j * (ii * 4 * pi / Zh + 3 * pi / Zh + alpha))
                    ax.annotate(
                        text="",
                        xy=(Z2.real, Z2.imag),
                        xytext=(Z1.real, Z1.imag),
                        arrowprops=dict(arrowstyle="->", linewidth=1, color="b"),
                    )
