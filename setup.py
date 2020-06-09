import setuptools
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

python_requires = ">= 3.5"

# Pyleecan dependancies
install_requires = [
    "cloudpickle>=1.3.0",
    "gmsh-sdk>=4.5.5.post1",
    "matplotlib>=3.2.1",
    "mock>=4.0.2",
    "numpy>=1.18.2",
    "pandas>=1.0.3",
    "PyQt5>=5.14.1",
    "PyQt5-sip>=12.7.1",
    "scipy>=1.4.1",
    "xlrd>=1.2.0",
    "deap>=1.3.1",
    "SciDataTool>=0.0.4",
    "pyfemm >= 0.1.0;platform_system=='Windows'",
]

tests_require = [
    "ddt>=1.3.1",
    "pytest>=5.4.1",
]

setuptools.setup(
    name="pyleecan",
    version="0.0.0.0",
    author="Pyleecan Developers",
    author_email="",
    description="Python Library for Electrical Engineering Computational Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/pyleecan",
    download_url="https://github.com/Eomys/pyleecan.git",
    packages=setuptools.find_packages(exclude=["Tests", "Tutorials"]),
    package_data={
        # Include any *.json files found in pyleecan:
        # '': ['*.json'],
        "pyleecan": ["*.json"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
    install_requires=install_requires,
    tests_require=tests_require,
)
