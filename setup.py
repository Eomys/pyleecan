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

PYLEECAN_VERSION = "1.4.0"


with open("README.md", "r") as fh:
    long_description = fh.read()

python_requires = ">= 3.6"

# Pyleecan main dependancies
install_requires = [
    "cloudpickle>=1.3.0",
    "ezdxf==0.14.2",
    "h5py>=3.2.1",
    "matplotlib>=3.3.2",
    "meshio>=4.0.15,<=4.4.6",
    "numpy>1.19.5",
    "pandas>=1.0.3",
    'pyfemm>=0.1.1;platform_system=="Windows"',
    "PySide2>=5.15.2",
    "pyuff>=1.25",
    "pyvista>=0.25.3,<=0.31.3",
    "quadpy",
    "SciDataTool>=2.5.0",
    "scipy>=1.4.1",
    "setuptools",
    "git+https://gitlab.com/CedMrnl/swat-em.git",
    "xlrd>=1.2.0",
    "xlwt>=1.3.0",
]
# Pyleecan optional dependancies
full_require = [
    'deap>=1.3.1',
    'smoot>=0.1.0',
    'gmsh-sdk>=4.6.0',
]

# Pyleecan Test dependancies
tests_require = [
    "ddt>=1.3.1",
    "hypothesis",
    "mock>=4.0.2",
    "nbconvert",
    "nbformat",
    "pytest>=5.4.1",
    "pytest-qt>=3.3.0",
]

setuptools.setup(
    name="pyleecan",
    version=PYLEECAN_VERSION,
    author="Pyleecan Developers",
    author_email="pyleecan@framalistes.org",
    description="Python Library for Electrical Engineering Computational Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/pyleecan",
    download_url="https://github.com/Eomys/pyleecan/archive/"
    + PYLEECAN_VERSION
    + ".tar.gz",
    packages=setuptools.find_packages(exclude=["Tests*", "Tutorials*"]),
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
        "test": tests_require,
        "full": full_require
    },  # Enables to install the test dependancies using pip install pyleecan[test]
)
