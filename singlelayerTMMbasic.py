# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:53:01 2019

@author: Tahmid Hassan Talukdar

Reflection spectrum for single layer pSi etch
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd 

Df = pd.read_csv('12.5mA_500nm_KOH40min.txt', sep='\t', skiprows=60, skipfooter = 200)

A = Df.values

lambdas = A[:,0]
Reflectance = A[:,1]

plt.plot(lambdas,Reflectance)

multiplier = 200;   # Use this to fit the curve to the captured spectrum to offset the intensity difference 


index = 1.85   # Predicted Index

L1 = 500    # Layer thickness


                
n = np.array([1,index,3.5])
            
            
Refl = np.zeros(1201-400)
xaxis = np.zeros(1201-400)
            
for i in range(400,1201):
                
    lambdas = i;
                
    beta1 = 2*3.1415*index/lambdas; 
    
    t01 = 2*n[0] / (n[0]+n[1])
    r01 = (n[0]-n[1])/(n[0]+n[1])
    
    t12 = 2*n[1]/(n[1]+n[2]);
    r12 = (n[1]-n[2])/(n[1]+n[2])
    
    I01 = np.array([[1/t01,r01/t01],[r01/t01,1/t01]])
    
    P1 = np.array([[np.exp(-1j*beta1*L1), 0], [0, np.exp(1j*beta1*L1)]])
    
    I12 = np.array([[1/t12,r12/t12],[r12/t12,1/t12]])
    
    T1 = np.dot(I01,P1)
    
    T = np.dot(T1,I12) 
    
    r = T[1][0]/T[0][0]
    
    R = np.abs(r)*np.abs(r)
    
    Refl[i-400] = R
    
    xaxis[i-400] = i
    


Refl = Refl*multiplier

plt.plot(xaxis,Refl, label='z')