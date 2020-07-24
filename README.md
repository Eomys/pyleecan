# <img alt="Pyleecan" src="https://www.pyleecan.org/_static/favicon.png" height="120">

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Presentation
PYLEECAN™ objective is to provide a **user-friendly, unified, flexible simulation framework for the multiphysic design and optimization of electrical machines and drives** based on fully open-source software.

It is meant to be used by researchers, R&D engineers and teachers in electrical engineering, both on standard topologies of electrical machines and on novel topologies (e.g. during a PhD work). 
An objective of PYLEECAN is that **every PhD student should start with PYLEECAN instead of implementing his own scripts (e.g. coupling Scilab or Matlab with Femm)**.

## Scope
The initial scope of the project is to simulate the electromagnetic performances of the following 2D radial flux machines:
* Interior, Surface and Surface Inset Permanent Magnet Synchronous Machines (IPMSM, SPMSM, SIPMSM) with inner or outer rotor
* Squirrel Cage Induction Machines (SCIM) and Doubly Fed Induction Machines (DFIM)
* Synchro Reluctant Machines (SyRM)
* Switched Reluctance Machines (SRM).

The project should then address 3D topologies (axial flux machines, claw-pole synchronous machines) and linear machines.
On a longer term, PYLEECAN should also include the following five physics with different model granularity (e.g. analytic, semi-analytic, finite element):
* Electrical
* Electromagnetics
* Heat Transfer
* Structural Mechanics
* Acoustics

## Origin and status of the project
EOMYS initiated in 2018 the open-source project named PYLEECAN (Python Library for Electrical Engineering Computational Analysis) under Apache license by releasing a part of [MANATEE](https://eomys.com/produits/manatee/article/logiciel-manatee?lang=en) commercial software scripts. These initial scripts included a fully **object-oriented modelling** of main radial flux electrical machines, with parameterized geometry. However, PYLEECAN is not an EOMYS-only project, the initial maintainers includes other companies and universities and all contributors are welcome.

* PYLEECAN is fully coupled to [FEMM](http://www.femm.info) to carry **non-linear magnetostatic** analysis including sliding band and symmetries. For now this coupling is available only on Windows.
* PYLEECAN includes a **Graphical User Interface** to define main 2D radial flux topologies parametrized geometries (PMSM, IM, SRM, SyRM) including material library.
* PYLEECAN is coupled to [Gmsh](http://gmsh.info/) **2D/3D finite element mesh generator** to run third-party multiphysic solvers. 
* PYLEECAN is coupled to a **multiobjective optimization** library to carry design optimization of electrical machines.

If you are interested by a topology or a specific model, you can [open an issue](https://github.com/Eomys/pyleecan/issues) on this Github repository to talk about it. We will gladly explain how to add it yourself or we will add it to the development list for further release.

## Documentation / Website
For now all the information on the project are available on [www.pyleecan.org](http://www.pyleecan.org). At this link, you will find the ICEM 2018 publication and the architecture documentation.

## Contact
You can contact us on Github by opening an issue (to request a feature, ask a question or report a bug) or at pyleecan@framalistes.org that redirect to all the maintainers.
