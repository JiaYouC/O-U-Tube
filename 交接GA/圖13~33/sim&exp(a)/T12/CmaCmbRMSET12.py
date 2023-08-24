#!/usr/bin/env python
# coding: utf-8

#%%
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
@jit(nopython=True) 
def tfor(R0,R1,R2,R3,R4,R5,R6,T,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,Cma,Cmb):
    g=9.81
    Lb=7.5     #8.6計算到平壓塔中心
    La=18.35   #19.45計算到平壓塔中心
    d=np.sqrt(0.2)
    db=0.65
    A=0.2
    Ab=(db/2)**2*np.pi
    Aa=0.16
    Arev=1.21
    fa=0
    fb=0
    delt=0.01
    density=998
    viscosity=10**(-3)
    rough=0
    n=7
    alpha=30.643
    ka=39#40 #170  
    kb=3.5
    t=0
    te=300005
    Qa0=0
    Qb0=0
    Qa=[]
    zx0=0
    zy0=0
    for i in np.arange(0,te):
        time=delt*i
        
        wrpm = (  R0 
                + R1*np.sin( 2*np.pi*time/T+gamma1)
                + R2*np.sin( 4*np.pi*time/T+gamma2)
                + R3*np.sin( 6*np.pi*time/T+gamma3)
                + R4*np.sin( 8*np.pi*time/T+gamma4)
                + R5*np.sin(10*np.pi*time/T+gamma5)
                + R6*np.sin(12*np.pi*time/T+gamma6)
               )  
        Fpump=np.abs(wrpm)*wrpm/alpha
        fa=0
        Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
        Qa.append(Qa0)
        fb=0  
        Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
        zx0=(Qa0-Qb0)*delt/Arev+zx0
        zy0=(Qb0-Qa0)*delt/Arev+zy0
    return Qa

#%%

order=6

with open('openRparameter2.csv' , 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
csv_file.close() 
del list_of_rows[0]
text=np.asarray([x[0] for x in list_of_rows])
T=np.asarray([x[1] for x in list_of_rows],dtype=float)
R0=np.asarray([x[2] for x in list_of_rows],dtype=float)
R1=np.asarray([x[3] for x in list_of_rows],dtype=float)
R2=np.asarray([x[4] for x in list_of_rows],dtype=float)
R3=np.asarray([x[5] for x in list_of_rows],dtype=float)
R4=np.asarray([x[6] for x in list_of_rows],dtype=float)
R5=np.asarray([x[7] for x in list_of_rows],dtype=float)
R6=np.asarray([x[8] for x in list_of_rows],dtype=float)

gamma1=np.asarray([x[9] for x in list_of_rows],dtype=float)
gamma2=np.asarray([x[10] for x in list_of_rows],dtype=float)
gamma3=np.asarray([x[11] for x in list_of_rows],dtype=float)
gamma4=np.asarray([x[12] for x in list_of_rows],dtype=float)
gamma5=np.asarray([x[13] for x in list_of_rows],dtype=float)
gamma6=np.asarray([x[14] for x in list_of_rows],dtype=float)



with open('T6912.csv' , 'r') as csv_file:
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

if order==6:
    Vgamma1=np.asarray([x[9] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[10] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[11] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[12] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[14] for x in list_of_rows],dtype=float)
    
if order==7:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[10] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[11] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[12] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[16] for x in list_of_rows],dtype=float)
    
    
if order==8:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    V8=np.asarray([x[10] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[11] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[12] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[16] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[17] for x in list_of_rows],dtype=float)
    Vgamma8=np.asarray([x[18] for x in list_of_rows],dtype=float)
    
if order==9:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    V8=np.asarray([x[10] for x in list_of_rows],dtype=float)
    V9=np.asarray([x[11] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[12] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[16] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[17] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[18] for x in list_of_rows],dtype=float)
    Vgamma8=np.asarray([x[19] for x in list_of_rows],dtype=float)
    Vgamma9=np.asarray([x[20] for x in list_of_rows],dtype=float)
    
       
