from numpy import arcsin, exp, pi, sqrt, sin, cos


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    point_list: list
        A list of 10 Point

    """

    Rbo = self.get_Rbo()
    Ryo=self.get_Ryoke()

    hsp = pi / self.Zs  # Half slot pitch

    # ZXt => Complex coordinate in the tooth ref
    # ZX => Complex coordinate in the slot ref
    y1t=self.W1+self.W3/2
    #Point Zch slot midium high point
    Zch=Rbo+self.H2
    #Point Zcl slot midium low point
    Zcl=Rbo
    
    
    #relation bewteen the axis tooth and the axis slot
    Zcht=Zch*exp(1j*hsp)
    xcht=Zch*cos(hsp)
    ycht=Zch*sin(hsp)
    
    Zclt=Zcl*exp(1j*hsp)
    xclt=Zcl*cos(hsp)
    yclt=Zcl*sin(hsp)
    
    #Line Zch Zcl
    #y=-(xcht-xclt)/(ycht-yclt)*x+ycht+xcht*(xcht-xclt)/(ycht-yclt)
    
    
 
    #Z4
    x4t=(self.W1+self.W3/2-ycht-xcht*(xcht-xclt)/(ycht-yclt))*-(ycht-yclt)/(xcht-xclt)
    y4t=-(xcht-xclt)/(ycht-yclt)*x4t+ycht+xcht*(xcht-xclt)/(ycht-yclt)
    Z4t=x4t+1j*y4t
    Z4=Z4t*exp(-1j*hsp)
    #Z3
    x3t=x4t
    y3t=self.W3/2+self.R1
    Z3t=x3t+1j*y3t
    Z3=Z3t*exp(-1j*hsp)
    #Z2
    x2t=x3t-self.R1
    y2t=y1t
    Z2t=x2t+1j*y2t
    Z2=Z2t*exp(-1j*hsp)
    #Z1
    y1t=self.W3/2
    x1t=sqrt((Rbo)**2-(y1t)**2)
    Z1t=x1t+1j*y1t
    Z1=Z1t*exp(-1j*hsp)
 
   
    
    




    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()


    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8]
