# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sy
import math
from csv import reader
from sklearn.metrics import mean_squared_error
from tqdm import trange
#%%
import numba 
from numba import jit

with open('sin.csv' , 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
csv_file.close() 
del list_of_rows[0]
text=np.asarray([x[0] for x in list_of_rows])
T=np.asarray([x[1] for x in list_of_rows],dtype=float)
V0=np.asarray([x[2] for x in list_of_rows],dtype=float)
V1=np.asarray([x[3] for x in list_of_rows],dtype=float)
V2=np.asarray([x[4] for x in list_of_rows],dtype=float)
V3=np.asarray([x[5] for x in list_of_rows],dtype=float)
V4=np.asarray([x[6] for x in list_of_rows],dtype=float)
V5=np.asarray([x[7] for x in list_of_rows],dtype=float)
V6=np.asarray([x[8] for x in list_of_rows],dtype=float)

Vgamma1=np.asarray([x[9] for x in list_of_rows],dtype=float)
Vgamma2=np.asarray([x[10] for x in list_of_rows],dtype=float)
Vgamma3=np.asarray([x[11] for x in list_of_rows],dtype=float)
Vgamma4=np.asarray([x[12] for x in list_of_rows],dtype=float)
Vgamma5=np.asarray([x[13] for x in list_of_rows],dtype=float)
Vgamma6=np.asarray([x[14] for x in list_of_rows],dtype=float)

with open('V_target_sin.csv' , 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
csv_file.close() 
del list_of_rows[0]
Vt0=np.asarray([x[0] for x in list_of_rows],dtype=float)
Vt1=np.asarray([x[1] for x in list_of_rows],dtype=float)
Vt2=np.asarray([x[2] for x in list_of_rows],dtype=float)
Vt3=np.asarray([x[3] for x in list_of_rows],dtype=float)
Vt4=np.asarray([x[4] for x in list_of_rows],dtype=float)
Vt5=np.asarray([x[5] for x in list_of_rows],dtype=float)
Vt6=np.asarray([x[6] for x in list_of_rows],dtype=float)

Vtgamma1=np.asarray([x[7] for x in list_of_rows],dtype=float)
Vtgamma2=np.asarray([x[8] for x in list_of_rows],dtype=float)
Vtgamma3=np.asarray([x[9] for x in list_of_rows],dtype=float)
Vtgamma4=np.asarray([x[10] for x in list_of_rows],dtype=float)
Vtgamma5=np.asarray([x[11] for x in list_of_rows],dtype=float)
Vtgamma6=np.asarray([x[12] for x in list_of_rows],dtype=float)
umax=np.asarray([x[13] for x in list_of_rows],dtype=float)
for num in range(0,len(T),1):
    ttt=np.arange(0,2*T[num]+0.01,0.01)
                
    vfourier=(  V0[num] 
              + V1[num]*np.sin( 2*np.pi*ttt/T[num]+Vgamma1[num])
              + V2[num]*np.sin( 4*np.pi*ttt/T[num]+Vgamma2[num])
              + V3[num]*np.sin( 6*np.pi*ttt/T[num]+Vgamma3[num])
              + V4[num]*np.sin( 8*np.pi*ttt/T[num]+Vgamma4[num])
              + V5[num]*np.sin(10*np.pi*ttt/T[num]+Vgamma5[num])
              + V6[num]*np.sin(12*np.pi*ttt/T[num]+Vgamma6[num])
             )  
    count=0
    cnt=0  
    while cnt!=-1:
          if(vfourier[count]<0):
              if(vfourier[count+1]>0):
                  cnt=-1
          count =  count + 1 

    t=np.arange(count,count+T[num]*100+1,1)
    t=t/100
    vfourier=(  V0[num] 
              + V1[num]*np.sin( 2*np.pi*t/T[num]+Vgamma1[num])
              + V2[num]*np.sin( 4*np.pi*t/T[num]+Vgamma2[num])
              + V3[num]*np.sin( 6*np.pi*t/T[num]+Vgamma3[num])
              + V4[num]*np.sin( 8*np.pi*t/T[num]+Vgamma4[num])
              + V5[num]*np.sin(10*np.pi*t/T[num]+Vgamma5[num])
              + V6[num]*np.sin(12*np.pi*t/T[num]+Vgamma6[num])
             )
    
    vtarge=(  Vt0[num] 
              + Vt1[num]*np.sin( 2*np.pi*ttt/T[num]+Vtgamma1[num])
              + Vt2[num]*np.sin( 4*np.pi*ttt/T[num]+Vtgamma2[num])
              + Vt3[num]*np.sin( 6*np.pi*ttt/T[num]+Vtgamma3[num])
              + Vt4[num]*np.sin( 8*np.pi*ttt/T[num]+Vtgamma4[num])
              + Vt5[num]*np.sin(10*np.pi*ttt/T[num]+Vtgamma5[num])
              + Vt6[num]*np.sin(12*np.pi*ttt/T[num]+Vtgamma6[num])
             )  
    count=0
    cnt=0  
    while cnt!=-1:
          if(vtarge[count]<0):
              if(vtarge[count+1]>0):
                  cnt=-1
          count =  count + 1 

    tt=np.arange(count,count+T[num]*100+1,1)
    tt=tt/100
    vtarge=(  Vt0[num] 
              + Vt1[num]*np.sin( 2*np.pi*tt/T[num]+Vtgamma1[num])
              + Vt2[num]*np.sin( 4*np.pi*tt/T[num]+Vtgamma2[num])
              + Vt3[num]*np.sin( 6*np.pi*tt/T[num]+Vtgamma3[num])
              + Vt4[num]*np.sin( 8*np.pi*tt/T[num]+Vtgamma4[num])
              + Vt5[num]*np.sin(10*np.pi*tt/T[num]+Vtgamma5[num])
              + Vt6[num]*np.sin(12*np.pi*tt/T[num]+Vtgamma6[num])
             )  
    RMSE=np.sqrt(mean_squared_error(vtarge,vfourier))
    print(RMSE/umax[num])