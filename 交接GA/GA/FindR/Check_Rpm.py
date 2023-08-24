# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
from tqdm import trange
from csv import reader
order=6

with open('./GA_checkR.csv', 'w', encoding='utf-8') as res:
    res.write('T0')
    res.write(',R0,')
    res.write(','.join(['R'+str(i) for i in range(1, order+1)]))
    res.write(',')
    res.write(','.join(['phi'+str(i) for i in range(1, order+1)]))
    res.write('\n')
res.close() 
#%%
for i in range(0,3,1):
    if int(i)==0:
        path='T06/'
    if int(i)==1:
        path='T09/'
    if int(i)==2:
        path='T12/'
    for k in range(0,3,1):
        for j in range(20,180,20):
            if int(k)==0:
                with open(path+str(int(j))+'/GA_findR/GA_R_sin.csv' , 'r') as csv_file:
                    csv_reader = reader(csv_file)
                    # Passing the cav_reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                csv_file.close() 
            if int(k)==1:
                with open(path+str(int(j))+'/GA_findR/GA_R_forward.csv' , 'r') as csv_file:
                    csv_reader = reader(csv_file)
                    # Passing the cav_reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                csv_file.close() 
            if int(k)==2:
                with open(path+str(int(j))+'/GA_findR/GA_R_stoke.csv' , 'r') as csv_file:
                    csv_reader = reader(csv_file)
                    # Passing the cav_reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                csv_file.close() 
            del list_of_rows[0]
            solutions = []
            TTT=np.asarray([x[0] for x in list_of_rows],dtype=float)
            R0=np.asarray([x[1] for x in list_of_rows],dtype=float)
            R1=np.asarray([x[2] for x in list_of_rows],dtype=float)
            R2=np.asarray([x[3] for x in list_of_rows],dtype=float)
            R3=np.asarray([x[4] for x in list_of_rows],dtype=float)
            R4=np.asarray([x[5] for x in list_of_rows],dtype=float)
            R5=np.asarray([x[6] for x in list_of_rows],dtype=float)
            R6=np.asarray([x[7] for x in list_of_rows],dtype=float)
            
            T=TTT[0]
            R0=R0[0]
            R1=R1[0]
            R2=R2[0]
            R3=R3[0]
            R4=R4[0]
            R5=R5[0]
            R6=R6[0]
            if order==6:
                phi1=np.asarray([x[8] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[9] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[10] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[11] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[13] for x in list_of_rows],dtype=float)
                
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                
            if order==7:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[9] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[10] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[11] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[15] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                
                
            if order==8:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                R8=np.asarray([x[9] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[10] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[11] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[15] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[16] for x in list_of_rows],dtype=float)
                phi8=np.asarray([x[17] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                R8=R8[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                phi8=phi8[0]
                
            if order==9:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                R8=np.asarray([x[9] for x in list_of_rows],dtype=float)
                R9=np.asarray([x[10] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[11] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[15] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[16] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[17] for x in list_of_rows],dtype=float)
                phi8=np.asarray([x[18] for x in list_of_rows],dtype=float)
                phi9=np.asarray([x[19] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                R8=R8[0]
                R9=R9[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                phi8=phi8[0]
                phi9=phi9[0]
                
                
            if order==10:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                R8=np.asarray([x[9] for x in list_of_rows],dtype=float)
                R9=np.asarray([x[10] for x in list_of_rows],dtype=float)
                R10=np.asarray([x[11] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[15] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[16] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[17] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[18] for x in list_of_rows],dtype=float)
                phi8=np.asarray([x[19] for x in list_of_rows],dtype=float)
                phi9=np.asarray([x[20] for x in list_of_rows],dtype=float)
                phi10=np.asarray([x[21] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                R8=R8[0]
                R9=R9[0]
                R10=R10[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                phi8=phi8[0]
                phi9=phi9[0]
                phi10=phi10[0]
                    
            if order==11:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                R8=np.asarray([x[9] for x in list_of_rows],dtype=float)
                R9=np.asarray([x[10] for x in list_of_rows],dtype=float)
                R10=np.asarray([x[11] for x in list_of_rows],dtype=float)
                R11=np.asarray([x[12] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[15] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[16] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[17] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[18] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[19] for x in list_of_rows],dtype=float)
                phi8=np.asarray([x[20] for x in list_of_rows],dtype=float)
                phi9=np.asarray([x[21] for x in list_of_rows],dtype=float)
                phi10=np.asarray([x[22] for x in list_of_rows],dtype=float)
                phi11=np.asarray([x[23] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                R8=R8[0]
                R9=R9[0]
                R10=R10[0]
                R11=R11[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                phi8=phi8[0]
                phi9=phi9[0]
                phi10=phi10[0]
                phi11=phi11[0]
                
                
            if order==12:
                R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
                R8=np.asarray([x[9] for x in list_of_rows],dtype=float)
                R9=np.asarray([x[10] for x in list_of_rows],dtype=float)
                R10=np.asarray([x[11] for x in list_of_rows],dtype=float)
                R11=np.asarray([x[12] for x in list_of_rows],dtype=float)
                R12=np.asarray([x[13] for x in list_of_rows],dtype=float)
                phi1=np.asarray([x[14] for x in list_of_rows],dtype=float)
                phi2=np.asarray([x[15] for x in list_of_rows],dtype=float)
                phi3=np.asarray([x[16] for x in list_of_rows],dtype=float)
                phi4=np.asarray([x[17] for x in list_of_rows],dtype=float)
                phi5=np.asarray([x[18] for x in list_of_rows],dtype=float)
                phi6=np.asarray([x[19] for x in list_of_rows],dtype=float)
                phi7=np.asarray([x[20] for x in list_of_rows],dtype=float)
                phi8=np.asarray([x[21] for x in list_of_rows],dtype=float)
                phi9=np.asarray([x[22] for x in list_of_rows],dtype=float)
                phi10=np.asarray([x[23] for x in list_of_rows],dtype=float)
                phi11=np.asarray([x[24] for x in list_of_rows],dtype=float)
                phi12=np.asarray([x[25] for x in list_of_rows],dtype=float)
                
                R7=R7[0]
                R8=R8[0]
                R9=R9[0]
                R10=R10[0]
                R11=R11[0]
                R12=R12[0]
                phi1=phi1[0]
                phi2=phi2[0]
                phi3=phi3[0]
                phi4=phi4[0]
                phi5=phi5[0]
                phi6=phi6[0]
                phi7=phi7[0]
                phi8=phi8[0]
                phi9=phi9[0]
                phi10=phi10[0]
                phi11=phi11[0]
                phi12=phi12[0]
#%%
            t=np.arange(0,2*T+0.01,0.01)
            funnn=(R0+R1*np.sin(2*1*np.pi*t/T+phi1)+R2*np.sin(2*2*np.pi*t/T+phi2)+R3*np.sin(2*3*np.pi*t/T+phi3)+R4*np.sin(2*4*np.pi*t/T+phi4)+R5*np.sin(2*5*np.pi*t/T+phi5)+R6*np.sin(2*6*np.pi*t/T+phi6))
            if order > 6:
                funnn=funnn+R7*np.sin(2*7*np.pi*t/T+phi7)
                if order > 7:
                    funnn=funnn+R8*np.sin(2*8*np.pi*t/T+phi8)
                    if order > 8:
                        funnn=funnn+R9*np.sin(2*9*np.pi*t/T+phi9)
                        if order > 9:
                            funnn=funnn+R10*np.sin(2*10*np.pi*t/T+phi10)
                            if order > 10:
                                funnn=funnn+R11*np.sin(2*11*np.pi*t/T+phi11)
                                if order > 11:
                                    funnn=funnn+R12*np.sin(2*12*np.pi*t/T+phi12)  
            with open('./GA_checkR.csv', 'a', encoding='utf-8') as res:
                if max(funnn/np.sqrt(abs(funnn)))>=1000:
                    res.write('ERROR'+'\n')
                if max(funnn/np.sqrt(abs(funnn)))<1000:
                    if order == 12:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','+str(R8)+','+str(R9)+','+str(R10)+','+str(R11)+','+str(R12)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)+','+str(phi8)+','+str(phi9)+','+str(phi10)+','+str(phi11)+','+str(phi12)
                                  +'\n')
                    if order == 11:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','+str(R8)+','+str(R9)+','+str(R10)+','+str(R11)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)+','+str(phi8)+','+str(phi9)+','+str(phi10)+','+str(phi11)
                                  +'\n')
                    if order == 10:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','+str(R8)+','+str(R9)+','+str(R10)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)+','+str(phi8)+','+str(phi9)+','+str(phi10)
                                  +'\n')
                    if order == 9:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','+str(R8)+','+str(R9)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)+','+str(phi8)+','+str(phi9)
                                  +'\n')
                    if order == 8:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','+str(R8)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)+','+str(phi8)
                                  +'\n')
                    if order == 7:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(R7)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +str(phi7)
                                  +'\n')
                    if order == 6:
                        res.write(str(T)+','+str(R0)+','
                                  +str(R1)+','+str(R2)+','+str(R3)+','+str(R4)+','+str(R5)+','+str(R6)+','
                                  +str(phi1)+','+str(phi2)+','+str(phi3)+','+str(phi4)+','+str(phi5)+','+str(phi6)+','
                                  +'\n')
            res.close()
