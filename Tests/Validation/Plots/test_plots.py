from numpy import squeeze, linspace, sin
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
import unittest
from Tests import save_validation_path as save_path
import pytest

from pyleecan.Classes.Simu1 import Simu1
from Tests.Validation.Machine.SCIM_006 import SCIM_006

from pyleecan.Classes.Output import Output
from SciDataTool import DataTime, Data1D, DataLinspace, DataFreq
from Tests import DATA_DIR
from pyleecan.Classes.ImportMatlab import ImportMatlab

simu = Simu1(name="EM_SCIM_NL_006", machine=SCIM_006)

mat_file_Br = join(DATA_DIR, "Plots/default_proj_Br.mat")
mat_file_time = join(DATA_DIR, "Plots/default_proj_time.mat")
mat_file_angle = join(DATA_DIR, "Plots/default_proj_angle.mat")
mat_file_MTr_freqs = join(DATA_DIR, "Plots/default_proj_MTr_freqs.mat")
mat_file_MTr_wavenumber = join(DATA_DIR, "Plots/default_proj_MTr_wavenumber.mat")
mat_file_MTr = join(DATA_DIR, "Plots/default_proj_MTr.mat")
mat_file_Br_cfft2 = join(DATA_DIR, "Plots/default_proj_Br_cfft2.mat")
mat_file_Brfreqs = join(DATA_DIR, "Plots/default_proj_Brfreqs.mat")
mat_file_Brwavenumber = join(DATA_DIR, "Plots/default_proj_Brwavenumber.mat")

# Read input files from Manatee
Br = squeeze(ImportMatlab(file_path=mat_file_Br, var_name="XBr").get_data())
time = squeeze(ImportMatlab(file_path=mat_file_time, var_name="timec").get_data())
angle = squeeze(
    ImportMatlab(file_path=mat_file_angle, var_name="alpha_radc").get_data()
)
MTr_freqs = squeeze(
    ImportMatlab(file_path=mat_file_MTr_freqs, var_name="freqs").get_data()
)
MTr_wavenumber = squeeze(
    ImportMatlab(file_path=mat_file_MTr_wavenumber, var_name="orders_circ").get_data()
)
MTr = squeeze(ImportMatlab(file_path=mat_file_MTr, var_name="XPwr").get_data())
Br_cfft2 = squeeze(ImportMatlab(file_path=mat_file_Br_cfft2, var_name="Fwr").get_data())
freqs_Br = squeeze(
    ImportMatlab(file_path=mat_file_Brfreqs, var_name="freqs").get_data()
)
wavenumber = squeeze(
    ImportMatlab(file_path=mat_file_Brwavenumber, var_name="orders").get_data()
)

# Plot parameters
freq_max = 13000
r_max = 78


