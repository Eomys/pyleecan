from os.path import isfile
from os.path import join

import matplotlib.pyplot as plt
import pytest
from SciDataTool import DataTime, Data1D, DataLinspace, VectorField, Norm_ref
from numpy import linspace, sin, squeeze

from Tests import TEST_DATA_DIR
from Tests import save_plot_path as save_path
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D, dict_3D
from pyleecan.definitions import DATA_DIR


@pytest.fixture(scope="module")
def import_data():
    SCIM_006 = load(join(DATA_DIR, "Machine", "SCIM_006.json"))

    simu = Simu1(name="test_plots", machine=SCIM_006)

    mat_file_Br = join(TEST_DATA_DIR, "Plots", "default_proj_Br.mat")
    mat_file_time = join(TEST_DATA_DIR, "Plots", "default_proj_time.mat")
    mat_file_angle = join(TEST_DATA_DIR, "Plots", "default_proj_angle.mat")
    mat_file_Br_cfft2 = join(TEST_DATA_DIR, "Plots", "default_proj_Br_cfft2.mat")
    mat_file_Brfreqs = join(TEST_DATA_DIR, "Plots", "default_proj_Brfreqs.mat")
    mat_file_Brwavenumber = join(
        TEST_DATA_DIR, "Plots", "default_proj_Brwavenumber.mat"
    )
    if not isfile(mat_file_Br):
        import urllib.request

        url = "https://www.pyleecan.org/Data/default_proj_Br.mat"
        urllib.request.urlretrieve(url, mat_file_Br)

    if not isfile(mat_file_Br_cfft2):
        import urllib.request

        url = "https://www.pyleecan.org/Data/default_proj_Br_cfft2.mat"
        urllib.request.urlretrieve(url, mat_file_Br_cfft2)

    data = {}
    data["SCIM_006"] = SCIM_006
    data["simu"] = simu
    # Read input files from Manatee
    data["flux"] = ImportMatlab(mat_file_Br, var_name="XBr")
    data["time"] = ImportMatlab(mat_file_time, var_name="timec")
    data["angle"] = ImportMatlab(mat_file_angle, var_name="alpha_radc")

    data["flux_FT"] = ImportMatlab(mat_file_Br_cfft2, var_name="Fwr")
    data["freqs"] = ImportMatlab(mat_file_Brfreqs, var_name="freqs")
    data["wavenumber"] = ImportMatlab(mat_file_Brwavenumber, var_name="orders")
    data["OP"] = InputCurrent(N0=2000, Id_ref=10, Iq_ref=-10)
    # Plot parameters
    data["freq_max"] = 2000
    data["r_max"] = 78
    return data


