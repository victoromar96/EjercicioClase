# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:17:38 2018

@author: ESFOT
"""

import time 
print (time.localtime())
t=time.localtime()
year = t[0]
month =t[1]
hora = t[3]
minutos = t[4]
segundos = t[5]
print(year)
print(month)
print('la hora es')
print(hora,':',minutos,segundos)


for x in range(1,61):
    print(x)

for x in range(1,61):
    print(x)
    time.sleep(1)
    
