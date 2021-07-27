# -*- coding: utf-8 -*-

from os import mkdir
from os.path import isdir, join

import matplotlib.pyplot as plt
import pytest
from numpy import linspace
from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from Tests import save_plot_path as save_path

save_path = join(save_path, "Import")
if not isdir(save_path):
    mkdir(save_path)


def testSPWM():
    """Check """
    # fs, duration, f,fmax,fmode, fswimode,fswi, fswi_max,typePWM, Vdc1, U0, type_carrier
    for ii in range(2):
        for jj in range(4):
            for hh in range(4):
                test_obj = ImportGenPWM(
                    fs=96000,
                    duration=2,
                    f=1,
                    fmax=5,
                    fmode=ii,
                    fswimode=jj,
                    fswi=5,
                    fswi_max=15,
                    typePWM=8,
                    Vdc1=2,
                    U0=0.70,
                    type_carrier=hh,
                )
                # Generate the signal
                time = linspace(start=0, stop=2, num=2 * 96000, endpoint=True)
                Triphase = test_obj.get_data()[0]
                Vas=test_obj.get_data()[1]
                Triangle=test_obj.get_data()[3]


                

                # Plot/save the result
                plt.close("all")
                plt.plot(time, Triphase[:, 1])
                plt.plot(time, Vas)
                plt.plot(time, Triangle)
                fig = plt.gcf()
                fig.savefig(
                    join(
                        save_path,
                        "test_ImportGenPWM_"
                        + str(ii)
                        + "_"
                        + str(jj)
                        + "_"
                        + str(hh)
                        + "_SPWM.png",
                    )
                )


def testDPWM():
    """Check """
    for ii in range(9):
        # fs, duration, f,fmax,fmode, fswimode,fswi, fswi_max,typePWM, Vdc1, U0, type_carrier
        test_obj = ImportGenPWM(
            fs=96000,
            duration=2,
            f=1,
            fmax=5,
            fmode=0,
            fswimode=0,
            fswi=10,
            fswi_max=30,
            typePWM=ii,
            Vdc1=2,
            U0=0.70,
            type_carrier=0,
        )
        # Generate the signal
        time = linspace(start=0, stop=2, num=2 * 96000, endpoint=True)
        Triphase = test_obj.get_data()[0]
        Vas=test_obj.get_data()[1]
        Triangle=test_obj.get_data()[3]


        # Plot/save the result
        plt.close("all")
        plt.plot(time, Triphase[:, 1])
        plt.plot(time, Vas)
        plt.plot(time, Triangle)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_ImportGenPWM_" + str(ii) + ".png"))


if __name__ == "__main__":
    testDPWM()
    testSPWM()