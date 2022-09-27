from ...Functions.FEMM.create_FEMM_boundary_conditions import (
    create_FEMM_boundary_conditions,
)


def get_FEMM_BC_propname(femm, line_label, BC_dict):
    """Get/create the Boundary coundition corresponding the line

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    line_label : str
        BOUNDARY_PROP_LAB of the line
    BC_dict : dict
        Boundary condition dict ([line label] = BC name)

    Returns
    -------
    propname : str
        Name of the property to set
    """

    if line_label not in BC_dict:
        create_FEMM_boundary_conditions(femm, line_label, BC_dict)
    return BC_dict[line_label]
