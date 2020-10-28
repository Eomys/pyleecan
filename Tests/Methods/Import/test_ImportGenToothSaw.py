# -*- coding: utf-8 -*-

import pytest
from os import mkdir
from os.path import isdir, join

from numpy import linspace
import matplotlib.pyplot as plt

from pyleecan.Classes.ImportGenToothSaw import ImportGenToothSaw
from Tests import save_plot_path as save_path


save_path = join(save_path, "Import")
if not isdir(save_path):
    mkdir(save_path)


def test_forward():
    """Check that the ImportGenToothSaw can generate forward toothsaw"""
    Tf = 2
    N = 2048 * 4
    test_obj = ImportGenToothSaw(type_signal=0, f=4, A=2, N=N, Tf=Tf)

    # Generate the signal
    time = linspace(start=0, stop=Tf, num=N, endpoint=False)
    result = test_obj.get_data()

    # Plot/save the result
    plt.close("all")
    plt.plot(time, result)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_forward.png"))

    # Check the signal
    assert result.shape == (N,)
    assert max(result) == pytest.approx(2, abs=0.01)
    assert min(result) == pytest.approx(-2, abs=0.01)
    assert result[0] == pytest.approx(0)
    assert result[-1] == pytest.approx(-0.004, abs=0.001)


def test_forward_delay():
    """Check that the ImportGenToothSaw can generate forward toothsaw"""
    Tf = 2
    N = 2048 * 4
    test_obj = ImportGenToothSaw(type_signal=0, Dt=0.2, f=4, A=2, N=N, Tf=Tf)

    # Generate the signal
    time = linspace(start=0, stop=Tf, num=N, endpoint=False)
    result = test_obj.get_data()

    # Plot/save the result
    plt.close("all")
    plt.plot(time, result)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_forward_delay.png"))

    # Check the signal
    assert result.shape == (N,)
    assert max(result) == pytest.approx(2, abs=0.01)
    assert min(result) == pytest.approx(-2, abs=0.01)
    assert result[0] == pytest.approx(-0.8, abs=0.01)
    assert result[-1] == pytest.approx(-0.8, abs=0.01)


def test_backward():
    """Check that the ImportGenToothSaw can generate backward toothsaw"""
    Tf = 1
    N = 2048 * 4
    test_obj = ImportGenToothSaw(type_signal=1, f=4, A=4, N=N, Tf=Tf)

    # Generate the signal
    time = linspace(start=0, stop=Tf, num=N, endpoint=False)
    result = test_obj.get_data()

    # Plot/save the result
    plt.close("all")
    plt.plot(time, result)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_backward.png"))

    # Check the signal
    assert result.shape == (N,)
    assert max(result) == pytest.approx(4, abs=0.01)
    assert min(result) == pytest.approx(-4, abs=0.01)
    assert result[0] == pytest.approx(0)
    assert result[-1] == pytest.approx(0.0039, abs=0.01)


def test_sym():
    """Check that the ImportGenToothSaw can generate symmetry toothsaw"""
    Tf = 1
    N = 2048 * 4
    test_obj = ImportGenToothSaw(type_signal=2, f=4, A=4, N=N, Tf=Tf)

    # Generate the signal
    time = linspace(start=0, stop=Tf, num=N, endpoint=False)
    result = test_obj.get_data()

    # Plot/save the result
    plt.close("all")
    plt.plot(time, result)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_sym.png"))

    # Check the signal
    assert result.shape == (N,)
    assert max(result) == 4
    assert min(result) == -4
    assert result[0] == pytest.approx(0)
    assert result[-1] == pytest.approx(-0.007, abs=0.001)
