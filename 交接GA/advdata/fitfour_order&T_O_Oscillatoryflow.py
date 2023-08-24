import numpy as np
from numpy import arange, array
from os import listdir, path
from pandas import read_csv
from random import randint
from symfit import core, cos, Fit, parameters, sin, variables
import matplotlib.pyplot as plt
import math

order=6       #計算幾階
T=6           #週期
F = 2 * np.pi /T #除的數字是週期
samplingRate=1./50.
def fourier(x,n=0):
    a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n+1)]))
    sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n+1)]))
    series = a0+sum(ai*cos(i*F*x)+bi*sin(i*F*x) for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
    return series


x, y = variables('x, y')
#w, = parameters('w')
model_dict = {y: fourier(x, n=order)}
print(model_dict)

with open('./T6912.csv', 'w', encoding='utf-8') as res:
    res.write('f')
    res.write(',T0')
    res.write(',V0,')
    res.write(','.join(['V'+str(i) for i in range(1, order+1)]))
    res.write(',')
    res.write(','.join(['phi'+str(i) for i in range(1, order+1)]))
    res.write('\n')
    for TTTTT in range(6,15,3):
        T=TTTTT           #週期
        F = 2 * np.pi /T #除的數字是週期
        samplingRate=1./50.
        def fourier(x,n=0):
            a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n+1)]))
            sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n+1)]))
            series = a0+sum(ai*cos(i*F*x)+bi*sin(i*F*x) for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
            return series
        x, y = variables('x, y')
        #w, = parameters('w')
        model_dict = {y: fourier(x, n=order)}
        print(model_dict)
        if TTTTT == 6:
            folder = './O_Oscillatoryflow/T06/'
        if TTTTT == 9:
            folder = './O_Oscillatoryflow/T09/'
        if TTTTT == 12:
            folder = './O_Oscillatoryflow/T12/'
            
        files = sorted([f for f in listdir(folder) if path.isfile(path.join(folder, f))])
        for i, f in enumerate(files):
            print(f, round(i/len(files)*100, 2))
            res.write(f+',')
            read = read_csv(folder+f, encoding='big5')
            data = read['V1/X/E']
            #length = int(.9*len(read))+1
            length = int(9*T/samplingRate)+1#讀取的資料長度3是3個週期
            xdata = arange(length)*samplingRate
    
            r2 = 0.
            num = 0
            while r2 < .9:
                for i in range(num+1, len(data)):
                    if data[i] < 0 and min(data[i+1:i+10]) <0:
                        num = i+1
                        break
                ydata = array(data[num:num+length])
                print(1)
                #print(xdata)
                #print(ydata)
                fit = Fit(model_dict, xdata, ydata, minimizer=core.minimizers.Powell)
                fit_result = fit.execute()
                r2 = fit_result.r_squared
                #print(fit_result)
                #print(i, r2)
                ##raw data
                plt.plot(ydata, color='gray') 
                yfit = fit.model(x=xdata, **fit_result.params).y
                #plt.plot(fit.model(x=xdata, **fit_result.params).y, color='yellow')
           
                ##first replace
                error = yfit-ydata
                #print('error1=',abs(error).max())
                stde = np.std(error)
                #print('5stde1=',5*stde)
                for i in range(error.size):
                    ydata[abs(error)>5*stde]=yfit[abs(error)>5*stde]
                    #plt.plot(ydata, color='blue')
    
                ##second fit
                fit = Fit(model_dict, xdata, ydata, minimizer=core.minimizers.Powell)
                fit_result = fit.execute()
                yfit2 = fit.model(x=xdata, **fit_result.params).y
                #plt.plot(fit.model(x=xdata, **fit_result.params).y, color='turquoise')
                
                ##second replace
                error2 = yfit2-ydata
                #print('error2=',abs(error2).max())
                stde2 = np.std(error2)
                #print('5stde2=',5*stde2)
                for i in range(error2.size):
                    ydata[abs(error2)>5*stde2]=yfit[abs(error2)>5*stde2]
                    #plt.plot(ydata, color='red')
            
                ##third fit
                fit = Fit(model_dict, xdata, ydata, minimizer=core.minimizers.Powell)
                fit_result = fit.execute()
                yfit3 = fit.model(x=xdata, **fit_result.params).y
                #plt.plot(fit.model(x=xdata, **fit_result.params).y, color='pink')
            
                ##third replace
                error3 = yfit3-ydata
                #print('error3=',abs(error3).max())
                stde3 = np.std(error3)
                #print('5stde3=',5*stde3)
                for i in range(error3.size):
                    ydata[abs(error3)>5*stde3]=yfit[abs(error3)>5*stde3]
                    #plt.plot(ydata, color='orange')
            
                ##final fit
                fit = Fit(model_dict, xdata, ydata, minimizer=core.minimizers.Powell)
                fit_result = fit.execute()
                yfit4 = fit.model(x=xdata, **fit_result.params).y
                #plt.plot(fit.model(x=xdata, **fit_result.params).y, color='yellow')
            
                error = yfit4-ydata
                #print('error4=',abs(error).max())
                stde = np.std(error)
                #print('3stde4=',3*stde)
    
                '''
                plt.title(f)
                plt.xlabel('t(s)')
                plt.ylabel('u(cm/s)')
                plt.plot(fit.model(x=xdata, **fit_result.params).y, color='steelblue')
                #plt.savefig(f+'.png', dpi=200)
                plt.show()
                plt.close()
                '''
            A0=[]    
            for k, v in fit_result.params.items():
                A0.append(v)
            
            a0 = A0[0]
            for count in range(1,order+1,1):
                globals()['a'+str(count)] = A0[count]
                globals()['b'+str(count)] = A0[count+order]
            
            a1=  A0[1]
            a2 = A0[2]
            a3 = A0[3]
            a4 = A0[4]
            a5 = A0[5]
            a6 = A0[6]
            b1 = A0[1+order]
            b2 = A0[2+order]
            b3 = A0[3+order]
            b4 = A0[4+order]
            b5 = A0[5+order]
            b6 = A0[6+order]
            if order > 6:
                a7 = A0[7]
                b7 = A0[7+order]
                if order > 7:
                    a8 = A0[8]
                    b8 = A0[8+order]
                    if order > 8:
                        a9 = A0[9]
                        b9 = A0[9+order]
                        if order > 9:
                            a10 = A0[10]
                            b10 = A0[10+order]
                            if order > 10:
                                a11 = A0[11]
                                b11 = A0[11+order]
                                if order > 11:
                                    a12 = A0[12]
                                    b12 = A0[12+order]
                                    
            
            
            t=np.arange(2950,2950+T,0.2)  
            
            length = int(len(files))
            F1 = arange(length)
            
            #print('f=',FF1)
            #print(FF1)
            length1 = int(len(files))
            
            A1 = arange(length1)
            AA1 = array(a1)
            #print('a1=',AA1)
            A2 = arange(length1)
            AA2 = array(a2)
            A3 = arange(length1)
            AA3 = array(a3)
            A4 = arange(length1)
            AA4 = array(a4)
            A5 = arange(length1)
            AA5 = array(a5)
            A6 = arange(length1)
            AA6 = array(a6)
            if order > 6: 
                A7 = arange(length1)
                AA7 = array(a7)
                if order > 7:
                    A8 = arange(length1)
                    AA8 = array(a8)
                    if order > 8:
                        A9 = arange(length1)
                        AA9 = array(a9)
                        if order > 9:
                            A10 = arange(length1)
                            AA10 = array(a10)
                            if order > 10:
                                A11 = arange(length1)
                                AA11 = array(a11)
                                if order > 11:
                                    A12 = arange(length1)
                                    AA12 = array(a12)
            
            
            
            
            
            length2 = int(len(files))
            B1 = arange(length2)
            BB1 = array(b1)
            #print('b1=',BB1)
            B2 = arange(length2)
            BB2 = array(b2)
            B3 = arange(length2)
            BB3 = array(b3)
            B4 = arange(length2)
            BB4 = array(b4)
            B5 = arange(length2)
            BB5 = array(b5)
            B6 = arange(length2)
            BB6 = array(b6)
            if order > 6:
                B7 = arange(length2)
                BB7 = array(b7)
                if order > 7:
                    B8 = arange(length2)
                    BB8 = array(b8)
                    if order > 8:
                        B9 = arange(length2)
                        BB9 = array(b9)
                        if order > 9:
                            B10 = arange(length2)
                            BB10 = array(b10)
                            if order > 10:
                                B11 = arange(length2)
                                BB11 = array(b11)
                                if order > 11:
                                    B12 = arange(length2)
                                    BB12 = array(b12)
            
            
            
            
            
    
            C1 = np.sqrt(np.power(AA1,2)+np.power(BB1,2))
            C2 = np.sqrt((AA2)**2 + (BB2)**2)
            C3 = np.sqrt((AA3)**2 + (BB3)**2)
            C4 = np.sqrt((AA4)**2 + (BB4)**2)
            C5 = np.sqrt((AA5)**2 + (BB5)**2)
            C6 = np.sqrt((AA6)**2 + (BB6)**2)
            phi1 = np.arccos(b1 / C1)
            phi2 = np.arccos(b2 / C2)
            phi3 = np.arccos(b3 / C3)
            phi4 = np.arccos(b4 / C4)
            phi5 = np.arccos(b5 / C5)
            phi6 = np.arccos(b6 / C6)
            if order > 6:
                C7 = np.sqrt(np.power(AA7,2)+np.power(BB7,2))
                phi7 = np.arccos(b7 / C7)
                if order > 7:
                    C8 = np.sqrt((AA8)**2 + (BB8)**2)
                    phi8 = np.arccos(b8 / C8)
                    if order > 8:
                        C9 = np.sqrt((AA9)**2 + (BB9)**2)
                        phi9 = np.arccos(b9 / C9)
                        if order > 9:
                            C10 = np.sqrt((AA10)**2 + (BB10)**2)
                            phi10 = np.arccos(b10 / C10)
                            if order > 10:
                                C11 = np.sqrt((AA11)**2 + (BB11)**2)
                                phi11 = np.arccos(b11 / C11)
                                if order > 11:
                                    C12 = np.sqrt((AA12)**2 + (BB12)**2)
                                    phi12 = np.arccos(b12 / C12)
            
            
            
            for gg in range(len(files)):
                phi1 = math.atan2(a1 , b1)
                phi2 = math.atan2(a2 , b2)
                phi3= math.atan2(a3 , b3)
                phi4= math.atan2(a4 , b4)
                phi5= math.atan2(a5 , b5)
                phi6 = math.atan2(a6 , b6)
                if order > 6:
                    phi7 = math.atan2(a7 , b7)
                    if order > 7:
                        phi8 = math.atan2(a8 , b8)
                        if order > 8:
                            phi9= math.atan2(a9 , b9)
                            if order > 9:
                                phi10= math.atan2(a10 , b10)
                                if order > 10:
                                    phi11= math.atan2(a11 , b11)
                                    if order > 11:
                                        phi12 = math.atan2(a12 , b12)
                
                
                
                
                
    
            PHI1 = phi1 - phi1
            PHI2 = phi2 - phi1*2
            PHI3 = phi3 - phi1*3
            PHI4 = phi4 - phi1*4
            PHI5 = phi5 - phi1*5
            PHI6 = phi6 - phi1*6
            
            PHI2= 2*np.pi*(PHI2/(2*np.pi)-np.floor(PHI2/(2*np.pi)))    
            PHI3= 2*np.pi*(PHI3/(2*np.pi)-np.floor(PHI3/(2*np.pi)))    
            PHI4= 2*np.pi*(PHI4/(2*np.pi)-np.floor(PHI4/(2*np.pi)))    
            PHI5= 2*np.pi*(PHI5/(2*np.pi)-np.floor(PHI5/(2*np.pi)))
            PHI6= 2*np.pi*(PHI6/(2*np.pi)-np.floor(PHI6/(2*np.pi)))
            if order > 6:
                PHI7 = phi1 - phi1*7
                PHI7= 2*np.pi*(PHI7/(2*np.pi)-np.floor(PHI7/(2*np.pi)))   
                if order > 7:
                    PHI8 = phi2 - phi1*8
                    PHI8= 2*np.pi*(PHI8/(2*np.pi)-np.floor(PHI8/(2*np.pi)))    
                    if order > 8:
                        PHI9 = phi3 - phi1*9
                        PHI9= 2*np.pi*(PHI9/(2*np.pi)-np.floor(PHI9/(2*np.pi))) 
                        if order > 9:
                            PHI10 = phi4 - phi1*10
                            PHI10= 2*np.pi*(PHI10/(2*np.pi)-np.floor(PHI10/(2*np.pi)))
                            if order > 10:
                                PHI11 = phi5 - phi1*11
                                PHI11= 2*np.pi*(PHI11/(2*np.pi)-np.floor(PHI11/(2*np.pi)))
                                if order > 11:
                                    PHI12 = phi6 - phi1*12
                                    PHI12= 2*np.pi*(PHI12/(2*np.pi)-np.floor(PHI12/(2*np.pi)))
            
            
            
            funnn=(a0+C1*np.sin(2*1*np.pi*t/T+PHI1)+C2*np.sin(2*2*np.pi*t/T+PHI2)+C3*np.sin(2*3*np.pi*t/T+PHI3)+C4*np.sin(2*4*np.pi*t/T+PHI4)+C5*np.sin(2*5*np.pi*t/T+PHI5)+C6*np.sin(2*6*np.pi*t/T+PHI6))
            if order > 6:
                funnn=funnn+C7*np.sin(2*7*np.pi*t/T+PHI7)
                if order > 7:
                    funnn=funnn+C8*np.sin(2*8*np.pi*t/T+PHI8)
                    if order > 8:
                        funnn=funnn+C9*np.sin(2*9*np.pi*t/T+PHI9)
                        if order > 9:
                            funnn=funnn+C10*np.sin(2*10*np.pi*t/T+PHI10)
                            if order > 10:
                                funnn=funnn+C11*np.sin(2*11*np.pi*t/T+PHI11)
                                if order > 11:
                                    funnn=funnn+C12*np.sin(2*12*np.pi*t/T+PHI12)
                    
            plt.plot(t,funnn, color='k',marker='o')
            plt.show()
            plt.close()
            if order == 12:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','+str(C8)+','+str(C9)+','+str(C10)+','+str(C11)+','+str(C12)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)+','+str(PHI8)+','+str(PHI9)+','+str(PHI10)+','+str(PHI11)+','+str(PHI12)
                          +'\n')
            if order == 11:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','+str(C8)+','+str(C9)+','+str(C10)+','+str(C11)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)+','+str(PHI8)+','+str(PHI9)+','+str(PHI10)+','+str(PHI11)
                          +'\n')
            if order == 10:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','+str(C8)+','+str(C9)+','+str(C10)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)+','+str(PHI8)+','+str(PHI9)+','+str(PHI10)
                          +'\n')
            if order == 9:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','+str(C8)+','+str(C9)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)+','+str(PHI8)+','+str(PHI9)
                          +'\n')
            if order == 8:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','+str(C8)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)+','+str(PHI8)
                          +'\n')
            if order == 7:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(C7)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)+','
                          +str(PHI7)
                          +'\n')
            if order == 6:
                res.write(str(T)+','+str(a0)+','
                          +str(C1)+','+str(C2)+','+str(C3)+','+str(C4)+','+str(C5)+','+str(C6)+','
                          +str(PHI1)+','+str(PHI2)+','+str(PHI3)+','+str(PHI4)+','+str(PHI5)+','+str(PHI6)
                          +'\n')
res.close()

