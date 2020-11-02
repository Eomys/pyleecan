# -*- coding: utf-8 -*-
from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataTime, VectorField

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Magnetics module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Magnetic object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    self.get_logger().info("Starting Magnetic module")
    output = self.parent.parent   
    
    # Compute and store time and angle axes from elec output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_time_angle(output)    
    
    # Calculate airgap flux
    (Br, Bt, Bz, Tem, Phi_wind_stator) = self.comp_flux_airgap(output, axes_dict)    
    
    # Get time and angular axes
    Angle = axes_dict["Angle"]
    Time = axes_dict["Time"]    
    
    # Store the results
    # Store airgap flux as VectorField object
    axis_list = [Time, Angle] # Axes for each airgap flux component
    output.mag.B = VectorField(
            name="Airgap flux density",
            symbol="B",            
        )
    # Radial flux component
    if Br is not None:
         output.mag.B.components["radial"]= DataTime(
            name="Airgap radial flux density",
            unit="T",
            symbol="B_r",
            axes=axis_list,
            values=Br,
        )
    # Tangential flux component
    if Bt is not None:     
        output.mag.B.components["tangential"]= DataTime(
            name="Airgap tangential flux density",
            unit="T",
            symbol="B_t",
            axes=axis_list,
            values=Bt,
        )
    # Axial flux component
    if Bz is not None:     
        output.mag.B.components["axial"]= DataTime(
            name="Airgap tangential flux density",
            unit="T",
            symbol="B_z",
            axes=axis_list,
            values=Bz,
        )
        
    # Store electromagnetic torque over time, and global values: average, peak to peak and ripple
    if Tem is not None:
        Time_Tem = axes_dict["Time_Tem"]    
        
        output.mag.Tem = DataTime(
            name="Electromagnetic torque",
            unit="Nm",
            symbol="T_{em}",
            axes=[Time_Tem],
            values=Tem,
        )
                
        output.mag.Tem_av = mean(Tem)
        self.get_logger().debug("Average Torque: " + str(output.mag.Tem_av) + " N.m")
        
        output.mag.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]    
        if output.mag.Tem_av != 0:
            output.mag.Tem_rip_norm = output.mag.Tem_rip_pp / output.mag.Tem_av  # []
        else:
            output.mag.Tem_rip_norm = None
    
    # Store stator winding flux and calculate electromotive force
    if Phi_wind_stator is not None:
        Phase = [axe for axe in Is.axes if axe.name == "phase"]
        
        output.mag.Phi_wind_stator = DataTime(
            name="Stator Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            values=Phi_wind_stator,
        )
        
        # Electromotive forces computation (update output)
        output.mag.comp_emf()

