# -*- coding: utf-8 -*-

import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def comp_coeff(self, file_path : str):
    """Enables to compute the coefficients of the loss model with a curve fitting
    on loss data, provided in a text file

    Parameters
    ----------
    file_path : str
        the full path of the file containing the loss data.
        Must contain 3 columns separated by spaces of tabulations :
        1st column : frequency
        2nd column : flux density magnitude
        3rd column : power loss (W)

    Returns
    -------
    Bool
        True if the curve fitting was succesfull, else False.
    """    
    
    Ch=self.k_hy
    Ce=self.k_ed
    alpha_f=self.alpha_f
    alpha_B=self.alpha_B

    def comp_loss(xdata, Ch, Ce, alpha_f, alpha_B):
        f=xdata[0]
        B=xdata[1]
        return Ch * f ** alpha_f * B ** alpha_B + Ce * (f * B) ** 2   

    with open(file_path,"r") as f:
        data=f.readlines()

    is_iron_loss = False
    f, B, loss = [], [], []
    for line in data:
        line=line.rstrip()
        if re.search("Iron loss",line, flags = re.I):
            is_iron_loss = True
        elif is_iron_loss:
            line=re.split(r"[\t\n ]+",line)
            if len(line)<3:
                is_iron_loss = False
            else:
                f.append(float(line[0]))
                B.append(float(line[1]))
                loss.append(float(line[2]))

    xdata=np.array([f,B])
    ydata=np.array(loss)
    popt,pcov=curve_fit(comp_loss,xdata,ydata)
    print(popt)

    B_check=np.linspace(0,2,1000)
    f_check_2000=np.ones((1000,))*2000
    f_check_50=np.ones((1000,))*50
    xverif1=np.array([f_check_50, B_check])
    xverif2=np.array([f_check_2000, B_check])
    plt.plot(B[:17], loss[:17],color='blue',label='measurements with f=50Hz',marker='o')
    plt.plot(B[155:], loss[155:],color='red',label='measurements with f=2000Hz',marker='o')
    plt.plot(B_check, comp_loss(xverif1, *popt),color='blue',linestyle='dashed',label='fitting with f=50Hz')
    plt.plot(B_check, comp_loss(xverif2, *popt),color='red',linestyle='dashed',label='fitting with f=2000Hz')
    plt.legend()
    plt.show()

    self.k_hy=popt[0]
    self.k_ed=popt[1]
    self.alpha_f=popt[2]
    self.alpha_B=popt[3]
    
    return True
