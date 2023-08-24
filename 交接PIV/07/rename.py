# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:40:01 2023

@author: user
"""

import os
import shutil
from tqdm import trange
s=1
n=9999
for i in trange(1,4,1):
    for b in range(s,n+1):                                #運行20000個檔案
        c=f'{b:04}'                                       #創建字串 0001 0002 0003 到 n
        e=f'{b:05}'                                                       
        
        path='./piv_07_10'
        
        file_oldname = os.path.join(path+"_100_0200_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile = os.path.join(path+"_100_0200_0"+str(i),"PIVlab_"+e+".txt")
        file_oldname1 = os.path.join(path+"_200_0400_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile1 = os.path.join(path+"_200_0400_0"+str(i),"PIVlab_"+e+".txt")
        file_oldname2 = os.path.join(path+"_300_0600_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile2 = os.path.join(path+"_300_0600_0"+str(i),"PIVlab_"+e+".txt")
        file_oldname3 = os.path.join(path+"_400_0800_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile3 = os.path.join(path+"_400_0800_0"+str(i),"PIVlab_"+e+".txt")
        
        file_oldname4 = os.path.join(path+"_500_1000_0"+str(i),"PIVlab_"+c+".txt")
        file_newname_newfile4 = os.path.join(path+"_500_1000_0"+str(i),"PIVlab_"+e+".txt")
        
        newFileName=shutil.move(file_oldname, file_newname_newfile)     #更改txt名稱
        newFileName=shutil.move(file_oldname1, file_newname_newfile1)
        newFileName=shutil.move(file_oldname2, file_newname_newfile2)
        newFileName=shutil.move(file_oldname3, file_newname_newfile3)
        newFileName=shutil.move(file_oldname4, file_newname_newfile4)