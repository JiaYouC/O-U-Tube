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

for Rpm in trange(100,600,100):
    path='./FPS_avg/'+str(Rpm)+'rpm/'        
    pathh=r'C:/Users/user/Desktop/交接code/07/piv_07_10_'                #放置檔案的資料夾路徑
    #for time in range(20000,20100,100):
    time=20000
    myArr1 = pd.read_csv(pathh+"100_0200_01"+"/PIVlab_00001.txt",delimiter=',')              #讀取第一個檔案以便知道尺寸
    s = 1                                                                    #檔案從第幾個開啟
    n = time                                                           #檔案從第幾個結束
    m = np.array(myArr1) 
    size = len(myArr1)                                                       #讀取檔案總共有幾列
    sum = np.zeros((int(size),5))                                            #創造零矩陣 準備將資料加上去
    sum2 = np.zeros((int(size),5))
    sum3 = np.zeros((int(size),5))
    ld = 0#0.0019                                                              #網格中心到底板距離  注意單位為m
    gd = m[1:2,1:2]-m[0:1,1:2]
    for b in range(s,n+1):                                                  #運行6117個檔案
        c=f'{b:05}'                                                          #創建字串 0001 0002 0003 到 n
        exposure=Rpm*2
        exp=f'{exposure:04}'
        myArr = pd.read_csv(pathh+str(Rpm)+'_'+str(exp)+'_01'+"/PIVlab_"+c+".txt",delimiter=',')          #讀取檔案
        myArr2 =pd.read_csv(pathh+str(Rpm)+'_'+str(exp)+'_02'+"/PIVlab_"+c+".txt",delimiter=',')
        myArr3 =pd.read_csv(pathh+str(Rpm)+'_'+str(exp)+'_03'+"/PIVlab_"+c+".txt",delimiter=',')
        k = np.array(myArr)                                                  #資料轉矩陣
        k2 = np.array(myArr2)   
        k3 = np.array(myArr3)   
        sum=sum+k                                                            #將資料加到原先創造的零矩陣上
        sum2=sum2+k2
        sum3=sum3+k3
        if b%100==0:
            average = sum/(b-s+1)                                                          #將總值除以檔案個數
            average2 = sum2/(b-s+1)        
            average3 = sum3/(b-s+1)
            x = (average[:,0:1]-average[:,0:1].mean())*100      #將x數值轉為左右對稱 並將單位從m改為cm
            lenth=int(len(x)/11)
            num=(
                 (average[0:lenth,1:2]-average[0:lenth,1:2].max())
                +(average[lenth:2*lenth,1:2]-average[lenth:2*lenth,1:2].max())
                +(average[2*lenth:3*lenth,1:2]-average[2*lenth:3*lenth,1:2].max())
                +(average[3*lenth:4*lenth,1:2]-average[3*lenth:4*lenth,1:2].max())
                +(average[4*lenth:5*lenth,1:2]-average[4*lenth:5*lenth,1:2].max())
                +(average[5*lenth:6*lenth,1:2]-average[5*lenth:6*lenth,1:2].max())
                +(average[6*lenth:7*lenth,1:2]-average[6*lenth:7*lenth,1:2].max())
                +(average[7*lenth:8*lenth,1:2]-average[7*lenth:8*lenth,1:2].max())
                +(average[8*lenth:9*lenth,1:2]-average[8*lenth:9*lenth,1:2].max())
                +(average[9*lenth:10*lenth,1:2]-average[9*lenth:10*lenth,1:2].max())
                +(average[10*lenth:11*lenth,1:2]-average[10*lenth:11*lenth,1:2].max())
                )/11
            #+(average[2*lenth:3*lenth,1:2]-average[2*lenth:3*lenth,1:2].max())
            #+(average[3*lenth:4*lenth,1:2]-average[3*lenth:4*lenth,1:2].max())
            
            y = ((num)*(-1)+ld+gd)*100               #將y數值轉為以d為結束的數值 並將單位從m改為cm
            
            u = (
                average[0:lenth,2:3]+average[lenth:2*lenth,2:3]+average[2*lenth:3*lenth,2:3]+average[3*lenth:4*lenth,2:3]
                +average[4*lenth:5*lenth,2:3]+average[5*lenth:6*lenth,2:3]+average[6*lenth:7*lenth,2:3]+average[7*lenth:8*lenth,2:3]
                +average[8*lenth:9*lenth,2:3]+average[9*lenth:10*lenth,2:3]+average[10*lenth:11*lenth,2:3]
                )*100/11  #'+average[2*lenth:3*lenth,2:3]+average[3*lenth:4*lenth,2:3]'                                                 #將u單位從m改為cm
            u2= (
                average2[0:lenth,2:3]+average2[lenth:2*lenth,2:3]+average2[2*lenth:3*lenth,2:3]+average2[3*lenth:4*lenth,2:3]
                +average2[4*lenth:5*lenth,2:3]+average2[5*lenth:6*lenth,2:3]+average2[6*lenth:7*lenth,2:3]+average2[7*lenth:8*lenth,2:3]
                +average2[8*lenth:9*lenth,2:3]+average2[9*lenth:10*lenth,2:3]+average2[10*lenth:11*lenth,2:3]
                )*100/11
            u3= (
                average3[0:lenth,2:3]+average3[lenth:2*lenth,2:3]+average3[2*lenth:3*lenth,2:3]+average3[3*lenth:4*lenth,2:3]
                +average3[4*lenth:5*lenth,2:3]+average3[5*lenth:6*lenth,2:3]+average3[6*lenth:7*lenth,2:3]+average3[7*lenth:8*lenth,2:3]
                +average3[8*lenth:9*lenth,2:3]+average3[9*lenth:10*lenth,2:3]+average3[10*lenth:11*lenth,2:3]
                )*100/11
            
            v = (
                average[0:lenth,3:4]+average[lenth:2*lenth,3:4]+average[2*lenth:3*lenth,3:4]+average[3*lenth:4*lenth,3:4]
                +average[4*lenth:5*lenth,3:4]+average[5*lenth:6*lenth,3:4]+average[6*lenth:7*lenth,3:4]+average[7*lenth:8*lenth,3:4]
                +average[8*lenth:9*lenth,3:4]+average[9*lenth:10*lenth,3:4]+average[10*lenth:11*lenth,3:4]
                )*100*(-1)/11  #'+average[2*lenth:3*lenth,3:4]+average[3*lenth:4*lenth,3:4]'                                            #將v單位從m改為cm v方向從下到上
            v2 = (
                average2[0:lenth,3:4]+average2[lenth:2*lenth,3:4]+average2[2*lenth:3*lenth,3:4]+average2[3*lenth:4*lenth,3:4]
                +average2[4*lenth:5*lenth,3:4]+average2[5*lenth:6*lenth,3:4]+average2[6*lenth:7*lenth,3:4]+average2[7*lenth:8*lenth,3:4]
                +average2[8*lenth:9*lenth,3:4]+average2[9*lenth:10*lenth,3:4]+average2[10*lenth:11*lenth,3:4]
                )*100*(-1)/11
            v3 = (
                average3[0:lenth,3:4]+average3[lenth:2*lenth,3:4]+average3[2*lenth:3*lenth,3:4]+average3[3*lenth:4*lenth,3:4]
                +average3[4*lenth:5*lenth,3:4]+average3[5*lenth:6*lenth,3:4]+average3[6*lenth:7*lenth,3:4]+average3[7*lenth:8*lenth,3:4]
                +average3[8*lenth:9*lenth,3:4]+average3[9*lenth:10*lenth,3:4]+average3[10*lenth:11*lenth,3:4]
                )*100*(-1)/11
            
            vorticity = (
                        average[0:lenth,4:5]+average[lenth:2*lenth,4:5]+average[2*lenth:3*lenth,4:5]+average[3*lenth:4*lenth,4:5]
                        +average[4*lenth:5*lenth,4:5]+average[5*lenth:6*lenth,4:5]+average[6*lenth:7*lenth,4:5]+average[7*lenth:8*lenth,4:5]
                        +average[8*lenth:9*lenth,4:5]+average[9*lenth:10*lenth,4:5]+average[10*lenth:11*lenth,4:5]
                        )/2  #'+average[2*lenth:3*lenth,4:5]+average[3*lenth:4*lenth,4:5]'                                               #渦度數值不變
            vorticity2 = (
                        average2[0:lenth,4:5]+average2[lenth:2*lenth,4:5]+average2[2*lenth:3*lenth,4:5]+average2[3*lenth:4*lenth,4:5]
                        +average2[4*lenth:5*lenth,4:5]+average2[5*lenth:6*lenth,4:5]+average2[6*lenth:7*lenth,4:5]+average2[7*lenth:8*lenth,4:5]
                        +average2[8*lenth:9*lenth,4:5]+average2[9*lenth:10*lenth,4:5]+average2[10*lenth:11*lenth,4:5]
                        )/2
            vorticity3 = (
                        average3[0:lenth,4:5]+average3[lenth:2*lenth,4:5]+average3[2*lenth:3*lenth,4:5]+average3[3*lenth:4*lenth,4:5]
                        +average3[4*lenth:5*lenth,4:5]+average3[5*lenth:6*lenth,4:5]+average3[6*lenth:7*lenth,4:5]+average3[7*lenth:8*lenth,4:5]
                        +average3[8*lenth:9*lenth,4:5]+average3[9*lenth:10*lenth,4:5]+average3[10*lenth:11*lenth,4:5]
                        )/2
            
            #Y=(y[0:len(y)/4]+y[len(y)/4:2*len(y)/4]+y[2*len(y)/4:3*len(y)/4]+y[3*len(y)/4:4*len(y)/4])/4
            array_all = np.hstack((y,u,v,vorticity))                               #合併5項數值
            array_all2 = np.hstack((y,u2,v2,vorticity2))
            array_all3 = np.hstack((y,u3,v3,vorticity3))
            
            ff=f'{b:05}'
            np.savetxt(path+'1st'+"/PIVlab_"+ff+".txt",array_all, delimiter=',',fmt='%1.12f')    #儲存檔案
            np.savetxt(path+'2nd'+"/PIVlab_"+ff+".txt",array_all2, delimiter=',',fmt='%1.12f')
            np.savetxt(path+'3rd'+"/PIVlab_"+ff+".txt",array_all3, delimiter=',',fmt='%1.12f')