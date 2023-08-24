# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:59:03 2023

@author: user
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import gzip
import os
import shutil
import csv
from tqdm import trange
import time

path='./space_avg/sin_n10_100_0030_'        
pathh=r'C:/Users/user/Desktop/交接code/交接PIV/sin/n10txt/sin_n10_100_0030'                #放置檔案的資料夾路徑
#for time in range(20000,20100,100):
time=600
myArr1 = pd.read_csv(pathh+"_01"+"/PIVlab_00001.txt",delimiter=',')              #讀取第一個檔案以便知道尺寸
s = 1                                                                    #檔案從第幾個開啟
n = time                                                           #檔案從第幾個結束
m = np.array(myArr1) 
size = len(myArr1)                                                       #讀取檔案總共有幾列
ld = 0#0.0019                                                              #網格中心到底板距離  注意單位為m
gd = m[1:2,1:2]-m[0:1,1:2]
for b in trange(s,n+1):                                                  #運行6117個檔案
    c=f'{b:05}'                                                          #創建字串 0001 0002 0003 到 n
    myArr = pd.read_csv(pathh+'_01'+"/PIVlab_"+c+".txt",delimiter=',')          #讀取檔案
    myArr2 =pd.read_csv(pathh+'_02'+"/PIVlab_"+c+".txt",delimiter=',')
    myArr3 =pd.read_csv(pathh+'_03'+"/PIVlab_"+c+".txt",delimiter=',')
    k = np.array(myArr)                                                  #資料轉矩陣
    k2 = np.array(myArr2)   
    k3 = np.array(myArr3)   
    y = k[:,1:2]
    x = (k[:,0:1]-k[:,0:1].mean())*100
    count=0
    while count!=-1:
        count=count+1
        if y[0]==y[count]:
            delt=count
            count=-1
    xnum=int(len(y)/delt)   
    
    avgy=-k[0:delt,1:2]+y[-1]
    
    u=k[0:delt,2:3]
    u2=k2[0:delt,2:3]
    u3=k3[0:delt,2:3]
    v=k[0:delt,3:4]
    v2=k2[0:delt,3:4]
    v3=k3[0:delt,3:4]
    vorticity=k[0:delt,4:5]
    vorticity2=k2[0:delt,4:5]
    vorticity3=k3[0:delt,4:5]
    for count in range(1,xnum):
        u=u+k[count*delt:(count+1)*delt,2:3]
        u2=u2+k2[count*delt:(count+1)*delt,2:3]
        u3=u+k3[count*delt:(count+1)*delt,2:3]
        v=v+k[count*delt:(count+1)*delt,3:4]
        v2=v2+k2[count*delt:(count+1)*delt,3:4]
        v3=v3+k3[count*delt:(count+1)*delt,3:4]
        vorticity=vorticity+k[count*delt:(count+1)*delt,4:5]
        vorticity2=vorticity2+k2[count*delt:(count+1)*delt,4:5]
        vorticity3=vorticity3+k3[count*delt:(count+1)*delt,4:5]
    avgu=u/xnum
    avgu2=u2/xnum
    avgu3=u3/xnum
    avgv=v/xnum
    avgv2=v2/xnum
    avgv3=v3/xnum
    avgvorticity=vorticity/xnum
    avgvorticity2=vorticity2/xnum
    avgvorticity3=vorticity3/xnum
    
    
    array_all = np.hstack((avgy,avgu,avgv,avgvorticity))                               #合併5項數值
    array_all2 = np.hstack((avgy,avgu2,avgv2,avgvorticity2))
    array_all3 = np.hstack((avgy,avgu3,avgv3,avgvorticity3))
    
  
    
    ff=f'{b:05}'
    np.savetxt(path+'01'+"/PIVlab_"+ff+".txt",array_all, delimiter=',',fmt='%1.12f')    #儲存檔案
    np.savetxt(path+'02'+"/PIVlab_"+ff+".txt",array_all2, delimiter=',',fmt='%1.12f')
    np.savetxt(path+'03'+"/PIVlab_"+ff+".txt",array_all3, delimiter=',',fmt='%1.12f')
    