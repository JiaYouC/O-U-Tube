# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:09:45 2023

@author: user
"""

import numpy as np
import random
import RMSEFindRsin as F
from tqdm import trange
from csv import reader

coP = 1.
mP  = 0.4
MGenration =60
Sample =32
order=6
#%%
def fitness(solution):
    if order==6:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12])
    if order==7:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12], solution[13],solution[14])
    if order==8:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12], solution[13],solution[14]
                                  , solution[15],solution[16])
    if order==9:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12], solution[13],solution[14]
                                  ,solution[15],solution[16],solution[17]
                                  ,solution[18])
    if order==10:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12],solution[13],solution[14]
                                  ,solution[15],solution[16],solution[17]
                                  ,solution[18],solution[19],solution[20])
    if order==11:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12],solution[13],solution[14]
                                  ,solution[15],solution[16],solution[17]
                                  ,solution[18],solution[19],solution[20]
                                  ,solution[21],solution[22])
    if order==12:
        Error = F.TunnelSimulation(solution[0],solution[1], solution[2], 
                                  solution[3],solution[4], solution[5], 
                                  solution[6],solution[7], solution[8], 
                                  solution[9],solution[10], solution[11], 
                                  solution[12],solution[13],solution[14]
                                  ,solution[15],solution[16],solution[17]
                                  ,solution[18],solution[19],solution[20]
                                  ,solution[21],solution[22],solution[23]
                                  ,solution[24])
    
    fitness = 1./Error
    return fitness
#%%
with open('R_sin_parameter.csv' , 'r') as csv_file:
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
if order==6:
    phi1=np.asarray([x[8] for x in list_of_rows],dtype=float)
    phi2=np.asarray([x[9] for x in list_of_rows],dtype=float)
    phi3=np.asarray([x[10] for x in list_of_rows],dtype=float)
    phi4=np.asarray([x[11] for x in list_of_rows],dtype=float)
    phi5=np.asarray([x[12] for x in list_of_rows],dtype=float)
    phi6=np.asarray([x[13] for x in list_of_rows],dtype=float)
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]])
                             ])
if order==7:
    R7=np.asarray([x[8] for x in list_of_rows],dtype=float)
    phi1=np.asarray([x[9] for x in list_of_rows],dtype=float)
    phi2=np.asarray([x[10] for x in list_of_rows],dtype=float)
    phi3=np.asarray([x[11] for x in list_of_rows],dtype=float)
    phi4=np.asarray([x[12] for x in list_of_rows],dtype=float)
    phi5=np.asarray([x[13] for x in list_of_rows],dtype=float)
    phi6=np.asarray([x[14] for x in list_of_rows],dtype=float)
    phi7=np.asarray([x[15] for x in list_of_rows],dtype=float)
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]])
                             ])
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
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],R8[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0],phi8[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([R8[1],R8[2],R8[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]]),
                              random.choice([phi8[1],phi8[2],phi8[3]])
                             ])
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
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],R8[0],R9[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0],phi8[0],phi9[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([R8[1],R8[2],R8[3]]),
                              random.choice([R9[1],R9[2],R9[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]]),
                              random.choice([phi8[1],phi8[2],phi8[3]]),
                              random.choice([phi9[1],phi9[2],phi9[3]])
                             ])
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
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],R8[0],R9[0],R10[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0],phi8[0],phi9[0],phi10[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([R8[1],R8[2],R8[3]]),
                              random.choice([R9[1],R9[2],R9[3]]),
                              random.choice([R10[1],R10[2],R10[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]]),
                              random.choice([phi8[1],phi8[2],phi8[3]]),
                              random.choice([phi9[1],phi9[2],phi9[3]]),
                              random.choice([phi10[1],phi10[2],phi10[3]])
                             ])
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
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],R8[0],R9[0],R10[0],R11[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0],phi8[0],phi9[0],phi10[0],phi10[0],phi11[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([R8[1],R8[2],R8[3]]),
                              random.choice([R9[1],R9[2],R9[3]]),
                              random.choice([R10[1],R10[2],R10[3]]),
                              random.choice([R11[1],R11[2],R11[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]]),
                              random.choice([phi8[1],phi8[2],phi8[3]]),
                              random.choice([phi9[1],phi9[2],phi9[3]]),
                              random.choice([phi10[1],phi10[2],phi10[3]]),
                              random.choice([phi11[1],phi11[2],phi11[3]])
                             ])
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
    solutions.append([R0[0],R1[0],R2[0],R3[0],R4[0],R5[0],R6[0],R7[0],R8[0],R9[0],R10[0],R11[0],R12[0],phi1[0],phi2[0],phi3[0],phi4[0],phi5[0],phi6[0],phi7[0],phi8[0],phi9[0],phi10[0],phi10[0],phi11[0],phi12[0]])
    for s in range(int(Sample)):
            solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                              random.choice([R1[1],R1[2],R1[3]]),
                              random.choice([R2[1],R2[2],R2[3]]),
                              random.choice([R3[1],R3[2],R3[3]]),
                              random.choice([R4[1],R4[2],R4[3]]),
                              random.choice([R5[1],R5[2],R5[3]]),
                              random.choice([R6[1],R6[2],R6[3]]),
                              random.choice([R7[1],R7[2],R7[3]]),
                              random.choice([R8[1],R8[2],R8[3]]),
                              random.choice([R9[1],R9[2],R9[3]]),
                              random.choice([R10[1],R10[2],R10[3]]),
                              random.choice([R11[1],R11[2],R11[3]]),
                              random.choice([R12[1],R12[2],R12[3]]),
                              random.choice([phi1[1],phi1[2],phi1[3]]),
                              random.choice([phi2[1],phi2[2],phi2[3]]),
                              random.choice([phi3[1],phi3[2],phi3[3]]),
                              random.choice([phi4[1],phi4[2],phi4[3]]),
                              random.choice([phi5[1],phi5[2],phi5[3]]),
                              random.choice([phi6[1],phi6[2],phi6[3]]),
                              random.choice([phi7[1],phi7[2],phi7[3]]),
                              random.choice([phi8[1],phi8[2],phi8[3]]),
                              random.choice([phi9[1],phi9[2],phi9[3]]),
                              random.choice([phi10[1],phi10[2],phi10[3]]),
                              random.choice([phi11[1],phi11[2],phi11[3]]),
                              random.choice([phi12[1],phi12[2],phi12[3]])
                             ])

#%%    
for jjj in range(0,3000,1):
    rankedsolutions = []

    for i in trange(MGenration):

        for s in solutions:
                rankedsolutions.append((fitness(s),s))
        rankedsolutions.sort()
        rankedsolutions.reverse()
        del rankedsolutions[Sample:]    
        #print(rankedsolutions)
        if i%5==0:
            print(f"=====GEN {i} best solutions ====")
            print(rankedsolutions[0])

        if rankedsolutions[0][0] >10000:
            break

        newGen = []
        for _ in range(int(Sample/2)):

            indexM = random.randint(0, int(Sample)-1)
            indexM = min(indexM,random.randint(0, int(Sample)))
            indexM = min(indexM,random.randint(0, int(Sample))) 
            indexF = random.randint(0, int(Sample)-1)
            indexF = min(indexF,random.randint(0, int(Sample)))
            indexF = min(indexF,random.randint(0, int(Sample)))

            r = random.uniform(0.00,1.00)
            if r <coP:
                weight =  [random.uniform(0.,1.) for _ in range(int(order*2)+1)]
            else:
                weight =  [1. for _ in range(int(order*2)+1)]

            e10 = rankedsolutions[indexM][1][0]*weight[0] + rankedsolutions[indexF][1][0]*(1-weight[0])
            e20 = rankedsolutions[indexF][1][0]*weight[0] + rankedsolutions[indexM][1][0]*(1-weight[0])

            e11 = rankedsolutions[indexM][1][1]*weight[1] + rankedsolutions[indexF][1][1]*(1-weight[1])
            e21 = rankedsolutions[indexF][1][1]*weight[1] + rankedsolutions[indexM][1][1]*(1-weight[1])

            e12 = rankedsolutions[indexM][1][2]*weight[2] + rankedsolutions[indexF][1][2]*(1-weight[2])
            e22 = rankedsolutions[indexF][1][2]*weight[2] + rankedsolutions[indexM][1][2]*(1-weight[2])

            e13 = rankedsolutions[indexM][1][3]*weight[3] + rankedsolutions[indexF][1][3]*(1-weight[3])
            e23 = rankedsolutions[indexF][1][3]*weight[3] + rankedsolutions[indexM][1][3]*(1-weight[3])

            e14 = rankedsolutions[indexM][1][4]*weight[4] + rankedsolutions[indexF][1][4]*(1-weight[4])
            e24 = rankedsolutions[indexF][1][4]*weight[4] + rankedsolutions[indexM][1][4]*(1-weight[4])

            e15 = rankedsolutions[indexM][1][5]*weight[5] + rankedsolutions[indexF][1][5]*(1-weight[5])
            e25 = rankedsolutions[indexF][1][5]*weight[5] + rankedsolutions[indexM][1][5]*(1-weight[5])

            e16 = rankedsolutions[indexM][1][6]*weight[6] + rankedsolutions[indexF][1][6]*(1-weight[6])
            e26 = rankedsolutions[indexF][1][6]*weight[6] + rankedsolutions[indexM][1][6]*(1-weight[6])

            e17 = rankedsolutions[indexM][1][7]*weight[7] + rankedsolutions[indexF][1][7]*(1-weight[7])
            e27 = rankedsolutions[indexF][1][7]*weight[7] + rankedsolutions[indexM][1][7]*(1-weight[7])

            e18 = rankedsolutions[indexM][1][8]*weight[8] + rankedsolutions[indexF][1][8]*(1-weight[8])
            e28 = rankedsolutions[indexF][1][8]*weight[8] + rankedsolutions[indexM][1][8]*(1-weight[8])

            e19 = rankedsolutions[indexM][1][9]*weight[9] + rankedsolutions[indexF][1][9]*(1-weight[9])
            e29 = rankedsolutions[indexF][1][9]*weight[9] + rankedsolutions[indexM][1][9]*(1-weight[9])

            e110 = rankedsolutions[indexM][1][10]*weight[10] + rankedsolutions[indexF][1][10]*(1-weight[10])
            e210 = rankedsolutions[indexF][1][10]*weight[10] + rankedsolutions[indexM][1][10]*(1-weight[10])

            e111 = rankedsolutions[indexM][1][11]*weight[11] + rankedsolutions[indexF][1][11]*(1-weight[11])
            e211 = rankedsolutions[indexF][1][11]*weight[11] + rankedsolutions[indexM][1][11]*(1-weight[11])

            e112 = rankedsolutions[indexM][1][12]*weight[12] + rankedsolutions[indexF][1][12]*(1-weight[12])
            e212 = rankedsolutions[indexF][1][12]*weight[12] + rankedsolutions[indexM][1][12]*(1-weight[12])

            if order>6:
                e113 = rankedsolutions[indexM][1][13]*weight[13] + rankedsolutions[indexF][1][13]*(1-weight[13])
                e213 = rankedsolutions[indexF][1][13]*weight[13] + rankedsolutions[indexM][1][13]*(1-weight[13])

                e114 = rankedsolutions[indexM][1][14]*weight[14] + rankedsolutions[indexF][1][14]*(1-weight[14])
                e214 = rankedsolutions[indexF][1][14]*weight[14] + rankedsolutions[indexM][1][14]*(1-weight[14])
                if order>7:
                    e115 = rankedsolutions[indexM][1][15]*weight[15] + rankedsolutions[indexF][1][15]*(1-weight[15])
                    e215 = rankedsolutions[indexF][1][15]*weight[15] + rankedsolutions[indexM][1][15]*(1-weight[15])

                    e116 = rankedsolutions[indexM][1][16]*weight[16] + rankedsolutions[indexF][1][16]*(1-weight[16])
                    e216 = rankedsolutions[indexF][1][16]*weight[16] + rankedsolutions[indexM][1][16]*(1-weight[16])
                    if order>8:
                        e117 = rankedsolutions[indexM][1][17]*weight[17] + rankedsolutions[indexF][1][17]*(1-weight[17])
                        e217 = rankedsolutions[indexF][1][17]*weight[17] + rankedsolutions[indexM][1][17]*(1-weight[17])

                        e118 = rankedsolutions[indexM][1][18]*weight[18] + rankedsolutions[indexF][1][18]*(1-weight[18])
                        e218 = rankedsolutions[indexF][1][18]*weight[18] + rankedsolutions[indexM][1][18]*(1-weight[18])
                        if order>9:
                            e119 = rankedsolutions[indexM][1][19]*weight[19] + rankedsolutions[indexF][1][19]*(1-weight[19])
                            e219 = rankedsolutions[indexF][1][19]*weight[19] + rankedsolutions[indexM][1][19]*(1-weight[19])

                            e120 = rankedsolutions[indexM][1][20]*weight[20] + rankedsolutions[indexF][1][20]*(1-weight[20])
                            e220 = rankedsolutions[indexF][1][20]*weight[20] + rankedsolutions[indexM][1][20]*(1-weight[20])
                            if order>10:
                                e121 = rankedsolutions[indexM][1][21]*weight[21] + rankedsolutions[indexF][1][21]*(1-weight[21])
                                e221 = rankedsolutions[indexF][1][21]*weight[21] + rankedsolutions[indexM][1][21]*(1-weight[21])

                                e122 = rankedsolutions[indexM][1][22]*weight[22] + rankedsolutions[indexF][1][22]*(1-weight[22])
                                e222 = rankedsolutions[indexF][1][22]*weight[22] + rankedsolutions[indexM][1][22]*(1-weight[22])
                                if order>11:
                                    e123 = rankedsolutions[indexM][1][23]*weight[23] + rankedsolutions[indexF][1][23]*(1-weight[23])
                                    e223 = rankedsolutions[indexF][1][23]*weight[23] + rankedsolutions[indexM][1][23]*(1-weight[23])

                                    e124 = rankedsolutions[indexM][1][24]*weight[24] + rankedsolutions[indexF][1][24]*(1-weight[24])
                                    e224 = rankedsolutions[indexF][1][24]*weight[24] + rankedsolutions[indexM][1][24]*(1-weight[24])
            if order==6:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212])
            if order==7:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214])
            if order==8:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114,e115,e116])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214,e215,e216])
            if order==9:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114,e115,e116,e117,e118])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214,e215,e216,e217,e218])
            if order==10:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114,e115,e116,e117,e118,e119,e120])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214,e215,e216,e217,e218,e219,e220])
            if order==11:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114,e115,e116,e117,e118,e119,e120,e121,e122])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214,e215,e216,e217,e218,e219,e220,e221,e222])
            if order==12:
                newGen.append([e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e110,e111,e112,e113,e114,e115,e116,e117,e118,e119,e120,e121,e122,e123,e124])
                newGen.append([e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e210,e211,e212,e213,e214,e215,e216,e217,e218,e219,e220,e221,e222,e223,e224])
        solutions = newGen

        beta = 0.5
        alpha = (1.- (i)/MGenration )**beta

        for ii in range(0,Sample-2):
            for j in range(0,int(order*2)+1):
                r = random.uniform(0.00,1.00)
                if r < mP:
                    maxG = np.max(np.array(solutions)[:,j])
                    minG = np.min(np.array(solutions)[:,j])
                    temp = random.uniform(minG,maxG)
                    if (temp<solutions[ii][j]):
                        solutions[ii][j] = minG+(temp-minG)**alpha*(solutions[ii][j]-minG)**(1-alpha)
                    else:
                        solutions[ii][j] = maxG-(maxG-temp)**alpha*(maxG-solutions[ii][j])**(1-alpha)

    solutions = []
    solutions.append(rankedsolutions[0][1])
    if order==6:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]])
                                 ])
    if order==7:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]])
                                 ])
    if order==8:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([R8[1],R8[2],R8[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]]),
                                  random.choice([phi8[1],phi8[2],phi8[3]])
                                 ])
    if order==9:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([R8[1],R8[2],R8[3]]),
                                  random.choice([R9[1],R9[2],R9[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]]),
                                  random.choice([phi8[1],phi8[2],phi8[3]]),
                                  random.choice([phi9[1],phi9[2],phi9[3]])
                                 ])
    if order==10:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([R8[1],R8[2],R8[3]]),
                                  random.choice([R9[1],R9[2],R9[3]]),
                                  random.choice([R10[1],R10[2],R10[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]]),
                                  random.choice([phi8[1],phi8[2],phi8[3]]),
                                  random.choice([phi9[1],phi9[2],phi9[3]]),
                                  random.choice([phi10[1],phi10[2],phi10[3]])
                                 ])
    if order==11:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([R8[1],R8[2],R8[3]]),
                                  random.choice([R9[1],R9[2],R9[3]]),
                                  random.choice([R10[1],R10[2],R10[3]]),
                                  random.choice([R11[1],R11[2],R11[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]]),
                                  random.choice([phi8[1],phi8[2],phi8[3]]),
                                  random.choice([phi9[1],phi9[2],phi9[3]]),
                                  random.choice([phi10[1],phi10[2],phi10[3]]),
                                  random.choice([phi11[1],phi11[2],phi11[3]])
                                 ])
    if order==12:
        for s in range(int(Sample)):
                solutions.append([random.choice([R0[1],R0[2],R0[3]]),
                                  random.choice([R1[1],R1[2],R1[3]]),
                                  random.choice([R2[1],R2[2],R2[3]]),
                                  random.choice([R3[1],R3[2],R3[3]]),
                                  random.choice([R4[1],R4[2],R4[3]]),
                                  random.choice([R5[1],R5[2],R5[3]]),
                                  random.choice([R6[1],R6[2],R6[3]]),
                                  random.choice([R7[1],R7[2],R7[3]]),
                                  random.choice([R8[1],R8[2],R8[3]]),
                                  random.choice([R9[1],R9[2],R9[3]]),
                                  random.choice([R10[1],R10[2],R10[3]]),
                                  random.choice([R11[1],R11[2],R11[3]]),
                                  random.choice([R12[1],R12[2],R12[3]]),
                                  random.choice([phi1[1],phi1[2],phi1[3]]),
                                  random.choice([phi2[1],phi2[2],phi2[3]]),
                                  random.choice([phi3[1],phi3[2],phi3[3]]),
                                  random.choice([phi4[1],phi4[2],phi4[3]]),
                                  random.choice([phi5[1],phi5[2],phi5[3]]),
                                  random.choice([phi6[1],phi6[2],phi6[3]]),
                                  random.choice([phi7[1],phi7[2],phi7[3]]),
                                  random.choice([phi8[1],phi8[2],phi8[3]]),
                                  random.choice([phi9[1],phi9[2],phi9[3]]),
                                  random.choice([phi10[1],phi10[2],phi10[3]]),
                                  random.choice([phi11[1],phi11[2],phi11[3]]),
                                  random.choice([phi12[1],phi12[2],phi12[3]])
                                 ])
                                 
    with open('./GA_findR/GA_R_sin.csv' ,'w') as res:
            res.write('T,')
            res.write('R0,')
            res.write('R1,')
            res.write('R2,')
            res.write('R3,')
            res.write('R4,')
            res.write('R5,')
            res.write('R6,')
            if order==6:
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
            if order==7:
                res.write('R7,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
            if order==8:
                res.write('R7,')
                res.write('R8,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7,')
                res.write('phi8\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
                res.write('%.3f,'%rankedsolutions[0][1][15])
                res.write('%.3f,'%rankedsolutions[0][1][16])
            if order==9:
                res.write('R7,')
                res.write('R8,')
                res.write('R9,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7,')
                res.write('phi8,')
                res.write('phi9\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
                res.write('%.3f,'%rankedsolutions[0][1][15])
                res.write('%.3f,'%rankedsolutions[0][1][16])
                res.write('%.3f,'%rankedsolutions[0][1][17])
                res.write('%.3f,'%rankedsolutions[0][1][18])
            if order==10:
                res.write('R7,')
                res.write('R8,')
                res.write('R9,')
                res.write('R10,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7,')
                res.write('phi8,')
                res.write('phi9,')
                res.write('phi10\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
                res.write('%.3f,'%rankedsolutions[0][1][15])
                res.write('%.3f,'%rankedsolutions[0][1][16])
                res.write('%.3f,'%rankedsolutions[0][1][17])
                res.write('%.3f,'%rankedsolutions[0][1][18])
                res.write('%.3f,'%rankedsolutions[0][1][19])
                res.write('%.3f,'%rankedsolutions[0][1][20])
            if order==11:
                res.write('R7,')
                res.write('R8,')
                res.write('R9,')
                res.write('R10,')
                res.write('R11,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7,')
                res.write('phi8,')
                res.write('phi9,')
                res.write('phi10,')
                res.write('phi11\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
                res.write('%.3f,'%rankedsolutions[0][1][15])
                res.write('%.3f,'%rankedsolutions[0][1][16])
                res.write('%.3f,'%rankedsolutions[0][1][17])
                res.write('%.3f,'%rankedsolutions[0][1][18])
                res.write('%.3f,'%rankedsolutions[0][1][19])
                res.write('%.3f,'%rankedsolutions[0][1][20])
                res.write('%.3f,'%rankedsolutions[0][1][21])
                res.write('%.3f,'%rankedsolutions[0][1][22])
            if order==12:
                res.write('R7,')
                res.write('R8,')
                res.write('R9,')
                res.write('R10,')
                res.write('R11,')
                res.write('R12,')
                res.write('phi1,')
                res.write('phi2,')
                res.write('phi3,')
                res.write('phi4,')
                res.write('phi5,')
                res.write('phi6,')
                res.write('phi7,')
                res.write('phi8,')
                res.write('phi9,')
                res.write('phi10,')
                res.write('phi11,')
                res.write('phi12\n')
                res.write('%.3f,'%TTT[0])
                res.write('%.3f,'%rankedsolutions[0][1][0])
                res.write('%.3f,'%rankedsolutions[0][1][1])
                res.write('%.3f,'%rankedsolutions[0][1][2])
                res.write('%.3f,'%rankedsolutions[0][1][3])
                res.write('%.3f,'%rankedsolutions[0][1][4])
                res.write('%.3f,'%rankedsolutions[0][1][5])
                res.write('%.3f,'%rankedsolutions[0][1][6])
                res.write('%.3f,'%rankedsolutions[0][1][7])
                res.write('%.3f,'%rankedsolutions[0][1][8])
                res.write('%.3f,'%rankedsolutions[0][1][9])
                res.write('%.3f,'%rankedsolutions[0][1][10])
                res.write('%.3f,'%rankedsolutions[0][1][11])
                res.write('%.3f,'%rankedsolutions[0][1][12])
                res.write('%.3f,'%rankedsolutions[0][1][13])
                res.write('%.3f,'%rankedsolutions[0][1][14])
                res.write('%.3f,'%rankedsolutions[0][1][15])
                res.write('%.3f,'%rankedsolutions[0][1][16])
                res.write('%.3f,'%rankedsolutions[0][1][17])
                res.write('%.3f,'%rankedsolutions[0][1][18])
                res.write('%.3f,'%rankedsolutions[0][1][19])
                res.write('%.3f,'%rankedsolutions[0][1][20])
                res.write('%.3f,'%rankedsolutions[0][1][21])
                res.write('%.3f,'%rankedsolutions[0][1][22])
                res.write('%.3f,'%rankedsolutions[0][1][23])
                res.write('%.3f,'%rankedsolutions[0][1][24])
    if rankedsolutions[0][0] >5:
            break
    if rankedsolutions[0][0] <0.7:
            break