if order==10:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    V8=np.asarray([x[10] for x in list_of_rows],dtype=float)
    V9=np.asarray([x[11] for x in list_of_rows],dtype=float)
    V10=np.asarray([x[12] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[16] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[17] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[18] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[19] for x in list_of_rows],dtype=float)
    Vgamma8=np.asarray([x[20] for x in list_of_rows],dtype=float)
    Vgamma9=np.asarray([x[21] for x in list_of_rows],dtype=float)
    Vgamma10=np.asarray([x[22] for x in list_of_rows],dtype=float)
    
        
if order==11:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    V8=np.asarray([x[10] for x in list_of_rows],dtype=float)
    V9=np.asarray([x[11] for x in list_of_rows],dtype=float)
    V10=np.asarray([x[12] for x in list_of_rows],dtype=float)
    V11=np.asarray([x[13] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[16] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[17] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[18] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[19] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[20] for x in list_of_rows],dtype=float)
    Vgamma8=np.asarray([x[21] for x in list_of_rows],dtype=float)
    Vgamma9=np.asarray([x[22] for x in list_of_rows],dtype=float)
    Vgamma10=np.asarray([x[23] for x in list_of_rows],dtype=float)
    Vgamma11=np.asarray([x[24] for x in list_of_rows],dtype=float)
    
    
if order==12:
    V7=np.asarray([x[9] for x in list_of_rows],dtype=float)
    V8=np.asarray([x[10] for x in list_of_rows],dtype=float)
    V9=np.asarray([x[11] for x in list_of_rows],dtype=float)
    V10=np.asarray([x[12] for x in list_of_rows],dtype=float)
    V11=np.asarray([x[13] for x in list_of_rows],dtype=float)
    V12=np.asarray([x[14] for x in list_of_rows],dtype=float)
    Vgamma1=np.asarray([x[15] for x in list_of_rows],dtype=float)
    Vgamma2=np.asarray([x[16] for x in list_of_rows],dtype=float)
    Vgamma3=np.asarray([x[17] for x in list_of_rows],dtype=float)
    Vgamma4=np.asarray([x[18] for x in list_of_rows],dtype=float)
    Vgamma5=np.asarray([x[19] for x in list_of_rows],dtype=float)
    Vgamma6=np.asarray([x[20] for x in list_of_rows],dtype=float)
    Vgamma7=np.asarray([x[21] for x in list_of_rows],dtype=float)
    Vgamma8=np.asarray([x[22] for x in list_of_rows],dtype=float)
    Vgamma9=np.asarray([x[23] for x in list_of_rows],dtype=float)
    Vgamma10=np.asarray([x[24] for x in list_of_rows],dtype=float)
    Vgamma11=np.asarray([x[25] for x in list_of_rows],dtype=float)
    Vgamma12=np.asarray([x[26] for x in list_of_rows],dtype=float)
#%%

g=9.81
Lb=7.5     #8.6計算到平壓塔中心
La=18.35   #19.45計算到平壓塔中心
d=np.sqrt(0.2)
db=0.65
A=0.2
Ab=(db/2)**2*np.pi
Aa=0.16
Arev=1.21
fa=0
fb=0
delt=0.01
density=998
viscosity=10**(-3)
rough=0
n=7
Cma=1.92#1.65#1.85
Cmb=0.18#0.3#0.15
alpha=30.643
ka=39#40 #170  
kb=3.5

#0.86
#u/Vc=(1-r/R)**(1/n)

