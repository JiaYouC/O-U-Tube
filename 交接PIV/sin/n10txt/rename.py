# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:40:01 2023

@author: user
"""

import os
import shutil
from tqdm import trange
s=1
n=600
for i in trange(1,4,1):
    for b in range(s,n+1):                                #運行20000個檔案
        c=f'{b:04}'                                       #創建字串 0001 0002 0003 到 n
        e=f'{b:05}'                                                       
        
        path='sin_n10'
        
        file_oldname = os.path.join(path+"_100_0030_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile = os.path.join(path+"_100_0030_0"+str(i),"PIVlab_"+e+".txt")
    
        
        newFileName=shutil.move(file_oldname, file_newname_newfile)     #更改txt名稱
    