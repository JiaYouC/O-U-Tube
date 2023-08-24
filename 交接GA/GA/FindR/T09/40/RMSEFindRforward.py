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
import numba 
from numba import jit
order=6
if order==6:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6):
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
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6,gamma1, gamma2, gamma3, gamma4, gamma5, gamma6):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6,gamma1, gamma2, gamma3, gamma4, gamma5, gamma6))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
    
        return RMSE

if order==7:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
    
        return RMSE

if order==8:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,R8,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                    + R8*np.sin(16*np.pi*time/T+gamma8)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,R8,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,R8,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
    
        return RMSE

if order==9:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                    + R8*np.sin(16*np.pi*time/T+gamma8)
                    + R9*np.sin(18*np.pi*time/T+gamma9)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
    
        return RMSE

if order==10:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                    + R8*np.sin(16*np.pi*time/T+gamma8)
                    + R9*np.sin(18*np.pi*time/T+gamma9)
                    + R10*np.sin(20*np.pi*time/T+gamma10)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
        return RMSE
    
if order==11:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                    + R8*np.sin(16*np.pi*time/T+gamma8)
                    + R9*np.sin(18*np.pi*time/T+gamma9)
                    + R10*np.sin(20*np.pi*time/T+gamma10)
                    + R11*np.sin(22*np.pi*time/T+gamma11)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,R11,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,R11,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
        return RMSE

if order==12:
    @jit(nopython=True) 
    def tfor(T,Cma,Cmb,R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11,gamma12):
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
                    + R7*np.sin(14*np.pi*time/T+gamma7)
                    + R8*np.sin(16*np.pi*time/T+gamma8)
                    + R9*np.sin(18*np.pi*time/T+gamma9)
                    + R10*np.sin(20*np.pi*time/T+gamma10)
                    + R11*np.sin(22*np.pi*time/T+gamma11)
                    + R12*np.sin(24*np.pi*time/T+gamma12)
                   )  
            #Fpump=np.abs(wrpm)*wrpm/alpha
            Fpump=wrpm/alpha
            fa=0
            Qa0=Qa0+delt*(Fpump+density*g*Ab*(zy0-zx0)-density*((fa*La)/d+ka)*Qa0*abs(Qa0)/(A*2))/((1+Cma)*density*La)
            Qa.append(Qa0)
            fb=0  
            Qb0=Qb0+delt*((density*g*Ab*(zx0-zy0)-density*((fb*Lb)/db+kb)*Qb0*abs(Qb0)/(Ab*2))/((1+Cmb)*density*Lb)) 
            zx0=(Qa0-Qb0)*delt/Arev+zx0
            zy0=(Qb0-Qa0)*delt/Arev+zy0
        return Qa
    
    def TunnelSimulation(R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,R11,R12,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11,gamma12):
        
        
        with open('U_sin.csv' , 'r') as csv_file:
                csv_reader = reader(csv_file)
                # Passing the cav_reader object to list() to get a list of lists
                list_of_rows = list(csv_reader)
        csv_file.close() 
        del list_of_rows[0]
        T0=np.asarray([x[0] for x in list_of_rows],dtype=float)
        U0=np.asarray([x[1] for x in list_of_rows],dtype=float)
        Cma0=np.asarray([x[2] for x in list_of_rows],dtype=float)
        Cmb0=np.asarray([x[3] for x in list_of_rows],dtype=float)
        
        T=T0[1]
        Cma=Cma0[1]
        Cmb=Cmb0[1]
        
        
        delt=0.01
        At=0.16
        Qa=np.asarray(tfor(T,Cma,Cmb,R0, R1, R2, R3, R4, R5, R6, R7,R8,R9,R10,R11,R12,gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11,gamma12))
        tst=T*240
        tend=T*241
        t=np.linspace(0,T,int((tend-tst)/delt)+1)  
        Qa=np.asarray(Qa)
        avg_va=Qa/At*100  #(m to cm)
        #u/Vc=(1-r/R)**(1/n)  Vc=u*(n+1)(2*n+1)/2*n**2 n=7 Vc=
        va_max=avg_va/0.86# *(n+1)*(2*n+1)/(2*n**2)
            
        count=int(tst/delt)
    
        cnt=0
        while cnt!=-1:
              if(va_max[count]<0):
                  if(va_max[count+1]>0):
                      cnt=-1
              count =  count + 1       
        
        velocity=va_max[count:count+int(T/delt)+1]
        U=U0[1]
        ttt=np.linspace(0,3*T,3*int((tend-tst)/delt)+1) 
        vfourier = (  
                        U*np.sin(2*np.pi*ttt/T)+U/4*np.sin(4*np.pi*ttt/T)
                   )
        cnt=0
        count=0
        while cnt!=-1:
              if(vfourier[count]<0):
                  if(vfourier[count+1]>0):
                      cnt=-1
              count =  count + 1 
        vfourier_used=vfourier[count:count+int(T/delt)+1]      
    #    plt.plot(t,vfourier,'r',label='exp.')
    
        RMSE=np.sqrt(mean_squared_error(velocity,vfourier_used))
    
        return RMSE