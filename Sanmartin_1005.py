# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:50:23 2018

@author: ESFOT
"""

import time
print (time.localtime())

t = time.localtime()
year =   t[0]
mounth = t[1]
day =    t[2]
hora =   t[3]
minu =   t[4]
seg =    t[5]


while True:
    t = time.localtime()
    print (hora, ":", minu,":", seg)
    time.sleep(1)
