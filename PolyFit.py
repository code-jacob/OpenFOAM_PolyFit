# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:03:03 2024

@author: trusinja
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

fluid = "air"

n = 7

quant_list = [ "rho_1atm" , "cp" , "mu" , "kappa" ]
quant_list_units = [ "[kg/m^3]" , "[J/kg/K]" , "[Pa.s]" , "[W/m/K]" ]


ii = 0
for quant in quant_list:
    inpfile = os.path.join(".\\", fluid , quant +".txt")
    
    df = pd.read_csv( inpfile , sep='\s+') #, delimiter="\t")
    print(df)
    
    fig1 = plt.figure(num=None, figsize=(10, 8), dpi=80 )
    fig1.canvas.manager.set_window_title(quant)
    plt.title(quant, fontsize=20)
    
    clr = "k"
    x = df.iloc[:, 0].to_numpy()
    y = df.iloc[:, 1].to_numpy()
    # print(name_M + " =", str("%.0f"%(Torque.iloc[-1])) )
    plt.plot( x , y , label= quant , linestyle='-', linewidth= 3, color=clr )
    plt.plot( x , y , "s", color=clr, markersize=8 )
    # plt.text(Time.iloc[-1], Torque.iloc[-1] , str("%.0f"%(Torque.iloc[-1])), fontsize= 20 , color=clr, horizontalalignment='center', verticalalignment='top' )        
    
    plt.rc('xtick', labelsize= 14)   
    plt.rc('ytick', labelsize= 14) 
    plt.ylabel('$'+quant+'$' + ' $'+quant_list_units[ii]+'$ ' , fontsize = 14)
    ii+=1
    plt.xlabel('$T$' + ' $[K]$ ' , fontsize = 14)
    plt.legend(loc='best', shadow= True,  ncol=1, fontsize= 16)
    
    plt.grid(linestyle= '--', linewidth= 2) 
    plt.tight_layout()
    plt.show()
    
    coefficients = np.polyfit(x, y, n - 1)
    f = np.poly1d(coefficients)
    xx = np.linspace(x[0], x[-1], 100)
    fxx = f(xx)
    plt.plot( xx, fxx , 'b--', linewidth= 4 )
    
    print(" coefficients = \n" , (coefficients) )
    coefficients = np.append(np.zeros(8-n),coefficients)
    
    print("\n",quant)
    print("(", *np.flip(coefficients), ")")


