# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:12:43 2022

@author: ansari
"""

""""
Modelind real covid data in Germany with SIR model:
In this code first of all the number of active infected cases are read from input file,
then this data subdevided to 8 tim window, each one follow a special distribution.
since we model it with use of SIR epiemic model,for each distribution there are 2 different 
beta and delta rates, beta is the transmission rate and delta is recovery rate.
after fitting data, different fitted curves are plotted at the end. 

"""
import numpy as np
from scipy. integrate import odeint
import pandas as pd
import matplotlib .pyplot as plt
from scipy.optimize import curve_fit


#reading Covid data from file

excel_file = 'Fallzahlen_Kum_Tab_aktuell.xlsx'
M = pd.read_excel ( excel_file,sheet_name = 2 )
M_New = M.iloc[9,1:367]        #this keeps the list of daily inf_case 


#we consider 8 differnt windows considering the input data

#each M_New shos daily infected case for realted time window
M_New1 = np.squeeze(np.asarray( M_New [0:75]))
M_New2 = np.squeeze(np.asarray( M_New [75:115]))
M_New3 = np.squeeze(np.asarray( M_New [115:139]))
M_New4 = np.squeeze(np.asarray( M_New [139:180]))
M_New5 = np.squeeze(np.asarray( M_New [180:200]))
M_New6 = np.squeeze(np.asarray( M_New [200:270]))
M_New7 = np.squeeze(np.asarray( M_New [270:300]))
M_New8 = np.squeeze(np.asarray( M_New [300:366]))

maxi = len(M)     # the no of data points (or no of days)

#differnt time windows
tf = np.linspace (0, maxi)
tf1 =np.linspace (0 ,75 ,75)
tf2 =np.linspace (75 ,115 ,40)
tf3 =np.linspace (115 ,139 ,24)
tf4 =np.linspace (139 ,180 ,41)
tf5 =np.linspace (180 ,200 ,20)
tf6 =np.linspace (200 ,270 ,70)
tf7 =np.linspace (270 ,300 ,30)
tf8 =np.linspace (300 ,366 ,66)



# preparing the output plot
fig1 = plt.figure( facecolor ='w',num=None ,figsize =(10, 6),
dpi =100 ,
edgecolor ='k')
fig1.suptitle ('Active infected − Hamburg',fontsize =14,
fontweight ='bold')
plt = fig1. add_subplot (111 ,facecolor ='white',axisbelow =True,label="1")

ax1=fig1.add_subplot(111, label="2", frame_on=False)

# T o t a l p o p u l a t i o n , N
N = 1788000 #83000000 Germany #1788000 Hamburg  #12930751 bayern  #3500000  berlin
# I n i t i a l number o f i n f e c t e d and r e c o v e r e d i n d i v i d u a l s , I 0 and R0 .

I0 = M_New1[0]      # the no of infected case at 11th Sep 2021(initial no of infected cases)
S0 = N-I0           #the initial no of suspected cases 
R0 = 0
delta =1/(27)

y0 = S0,I0,R0     #the initial values of SIR model

def sir_model(y, tf, beta, delta):    
    '''
    SIR differential equations
    '''

    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - delta * I
    dRdt = delta * I
   
    return dSdt,dIdt,dRdt

def fit_odeint1(tf1, beta, delta):
    return odeint(sir_model, y0, tf1, args=(beta, delta))[:,2]

#fitting curve to  data with least square method
popt1, pcov = curve_fit ( fit_odeint1 ,tf1 , M_New1 )  
fitted1 = fit_odeint1 (tf1 , *popt1)
beta1 = popt1 [0]
delta1 = popt1 [1]
print("\n beta and delta: ",popt1)

ret = odeint( sir_model , y0 , tf1 , args =(\
beta1 ,delta1 ))
S, I, R = ret.T

#***********************************************************
# 2sub− i n t e r v a l o f ti m e
y2 =ret.T[0][74]  ,ret.T[1][74]   , ret.T[2][74] 

def fit_odeint2 (tf2 ,beta,delta):
    return odeint( sir_model , y2 , tf2 ,args =(beta ,delta ))[: ,2]

popt2 , pcov = curve_fit ( fit_odeint2 ,tf2 , M_New2)
fitted2 = fit_odeint2 (tf2 , *popt2)
beta2 = popt2 [0]
delta2 = popt2 [1] 
print("\n beta2 and delta2: ",popt2)
ret = odeint( sir_model , y2 , tf2 ,args =(\
beta2 ,delta2 ))

S2 , I2 , R2  = ret.T


#*********************************************************
# 3 sub− i n t e r v a l o f ti m e
y3 = ret.T[0][39] , ret.T[1][39] , ret.T[2][39] 

def fit_odeint3 (tf3 ,beta ,delta):
    return odeint( sir_model , y3 , tf3 ,\
                  args =( beta ,delta  ))[: ,2]
    
popt3 , pcov = curve_fit ( fit_odeint3 ,tf3 , M_New3 )
fitted3 = fit_odeint3 (tf3 , *popt3)
beta3 = popt3 [0]
delta3 = popt3 [1]
print("\n beta3 and delta3: ",popt3)
ret = odeint( sir_model , y3 , tf3 ,\
args =(beta3 ,delta3))
S3 , I3 , R3  = ret.T


#**************************************************

# 4 sub− i n t e r v a l o f ti m e     
y4 = ret.T[0][23] ,ret.T[1][23] , ret.T[2][23]
def fit_odeint4 (tf4 ,beta,delta ):
    return odeint( sir_model , y4 , tf4 ,\
                  args =( beta ,delta ))[: ,2]
    
popt4 , pcov = curve_fit ( fit_odeint4 ,tf4 , M_New4 )
fitted4 = fit_odeint4 (tf4 , *popt4)
beta4 = popt4 [0]
delta4 = popt4 [1]
print("\n beta4 and delta4: ",popt4)
ret = odeint( sir_model , y4 , tf4 ,\
args =(beta4 ,delta4))
S4 , I4 , R4 = ret.T


#******************************************
# 5 sub− i n t e r v a l o f ti m e
y5 = ret.T[0][40] , ret.T[1][40] , ret.T[2][40] 
def fit_odeint5 (tf5 ,beta,delta ):
    return odeint( sir_model , y5 , tf5 ,args =( beta ,delta ))[: ,2]
popt5 , pcov = curve_fit ( fit_odeint5 ,tf5 , M_New5 )
fitted5 = fit_odeint5 (tf5 , *popt5)
beta5 = popt5 [0]
delta5 = popt5[1]
print("\n beta5 and delta5: ",popt5)

ret = odeint( sir_model , y5 , tf5 ,\
args =(beta5 ,delta5))
S5 , I5 , R5  = ret.T

#****************************************************************
# 6 sub− i n t e r v a l o f ti m e
y6 = ret.T[0][19] , ret.T[1][19] , ret.T[2][19]
def fit_odeint6 (tf6 ,beta ,delta):
     return odeint( sir_model , y6 , tf6 ,args =( beta ,delta ))[: ,2]
popt6 , pcov = curve_fit ( fit_odeint6 ,tf6 , M_New6 )

fitted6 = fit_odeint6 (tf6 , *popt6)
beta6 = popt6 [0]
delta6 = popt6[1]

print("\n beta6 and delta6: ",popt6)

ret = odeint( sir_model , y6 , tf6 ,\
args =(beta6 ,delta6))
S6 , I6 , R6 = ret.T


#******************************************************************************
# 7 sub− i n t e r v a l o f ti m e
y7 = ret.T[0][69] , ret.T[1][69] , ret.T[2][69]
def fit_odeint7 (tf7 ,beta ,delta):
     return odeint( sir_model , y7 , tf7 ,args =( beta ,delta ))[: ,2]
popt7 , pcov = curve_fit ( fit_odeint7 ,tf7 , M_New7 )

fitted7 = fit_odeint7 (tf7, *popt7)
beta7 = popt7 [0]
delta7 = popt7[1]

print("\n beta7 and delta7: ",popt7)

ret = odeint( sir_model , y7 , tf7 ,\
args =(beta7 ,delta7))
S7 , I7 , R7 = ret.T


#********************************************************************
# 8 sub− i n t e r v a l o f ti m e

y8 = ret.T[0][29] , ret.T[1][29] , ret.T[2][29]
def fit_odeint8 (tf8 ,beta ,delta):
     return odeint( sir_model , y8 , tf8 ,args =( beta ,delta ))[: ,2]
popt8 , pcov = curve_fit ( fit_odeint8 ,tf8 , M_New8 )

fitted8 = fit_odeint8 (tf8, *popt8)
beta8 = popt8 [0]
delta8 = popt8[1]

print("\n beta8 and delta8: ",popt8)

ret = odeint( sir_model , y8 , tf8 ,\
args =(beta8 ,delta8))
S8 , I8 , R8 = ret.T



#**************************************************************PLOTTING All Fitted Curves


plt.plot(tf1 , fitted1 , color="purple", alpha =5, lw =2.5 ,\
label="Model −> 11 SEP − 26 NOV 2021")

plt.plot(tf2 , fitted2 , color="magenta", alpha =5, lw =2.5 ,label='Model −> 26 NOV 2021 − 6 Jan')


plt.plot(tf3 , fitted3 , color= "blue", alpha =5, lw =2.5 ,label='Model −>  6 Jan − 30 Jan')

plt.plot(tf4 , fitted4 , color="aqua", alpha =5, lw =2.5 ,\
label='Model −>30 Jan − 11 MAR')

plt.plot(tf5 , fitted5 , color="lawngreen", alpha =5, lw =2.5 ,\
label='Model −>  11 MAR − 1 APR')
plt.plot(tf6 , fitted6 , color="darkorange", alpha =5, lw =2.5 ,\
label='Model −> 1 APR − 10 JUN')
plt.plot(tf7 , fitted7 , color="chocolate", alpha =5, lw =2.5 ,\
label='Model −> 10 JUN − 10 JUL')

plt.plot(tf8 , fitted8 , color="red", alpha =5, lw =2.5 ,\
label='Model −> 10 JUL − 12 SEP')

ax1.plot( M_New ,color="black",alpha =5 ,\
lw=2, linestyle ='dotted',label='Real data')       #Plot real data
ax1.xaxis.tick_top()
ax1.yaxis.tick_right()
xcoords = [75, 115, 139, 180, 200, 275, 300, 366]
for xc in zip(xcoords ):
    plt.axvline(x=xc , color="black", linestyle ='dotted', alpha =0.5 , lw =2)
plt.set_xlabel ('Time(days)',fontweight ="bold")
plt. set_ylabel ('Active infected case',fontweight ="bold")

plt.grid(b=True , which='major', c='w', lw=2, ls='-')
legend = plt.legend(title="Population: ",loc=6, bbox_to_anchor =(1.05 ,0.2))
