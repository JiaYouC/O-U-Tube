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
             )/((num+1)*20)
           
    
    tt=np.arange(0,T[num]+0.01,0.01)
    if num ==0:
        function=20*np.sin(2*np.pi*ttt/T[num])#109*np.sin(2*np.pi*ttt/T[num])+109/4*np.sin(4*np.pi*ttt/T[num])
        count=0
        cnt=0  
        while cnt!=-1:
              if(function[count]<0):
                  if(function[count+1]>0):
                      cnt=-1
              count =  count + 1
        tf=np.arange(count,count+T[num]*100+1,1)
        tf=tf/100
        function=(20*np.sin(2*np.pi*tf/T[num]))/20#(109*np.sin(2*np.pi*tf/T[num])+109/4*np.sin(4*np.pi*tf/T[num]))/120 
        array_all = np.hstack((tt,function,vfourier))
    if num!=0:
        array_all = np.hstack((array_all,vfourier))
a=array_all.reshape(len(T)+2,-1).T
np.savetxt("sin_vesuz.csv",a, delimiter=',',fmt='%1.12f')