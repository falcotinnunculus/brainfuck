# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 03:25:26 2022

@author: Mateusz Winiarski
"""

from brainlib import bfcompile
import numpy as np

name = input("Enter file name: ")

f = open(name,"r")

bfcode = f.read()

f.close()

#%%
# wyświetlanie kodu w Pythonie i jego wykonanie

# inicjalizacja cd
cache = np.zeros(30000).astype("u1") # pamięć 256-bitowa
pointer=0 # położenie wskaźnika

pycode=bfcompile(bfcode)

print(pycode)        
exec(pycode)
    
