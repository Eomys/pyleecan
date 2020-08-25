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
    #Point Zch
    Zch=Rbo+self.H2
    #Zcl
    Zcl=Rbo
    
    
    #relation bewteen the axis tooth and the axis slot
    Zcht=Zch*exp(1j*hsp)
    xcht=Zch*cos(hsp)
    ycht=Zch*sin(hsp)
    
    Zclt=Zcl*exp(1j*hsp)
    xclt=Zcl*cos(hsp)
    yclt=Zcl*sin(hsp)
    
    #Line Zch Zcl
    y=-(xcht-xclt)/(ycht-yclt)*x+ycht+xcht*(xcht-xclt)/(ycht-yclt)
    
    #Z1
    x1t=(self.W1+self.W3/2-ycht-xcht*(xcht-xclt)/(ycht-yclt))*-(ycht-yclt)/(xcht-xclt)
    y1t=-(xcht-xclt)/(ycht-yclt)*x1t+ycht+xcht*(xcht-xclt)/(ycht-yclt)
    Z1t=x1t+1j*y1t
    Z1=Z1t*exp(-1j*hsp)
    
    #Z2
    x2t=x1t
    y2t=self.W3/2+self.R1
    Z2t=x2t+1j*y2t
    Z2=Z2t*exp(-1j*hsp)
    
    #Z3
    x3t=x2t-self.R1
    y3t=self.W3/2
    Z3t=x3t+1j*y3t
    Z3=Z3t*exp(-1j*hsp)
    
    #Z4
    y4t=y3t
    x4t=sqrt((Rbo)**2-(y4t)**2)
    Z4t=x4t+1j*y4t
    Z4=Z4t*exp(-1j*hsp)


    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()


    return [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8]
