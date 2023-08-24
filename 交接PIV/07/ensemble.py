# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:03:07 2023

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
def insert(df,i,df_add):
    df1=df.iloc[:i,:]
    df2=df.iloc[i:,:]
    dfnew=pd.concat([df1,df_add,df2],ignore_index=True)
    return dfnew
for Rpm in trange(100,600,100):
    path='./FPS_avg/'+str(Rpm)+'rpm/'      
    #pathh=r'C:/Users/陳佳佑/Dropbox/PC/Desktop/newpiv/30cmtxt/05txt/FPS_avg/'+str(Rpm)+'rpm/'                  #放置檔案的資料夾路徑
    #for i in range(1,4,1):
        #for time in range(1,41,1):
    '''
    myArr1 = pd.read_csv(path+'1st'+"/PIVlab_00001.txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',')   
    myArr2 = pd.read_csv(path+'2nd'+"/PIVlab_00001.txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',')   
    myArr3 = pd.read_csv(path+'3rd'+"/PIVlab_00001.txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',')   
    myArr4=myArr1+myArr2+myArr3
    '''
    #讀取第一個檔案以便知道尺寸
    
    s = 100                                                                    #檔案從第幾個開啟
    n = 20000                                                         #檔案從第幾個結束
    for b in range(s,n+100,100):                                                  #運行6117個檔案
        c=f'{b:05}'                                                          #創建字串 0001 0002 0003 到 n
        myArr1 = pd.read_csv(path+'1st'+"/PIVlab_"+c+".txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',')          #讀取檔案
        myArr2 = pd.read_csv(path+'2nd'+"/PIVlab_"+c+".txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',') 
        myArr3 = pd.read_csv(path+'3rd'+"/PIVlab_"+c+".txt",names=["y[m]", "u[m/s]", "v[m/s]","vorticity[1/s]"],delimiter=',') 
        myArr4 = (myArr1+myArr2+myArr3)/3
        myArr4.columns=["y[cm]","u[cm/s]","v[cm/s]","vorticity[1/s]"]
        dfadd=pd.DataFrame({"y[cm]":["y[cm]"],"u[cm/s]":["u[cm/s]"],"v[cm/s]":["v[cm/s]"],"vorticity[1/s]":["vorticity[1/s]"]})
        #k = np.array(myArr4)                                                  #資料轉矩陣
        k=insert(myArr4,0,dfadd)
        #sum=sum+k                                                            #將資料加到原先創造的零矩陣上
        np.savetxt(path+'ensemble'+"/PIVlab_"+c+".txt",k, delimiter=',',fmt='%s')    #儲存檔案                                         #渦度數值不變
    #Y=(y[0:len(y)/4]+y[len(y)/4:2*len(y)/4]+y[2*len(y)/4:3*len(y)/4]+y[3*len(y)/4:4*len(y)/4])/4
    #array_all = np.hstack((y,u,v,vorticity))                               #合併5項數值
    
    