class Test_plots(object):
    @pytest.mark.long_5s
    @pytest.mark.SingleOP
    @pytest.mark.SCIM
    def test_default_proj_Br_time_space(self, import_data):
        SCIM_006 = import_data["SCIM_006"]
        simu = import_data["simu"]
        time = import_data["time"]
        angle = import_data["angle"]
        flux = import_data["flux"]
        flux_FT = import_data["flux_FT"]
        freqs = import_data["freqs"]
        wavenumber = import_data["wavenumber"]
        freq_max = import_data["freq_max"]
        r_max = import_data["r_max"]
        OP = import_data["OP"]

        time_arr = squeeze(time.get_data())
        angle_arr = squeeze(angle.get_data())
        flux_arr = flux.get_data()
        norm_angle = {"space_order": Norm_ref(ref=3)}

        simu = Simu1(name="test_default_proj_Br_time_space", machine=SCIM_006)
        simu.mag = None
        simu.force = None
        simu.struct = None
        simu.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        out = Output(simu=simu)
        simu.run()

        out2 = Output(simu=simu)

        # Reduce to 1/3 period
        Br_reduced = flux_arr[0:672, 0:672]
        time_reduced = time_arr[0:672]
        angle_reduced = angle_arr[0:672]

        # Build the data objects
        Time2 = Data1D(
            name="time",
            unit="s",
            symmetries={"period": 3},
            values=time_reduced,
        )
        Angle2 = Data1D(
            name="angle",
            unit="rad",
            symmetries={"period": 3},
            values=angle_reduced,
            normalizations=norm_angle,
        )
        Br2 = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            axes=[Time2, Angle2],
            values=Br_reduced,
        )
        out2.mag.B = VectorField(
            name="Airgap flux density", symbol="B", components={"radial": Br2}
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")

        out.mag.B.plot_2D_Data(
            "time",
            "angle[0]{°}",
            data_list=[out2.mag.B],
            is_auto_ticks=False,
            legend_list=["Reference", "Periodic"],
            save_path=join(save_path, "test_default_proj_Br_dataobj_period.png"),
            is_show_fig=False,
            **dict_2D,
        )
        out.mag.B.plot_2D_Data(
            "freqs=[0," + str(freq_max) + "]",
            data_list=[out2.mag.B],
            legend_list=["Reference", "Periodic"],
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_period_fft.png"),
            is_show_fig=False,
            **dict_2D,
        )

        out3 = Output(simu=simu)

        # Get linspace data
        t0 = time_arr[0]
        tf = time_arr[-1]
        deltat = time_arr[1] - time_arr[0]
        a0 = angle_arr[0]
        deltaa = angle_arr[1] - angle_arr[0]
        Na = len(angle_arr)

        # Build the data objects
        Time3 = DataLinspace(
            name="time",
            unit="s",
            initial=t0,
            final=tf + deltat,
            step=deltat,
            include_endpoint=False,
        )
        Angle3 = DataLinspace(
            name="angle",
            unit="rad",
            normalizations=norm_angle,
            initial=a0,
            step=deltaa,
            number=Na,
            include_endpoint=False,
        )
        Br3 = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            axes=[Time3, Angle3],
            values=flux_arr,
        )
        out3.mag.B = VectorField(
            name="Airgap flux density", symbol="B", components={"radial": Br3}
        )

        # Plot the result by comparing the two simulation (Data1D / DataLinspace)
        plt.close("all")
        out.mag.B.plot_2D_Data(
            "angle{°}",
            data_list=[out3.mag.B],
            legend_list=["Reference", "Linspace"],
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_linspace.png"),
            is_show_fig=False,
            **dict_2D,
        )
        out.mag.B.components["radial"].axes[1].normalizations["space_order"] = Norm_ref(
            ref=3
        )
        out.mag.B.plot_2D_Data(
            "wavenumber->space_order=[0,100]",
            data_list=[out3.mag.B],
            legend_list=["Reference", "Linspace"],
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_linspace_fft.png"),
            is_show_fig=False,
            **dict_2D,
        )

        simu4 = Simu1(name="test_default_proj_Br_time_space_ift", machine=SCIM_006)
        simu4.mag = None
        simu4.force = None
        simu4.struct = None
        simu4.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        out4 = Output(simu=simu4)
        simu4.run()
        out4.post.legend_name = "Inverse FT"

        # Plot the result by comparing the two simulation (direct / ifft)
        plt.close("all")

        out.mag.B.plot_2D_Data(
            "angle{°}",
            data_list=[out4.mag.B],
            legend_list=["Reference", "Inverse FFT"],
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_ift.png"),
            is_show_fig=False,
            **dict_2D,
        )
        out.mag.B.plot_2D_Data(
            "wavenumber=[0,100]",
            data_list=[out4.mag.B],
            legend_list=["Reference", "Inverse FFT"],
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_ift_fft.png"),
            is_show_fig=False,
            **dict_2D,
        )

        out5 = Output(simu=simu)

        # Get linspace data
        t0 = 0.01
        tf = 0.04
        Nt = 3000
        time5 = linspace(0.01, 0.04, 3000, endpoint=True)

        # Compute sine function
        Br5 = 0.2 * sin(375 * time5 - 1.5)

        # Build the data objects
        Time5 = DataLinspace(
            name="time",
            unit="s",
            initial=t0,
            final=tf,
            number=Nt,
            include_endpoint=True,
        )
        flux5 = DataTime(
            symbol="B_r",
            name="Airgap radial flux density",
            unit="T",
            axes=[Time5],
            values=Br5,
        )
        out5.mag.B = VectorField(
            name="Airgap flux density", symbol="B", components={"radial": flux5}
        )

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")

        out.mag.B.plot_2D_Data(
            "time",
            "angle[0]{°}",
            data_list=[out5.mag.B],
            legend_list=["Br", "0.2sin(375t-1.5)"],
            save_path=join(save_path, "test_default_proj_Br_compare.png"),
            is_auto_ticks=False,
            is_show_fig=False,
            **dict_2D,
        )

    @pytest.mark.SingleOP
    @pytest.mark.SCIM
    def test_default_proj_Br_cfft2(self, import_data):
        SCIM_006 = import_data["SCIM_006"]
        simu = import_data["simu"]
        time = import_data["time"]
        angle = import_data["angle"]
        flux = import_data["flux"]
        flux_FT = import_data["flux_FT"]
        freqs = import_data["freqs"]
        wavenumber = import_data["wavenumber"]
        freq_max = import_data["freq_max"]
        r_max = import_data["r_max"]
        OP = import_data["OP"]

        N_stem = 100

        simu = Simu1(name="test_default_proj_Br_cfft2", machine=SCIM_006)
        simu.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        simu.mag = None
        simu.force = None
        simu.struct = None
        out = Output(simu=simu)
        simu.run()

        # Plot the 2D FFT of flux density as stem plot
        plt.close("all")
        out.mag.B.plot_3D_Data(
            "freqs=[0," + str(freq_max) + "]",
            "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]",
            N_stem=N_stem,
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_dataobj_cfft2.png"),
            is_show_fig=False,
            **dict_3D,
        )

    @pytest.mark.SingleOP
    @pytest.mark.SCIM
    def test_default_proj_surf(self, import_data):
        SCIM_006 = import_data["SCIM_006"]
        simu = import_data["simu"]
        time = import_data["time"]
        angle = import_data["angle"]
        flux = import_data["flux"]
        flux_FT = import_data["flux_FT"]
        freqs = import_data["freqs"]
        wavenumber = import_data["wavenumber"]
        freq_max = import_data["freq_max"]
        r_max = import_data["r_max"]
        OP = import_data["OP"]

        simu = Simu1(name="test_default_proj_surf", machine=SCIM_006)
        simu.mag = None
        simu.force = None
        simu.struct = None
        simu.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        out = Output(simu=simu)
        simu.run()

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.mag.B.plot_3D_Data(
            "time=[0,0.06]",
            "angle{°}",
            component_list=["radial"],
            save_path=join(save_path, "test_default_proj_Br_surf_dataobj.png"),
            is_2D_view=False,
            is_show_fig=False,
            **dict_3D,
        )

    @pytest.mark.SingleOP
    @pytest.mark.SCIM
    def test_default_proj_fft2(self, import_data):
        SCIM_006 = import_data["SCIM_006"]
        simu = import_data["simu"]
        time = import_data["time"]
        angle = import_data["angle"]
        flux = import_data["flux"]
        flux_FT = import_data["flux_FT"]
        freqs = import_data["freqs"]
        wavenumber = import_data["wavenumber"]
        freq_max = import_data["freq_max"]
        r_max = import_data["r_max"]
        OP = import_data["OP"]

        simu = Simu1(name="test_default_proj_fft2", machine=SCIM_006)
        simu.mag = None
        simu.force = None
        simu.struct = None
        simu.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        out = Output(simu=simu)
        simu.run()

        # Plot the 2D FFT of flux density as 2D scatter plot with colormap
        plt.close("all")
        freq_max = 500
        r_max = 20
        out.mag.B.plot_3D_Data(
            "freqs=[0," + str(freq_max) + "]",
            "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]",
            is_2D_view=True,
            is_auto_ticks=False,
            save_path=join(save_path, "test_default_proj_Br_fft2_dataobj.png"),
            is_show_fig=False,
            **dict_3D,
        )

    @pytest.mark.SingleOP
    @pytest.mark.SCIM
    def test_default_proj_time_space(self, import_data):
        SCIM_006 = import_data["SCIM_006"]
        simu = import_data["simu"]
        time = import_data["time"]
        angle = import_data["angle"]
        flux = import_data["flux"]
        flux_FT = import_data["flux_FT"]
        freqs = import_data["freqs"]
        wavenumber = import_data["wavenumber"]
        freq_max = import_data["freq_max"]
        r_max = import_data["r_max"]
        OP = import_data["OP"]

        simu = Simu1(name="test_default_proj_time_space", machine=SCIM_006)
        simu.mag = None
        simu.force = None
        simu.struct = None
        simu.input = InputFlux(B_dict={"Br": flux}, time=time, angle=angle, OP=OP)
        out = Output(simu=simu)
        simu.run()

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.mag.B.plot_3D_Data(
            "time",
            "angle{°}",
            is_2D_view=True,
            save_path=join(save_path, "test_default_proj_Br_time_space_dataobj.png"),
            is_show_fig=False,
            **dict_3D,
        )
