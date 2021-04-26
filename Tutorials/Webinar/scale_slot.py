

def scale_slot(simu, scale_factor):
   """Edit stator slot size according to a percentage

   Parameters
   ----------
   simu: Simulation
     simulation to modify
   scale_factor: float
     stator slot scale factor
   """
   simu.machine.stator.slot.W0 *= scale_factor
   simu.machine.stator.slot.W1 *= scale_factor
   simu.machine.stator.slot.W2 *= scale_factor
   
   simu.machine.stator.slot.H0 *= scale_factor
   simu.machine.stator.slot.H1 *= scale_factor
   simu.machine.stator.slot.H2 *= scale_factor
   
   simu.machine.stator.slot.R1 *= scale_factor