with open('CmaCmbT12GPU.csv' , 'w',encoding='utf-8') as res:
      for Cmaa in trange(0,302,2):
        #res.write(text[num]+'\n')
        for Cmbb in range(0,302,2):
            Cma=Cmaa/100
            Cmb=Cmbb/100
            res.write('%.2f,'%Cma)
            res.write('%.2f,'%Cmb)
            for num in range(15,len(gamma6)):#6,9):#      #len(gamma6)-7
                Qa=np.asarray(tfor(R0[num],R1[num],R2[num],R3[num],R4[num],R5[num],R6[num],T[num],gamma1[num],gamma2[num],gamma3[num],gamma4[num],gamma5[num],gamma6[num],Cma,Cmb))
                                
                tst=T[num]*240
                tend=T[num]*241
                
                #Qa=np.asarray(Qa)
                avg_va=Qa/Aa*100  #(m to cm)
                
                va_max=avg_va/0.86#(n+1)*(2*n+1)/(2*n**2)#avg_va
                
                
                count=int(tst/delt)
               
                cnt=0
                while cnt!=-1:
                      if(va_max[count]<0):
                          if(va_max[count+1]>0):
                              cnt=-1
                      count =  count + 1    
                
                            
                velocity=va_max[count:count+int(T[num]/delt)+1]
                t=np.arange(0,2*T[num]+delt,delt)
                
                vfourier=(  
                            V0[num] 
                          + V1[num]*np.sin( 2*np.pi*t/T[num]+Vgamma1[num])
                          + V2[num]*np.sin( 4*np.pi*t/T[num]+Vgamma2[num])
                          + V3[num]*np.sin( 6*np.pi*t/T[num]+Vgamma3[num])
                          + V4[num]*np.sin( 8*np.pi*t/T[num]+Vgamma4[num])
                          + V5[num]*np.sin(10*np.pi*t/T[num]+Vgamma5[num])
                          + V6[num]*np.sin(12*np.pi*t/T[num]+Vgamma6[num])
                         )
                if order > 6:
                    vfourier=vfourier+V7*np.sin(2*7*np.pi*t/T[num]+Vgamma7[num])
                    if order > 7:
                        vfourier=vfourier+V8*np.sin(2*8*np.pi*t/T[num]+Vgamma8[num])
                        if order > 8:
                            vfourier=vfourier+V9*np.sin(2*9*np.pi*t/T[num]+Vgamma9[num])
                            if order > 9:
                                vfourier=vfourier+V10*np.sin(2*10*np.pi*t/T[num]+Vgamma10[num])
                                if order > 10:
                                    vfourier=vfourier+V11*np.sin(2*11*np.pi*t/T[num]+Vgamma11[num])
                                    if order > 11:
                                        vfourier=vfourier+V12*np.sin(2*12*np.pi*t/T[num]+Vgamma12[num])  
                count=0
                cnt=0  
                while cnt!=-1:
                      if(vfourier[count]<0):
                          if(vfourier[count+1]>0):
                              cnt=-1
                      count =  count + 1 
                
                t=np.arange(count,count+T[num]*100+1,1)
                t=t/100
                vfourier=(  
                            V0[num] 
                          + V1[num]*np.sin( 2*np.pi*t/T[num]+Vgamma1[num])
                          + V2[num]*np.sin( 4*np.pi*t/T[num]+Vgamma2[num])
                          + V3[num]*np.sin( 6*np.pi*t/T[num]+Vgamma3[num])
                          + V4[num]*np.sin( 8*np.pi*t/T[num]+Vgamma4[num])
                          + V5[num]*np.sin(10*np.pi*t/T[num]+Vgamma5[num])
                          + V6[num]*np.sin(12*np.pi*t/T[num]+Vgamma6[num])
                         )
                if order > 6:
                    vfourier=vfourier+V7*np.sin(2*7*np.pi*t/T[num]+Vgamma7[num])
                    if order > 7:
                        vfourier=vfourier+V8*np.sin(2*8*np.pi*t/T[num]+Vgamma8[num])
                        if order > 8:
                            vfourier=vfourier+V9*np.sin(2*9*np.pi*t/T[num]+Vgamma9[num])
                            if order > 9:
                                vfourier=vfourier+V10*np.sin(2*10*np.pi*t/T[num]+Vgamma10[num])
                                if order > 10:
                                    vfourier=vfourier+V11*np.sin(2*11*np.pi*t/T[num]+Vgamma11[num])
                                    if order > 11:
                                        vfourier=vfourier+V12*np.sin(2*12*np.pi*t/T[num]+Vgamma12[num]) 
                
               
                t=np.arange(0,T[num]+delt,delt)
                RMSE=np.sqrt(mean_squared_error(velocity,vfourier))
                bbb=RMSE/max(vfourier)
                #res.write('%.4f,'%RMSE)
                res.write('%.4f,'%bbb)
            res.write('\n')