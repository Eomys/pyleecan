try:
    import setuptools
except ImportError:  # Install setuptools if needed
    from os import system
    from sys import executable

    # run 'pip install setuptools'
    system("{} -m pip install setuptools".format(executable))

    import setuptools

import platform

# /!\ Increase the number before a release
# See https://www.python.org/dev/peps/pep-0440/
# Examples :
# First alpha of the release 0.1.0 : 0.1.0a1
# First beta of the release 1.0.0 : 1.0.0b1
# Second release candidate of the release 2.6.4 : 2.6.4rc2
# Release 1.1.0 : 1.1.0
# First post release of the release 1.1.0 : 1.1.0.post1

PYLEECAN_VERSION = "0.1.0.rc1"


with open("README.md", "r") as fh:
    long_description = fh.read()

python_requires = ">= 3.6"

# Pyleecan dependancies
install_requires = [
    "setuptools",
    "cloudpickle>=1.3.0",
    "matplotlib>=3.2.1",
    "numpy>=1.18.2",
    "pandas>=1.0.3",
    "PyQt5>=5.14.1",
    "PyQt5-sip>=12.7.1",
    "scipy>=1.4.1",
    "xlrd>=1.2.0",
    "deap>=1.3.1",
    "SciDataTool>=1.1.1",
    "pyvista>=0.25.3",
    "meshio>=4.0.15",
    "h5py>=2.10.0",
    'pyfemm >= 0.1.0;platform_system=="Windows"',
]


tests_require = ["ddt>=1.3.1", "pytest>=5.4.1", "mock>=4.0.2", "nbformat", "nbconvert"]

setuptools.setup(
    name="pyleecan",
    version=PYLEECAN_VERSION,
    author="Pyleecan Developers",
    author_email="pyleecan@framalistes.org",
    description="Python Library for Electrical Engineering Computational Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/pyleecan",
    download_url="https://github.com/Eomys/pyleecan/SciDataTool/archive/"
    + PYLEECAN_VERSION
    + ".tar.gz",
    packages=setuptools.find_packages(exclude=["Tests", "Tutorials"]),
    package_data={
        # Include any *.json files found in pyleecan:
        # '': ['*.json'],
        "pyleecan": ["*.json"]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
    install_requires=install_requires,
    extras_require={
        "test": tests_require
    },  # Enables to install the test dependancies using pip install pyleecan[test]
)
