import numpy as np
from numpy import arange, array
from os import listdir, path
from pandas import read_csv
from random import randint
from symfit import core, cos, Fit, parameters, sin, variables
import matplotlib.pyplot as plt
import math


folder = './O_steadyflow/steady/'

#folder = 'F:/adv_export/50/'
files = sorted([f for f in listdir(folder) if path.isfile(path.join(folder, f))])


with open('./O_steady.csv', 'w', encoding='utf-8') as res:
    res.write('R(rpm)')
    res.write(',V(m/s)\n')
   
    for i, f in enumerate(files):
        print(f, round(i/len(files)*100, 2))
        R=[-50,-100,-150,-200,-250,-300,-350,-400,-450,-500,50,100,150,200,250,300,350,400,450,500,550]
        read = read_csv(folder+f, encoding='big5')
        data = read['V1/X/E']
        #length = int(.9*len(read))+1
        length = 3000#讀取的資料長度3是3個週期
        std3=3*np.std(data)
        avg=np.mean(data)
        for alldata in range(0,len(data),1):
            if abs(data[alldata]-avg)>std3:
                del data[alldata]
        if i !=20:
            res.write(str(R[i])+','+str(np.mean(data)/100)+'\n')
       
res.close()