@pytest.mark.validation
class tests_plots(TestCase):
    # @unittest.skip
    def test_default_proj_Br_time_space(self):

        out = Output(simu=simu)
        out.post.legend_name = "Reference"

        # Build the data objects
        Time = Data1D(name="time", unit="s", symmetries={}, values=time)
        Angle = Data1D(name="angle", unit="rad", symmetries={}, values=angle)
        out.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time, Angle],
            normalizations={"space_order": 3},
            values=Br,
        )

        out2 = Output(simu=simu)
        out2.post.legend_name = "Periodicity 3"
        out2.post.line_color = "r--"

        # Reduce to 1/3 period
        Br_reduced = Br[0:672, 0:672]
        time_reduced = time[0:672]
        angle_reduced = angle[0:672]

        # Build the data objects
        Time = Data1D(
            name="time",
            unit="s",
            symmetries={"time": {"period": 3}},
            values=time_reduced,
        )
        Angle = Data1D(
            name="angle",
            unit="rad",
            symmetries={"angle": {"period": 3}},
            values=angle_reduced,
        )
        out2.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={"time": {"period": 3}, "angle": {"period": 3}},
            axes=[Time, Angle],
            normalizations={},
            values=Br_reduced,
        )

        out3 = Output(simu=simu)
        out3.post.legend_name = "Linspace"
        out3.post.line_color = "r--"

        # Get linspace data
        t0 = time[0]
        tf = time[-1]
        deltat = time[1] - time[0]
        a0 = angle[0]
        deltaa = angle[1] - angle[0]
        Na = len(angle)

        # Build the data objects
        Time = DataLinspace(
            name="time",
            unit="s",
            symmetries={},
            initial=t0,
            final=tf,
            step=deltat,
            include_endpoint=True,
        )
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            symmetries={},
            initial=a0,
            step=deltaa,
            number=Na,
            include_endpoint=False,
        )
        out3.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time, Angle],
            normalizations={"space_order": 3},
            values=Br,
        )

        out4 = Output(simu=simu)
        out4.post.legend_name = "Inverse FT"
        out4.post.line_color = "r--"

        # Build the data objects
        Freqs = Data1D(name="freqs", unit="Hz", symmetries={}, values=freqs_Br,)
        Wavenumber = Data1D(
            name="wavenumber", unit="", symmetries={}, values=wavenumber,
        )
        out4.mag.Br = DataFreq(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Freqs, Wavenumber],
            normalizations={},
            values=Br_cfft2,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_time("mag.Br", is_fft=True, freq_max=freq_max, out_list=[out2])

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_dataobj_period.png"))

        # Plot the result by comparing the two simulation (Data1D / DataLinspace)
        plt.close("all")
        out.plot_A_space(
            "mag.Br", is_fft=True, is_spaceorder=True, r_max=r_max, out_list=[out3]
        )

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_dataobj_linspace.png"))

        # Plot the result by comparing the two simulation (Data1D / DataLinspace)
        plt.close("all")
        out.plot_A_space("mag.Br", is_fft=True, r_max=r_max, out_list=[out4])

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_dataobj_ift.png"))

    # @unittest.skip
    def test_default_proj_Br_cfft2(self):

        r_max = 78
        freq_max = 2500
        mag_max = 0.6
        N_stem = 100

        out = Output(simu=simu)

        # Build the data objects
        Time = Data1D(name="time", unit="s", symmetries={}, values=time)
        #        Angle = Data1D(name="angle", unit="rad", symmetries={"angle": {"period": 2}}, values=out.mag.angle[0:2048])
        Angle = Data1D(name="angle", unit="rad", symmetries={}, values=angle)
        out.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time, Angle],
            normalizations={},
            values=Br,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_cfft2(
            "mag.Br", freq_max=freq_max, r_max=r_max, mag_max=mag_max, N_stem=N_stem
        )

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_dataobj_cfft2.png"))

    # @unittest.skip
    def test_default_proj_surf(self):

        out = Output(simu=simu)

        # Build the data objects
        Freqs = Data1D(name="freqs", unit="Hz", symmetries={}, values=freqs_Br,)
        Wavenumber = Data1D(
            name="wavenumber", unit="", symmetries={}, values=wavenumber,
        )
        out.mag.Br = DataFreq(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Freqs, Wavenumber],
            normalizations={},
            values=Br_cfft2,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_surf("mag.Br", t_max=0.06)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_surf_dataobj.png"))

    # @unittest.skip
    def test_default_proj_compare(self):

        out = Output(simu=simu)
        out.post.legend_name = "Br"

        # Build the data objects
        Time = Data1D(name="time", unit="s", symmetries={}, values=time)
        Angle = Data1D(name="angle", unit="rad", symmetries={}, values=angle)
        out.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time, Angle],
            normalizations={},
            values=Br,
        )

        out2 = Output(simu=simu)
        out2.post.legend_name = "0.2sin(375t-1.5)"
        out2.post.line_color = "r--"

        # Get linspace data
        t0 = 0.01
        tf = 0.04
        Nt = 3000
        time2 = linspace(0.01, 0.04, 3000, endpoint=True)

        # Compute sine function
        Br2 = 0.2 * sin(375 * time2 - 1.5)

        # Build the data objects
        Time = DataLinspace(
            name="time",
            unit="s",
            symmetries={},
            initial=t0,
            final=tf,
            number=Nt,
            include_endpoint=True,
        )
        out2.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time],
            normalizations={},
            values=Br2,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_time("mag.Br", out_list=[out2])

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_compare.png"))

    # @unittest.skip
    def test_default_proj_fft2(self):

        out = Output(simu=simu)

        # Build the data objects
        Freqs = Data1D(name="freqs", unit="Hz", symmetries={}, values=MTr_freqs)
        Wavenumber = Data1D(
            name="wavenumber", unit="dimless", symmetries={}, values=MTr_wavenumber
        )
        out.mag.Br = DataFreq(
            symbol="MT_r",
            name="Radial stress applying on stator",
            unit="N/m2",
            symmetries={},
            axes=[Freqs, Wavenumber],
            normalizations={},
            values=MTr,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_fft2("mag.Br", freq_max=13000, r_max=8, mag_max=50)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_MTr_fft2_dataobj.png"))

    # @unittest.skip
    def test_default_proj_time_space(self):

        out = Output(simu=simu)

        # Build the data objects
        Time = Data1D(name="time", unit="s", symmetries={}, values=time)
        Angle = Data1D(name="angle", unit="rad", symmetries={}, values=angle)
        out.mag.Br = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            symmetries={},
            axes=[Time, Angle],
            normalizations={"space_order": 3},
            values=Br,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_A_time_space("mag.Br", freq_max=freq_max, r_max=r_max)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_time_space_dataobj.png"))
