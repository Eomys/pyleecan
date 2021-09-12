import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
from Tests import TEST_DIR
from os.path import join, abspath, isfile

TUTO_DIR = abspath(join(TEST_DIR, "..", "Tutorials"))


@pytest.mark.skip
@pytest.mark.parametrize("tuto_name", ["tuto_Machine"])
def test_short_tutorial(tuto_name):
    """Execute the tutorial"""
    # Read the notebook
    with open(abspath(join(TUTO_DIR, tuto_name + ".ipynb"))) as f:
        nb = nbformat.read(f, as_version=4)

    # Execute it
    ep = ExecutePreprocessor(timeout=-1, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": abspath(join(TEST_DIR, ".."))}})


@pytest.mark.skip
@pytest.mark.long_5s
@pytest.mark.parametrize(
    "tuto_name",
    ["tuto_Simulation_FEMM", "tuto_Force", "tuto_Plots", "tuto_Optimization"],
)
def test_long_tutorial(tuto_name):
    """Execute the tutorial"""
    # Read the notebook
    with open(abspath(join(TUTO_DIR, tuto_name + ".ipynb"))) as f:
        nb = nbformat.read(f, as_version=4)

    # Execute it
    ep = ExecutePreprocessor(timeout=-1, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": abspath(join(TEST_DIR, ".."))}})
