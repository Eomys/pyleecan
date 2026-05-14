# Simulation Models

This folder stores simulation model inputs that were previously placed in the repository root.

Current contents:

- `SimulationModels/Toyota_Prius_2004/IPMSM_Toyota_Prius_2004.json`
- `SimulationModels/Nissan_Leaf_2012/leaf.dxf`
- `SimulationModels/Nissan_Leaf_2012/Nissan_Leaf_2012_DXF.json`

Notes:

- `IPMSM_Toyota_Prius_2004.json` is used as the loss-capable template machine for the local Nissan Leaf validation workflow.
- `leaf.dxf` is the supplied rotor/stator drawing used to rebuild the Leaf 2012 machine geometry.
- `Nissan_Leaf_2012_DXF.json` is the current tracked Pyleecan machine JSON exported from the latest calibrated Leaf validation snapshot.
- Generated results remain under `.local/verification/` and are not part of this tracked model-input folder.
