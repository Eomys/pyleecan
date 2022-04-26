from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pyplot import subplots
from matplotlib.patches import Polygon


def plot_anim_rotor(self, Nframe, Tanim, Nrot=1, is_loop=True):
    """Plot the machine with an animation of the rotor
    (Internal Rotor for now ?)

    Parameters
    ----------
    self : Machine
        Machine object
    Nframe: int
        Number of frame for the animation
    Tanim : float
        Duration of the animation [ms]
    Nrot : float
        Number of rotation
    is_loop : bool
        True to activate the loop animation
    """

    # Display
    fig, axes = subplots()
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Machine")

    # Axis Setup
    axes.axis("equal")

    # The Lamination is centered in the figure
    Lim = (self.stator.Rext) * 1.5  # Axes limit for plot
    Rsurf = self.rotor.build_geometry(sym=1, alpha=0, delta=0)

    # Rotation angle between each frame
    Dalpha = 2 * pi * Nrot / Nframe

    def init():
        """Create the patches for the first image"""
        Spatches = self.stator.plot(is_display=False)
        Rpatches = self.rotor.plot(is_display=False)
        for patch in Spatches:
            axes.add_patch(patch)
        for patch in Rpatches:
            axes.add_patch(patch)
        return []

    def update_rotor(ii):
        """Rotate and update the rotor patches"""
        for ii in range(len(Rsurf)):
            Rsurf[ii].rotate(Dalpha)
            patches = Rsurf[ii].get_patches()
            for patch in patches:
                if type(patch) is Polygon:
                    axes.patches[-len(Rsurf) + ii].xy = patch.xy
            # elif type(patch) is Circle:
            #     pass

        axes.set_xlim(-Lim, Lim)
        axes.set_ylim(-Lim, Lim)
        return []

    # Animation definition
    anim = animation.FuncAnimation(
        fig,
        update_rotor,
        init_func=init,
        frames=Nframe,
        interval=Tanim / Nframe,
        blit=True,
        repeat=is_loop,
    )
    plt.show()
