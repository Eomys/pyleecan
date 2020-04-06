from numpy import genfromtxt, squeeze, linspace, sin, abs as np_abs
from matplotlib.colors import ListedColormap
from scipy.io.wavfile import read
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
import unittest
from pyleecan.Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.SCIM_006 import SCIM_006

from pyleecan.Classes.Output import Output
from SciDataTool import DataTime, Data1D, DataLinspace, DataFreq
from pyleecan.Tests import DATA_DIR
from pyleecan.Classes.ImportMatlab import ImportMatlab

simu = Simu1(name="EM_SCIM_NL_006", machine=SCIM_006)

csv_file_Br = join(DATA_DIR, "default_proj_Br_time_angle.csv")
csv_file_time = join(DATA_DIR, "default_proj_time.csv")
csv_file_angle = join(DATA_DIR, "default_proj_angle.csv")
csv_file_aswl = join(DATA_DIR, "default_proj_LwiA.csv")
csv_file_freqs = join(DATA_DIR, "default_proj_freqs.csv")
csv_file_MTr_freqs = join(DATA_DIR, "default_proj_MTr_freqs.csv")
csv_file_MTr_wavenumber = join(DATA_DIR, "default_proj_MTr_wavenumber.csv")
mat_file_MTr = join(DATA_DIR, "default_proj_MTr.mat")
mat_file_Br_cfft2 = join(DATA_DIR, "default_proj_Br_cfft2.mat")
mat_file_Brfreqs = join(DATA_DIR, "default_proj_Brfreqs.mat")
mat_file_Brwavenumber = join(DATA_DIR, "default_proj_Brwavenumber.mat")
mat_file_colormap = join(DATA_DIR, "MANATEE_colormap.mat")
wav_file_sinus = join(DATA_DIR, "sinus_1000Hz_60dBSPL.wav")
wav_file_pinknoise = join(DATA_DIR, "PinkNoise_40dBpHz@1000Hz.wav")
wav_file_trafic = join(DATA_DIR, "trafic.wav")

# Read input files from Manatee
Br = genfromtxt(csv_file_Br, delimiter=",")
Br[0, 0] = -0.179266312
time = genfromtxt(csv_file_time, delimiter=",")
time[0] = 0
angle = genfromtxt(csv_file_angle, delimiter=",")
angle[0] = 0
aswl = genfromtxt(csv_file_aswl, delimiter=",")
aswl[0] = 0
freqs = genfromtxt(csv_file_freqs, delimiter=",")
freqs[0] = 0

MTr_freqs = genfromtxt(csv_file_MTr_freqs, delimiter=",")
MTr_freqs[0] = 0
MTr_wavenumber = genfromtxt(csv_file_MTr_wavenumber, delimiter=",")
MTr_wavenumber[0] = -8
MTr = squeeze(ImportMatlab(file_path=mat_file_MTr, var_name="XPwr").get_data())
Br_cfft2 = squeeze(ImportMatlab(file_path=mat_file_Br_cfft2, var_name="Fwr").get_data())
freqs_Br = squeeze(
    ImportMatlab(file_path=mat_file_Brfreqs, var_name="freqs").get_data()
)
wavenumber = squeeze(
    ImportMatlab(file_path=mat_file_Brwavenumber, var_name="orders").get_data()
)
newcolors = squeeze(
    ImportMatlab(file_path=mat_file_colormap, var_name="mymap").get_data()
)
colormap = ListedColormap(newcolors)
freq_max = 13000
r_max = 78

rate_sinus, sinus = read(wav_file_sinus)
if sinus.dtype == "int16":
    nb_bits = 16  # -> 16-bit wav files
elif sinus.dtype == "int32":
    nb_bits = 32  # -> 32-bit wav files
max_nb_bit = float(2 ** (nb_bits - 1))
sinus = sinus / (
    max_nb_bit
)  # samples is a numpy array of float representing the samples
rate_pinknoise, pinknoise = read(wav_file_pinknoise)
if pinknoise.dtype == "int16":
    nb_bits = 16  # -> 16-bit wav files
elif pinknoise.dtype == "int32":
    nb_bits = 32  # -> 32-bit wav files
max_nb_bit = float(2 ** (nb_bits - 1))
pinknoise = pinknoise / (
    max_nb_bit
)  # samples is a numpy array of float representing the samples
rate_trafic, trafic = read(wav_file_trafic)


class tests_dataobj(TestCase):
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

    @unittest.skip
    def test_sinus_thirdoct(self):

        out = Output(simu=simu)

        # Build the data objects
        Time = DataLinspace(
            name="time",
            unit="s",
            symmetries={},
            initial=0,
            final=1.0,
            number=rate_sinus,
            include_endpoint=False,
        )
        SPL = DataTime(
            symbol="SPL",
            name="Sound Pressure Level",
            unit="Pa",
            symmetries={},
            axes=[Time],
            normalizations={"Pa": 2.0e-5},
            values=sinus[1:],
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_ASWL(SPL)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_sinus_thirdoct_dataobj.png"))

    @unittest.skip
    def test_pinknoise_thirdoct(self):

        out = Output(simu=simu)

        # Build the data objects
        Time = DataLinspace(
            name="time",
            unit="s",
            symmetries={},
            initial=0,
            final=1.0,
            number=rate_pinknoise + 1,
            include_endpoint=False,
        )
        SPL = DataTime(
            symbol="SPL",
            name="Sound Pressure Level",
            unit="Pa",
            symmetries={},
            axes=[Time],
            normalizations={"Pa": 2.0e-5},
            values=pinknoise,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_ASWL(SPL)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_pinknoise_thirdoct_dataobj.png"))

    @unittest.skip
    def test_default_proj_aswl_thirdoct(self):

        out = Output(simu=simu)

        # Build the data objects
        Freqs = Data1D(name="freqs", unit="Hz", symmetries={}, values=freqs)
        ASWL = DataFreq(
            symbol="ASWL",
            name="A-weighted Sound Power Level",
            unit="dBA",
            symmetries={},
            axes=[Freqs],
            normalizations={},
            values=aswl,
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_ASWL(ASWL, is_dBA=True)

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_ASWL_thirdoct_dataobj.png"))

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
        out.plot_A_surf("mag.Br", t_max=0.06, colormap=colormap)

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
        out.plot_A_fft2(
            "mag.Br", freq_max=13000, r_max=8, mag_max=50, colormap=colormap
        )

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
        out.plot_A_time_space(
            "mag.Br", colormap=colormap, freq_max=freq_max, r_max=r_max
        )

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_default_proj_Br_time_space_dataobj.png"))
