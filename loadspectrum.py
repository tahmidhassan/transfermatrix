# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:25:38 2019

@author: Tahmid
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:38:01 2019

Transmission Spectrum captured through Newport Meter / SANTEC TSL-510

@author: Tahmid Hassan Talukdar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

Df = pd.read_csv('Sample3_ outer side.txt', sep='\t')

A = Df.values

lambdas = A[:,0]
Reflectance = A[:,1]

plt.plot(lambdas,Reflectance)