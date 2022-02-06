#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 03:37:35 2022

@author: Mateusz Winiarski
"""

import numpy as np
from brainlib import bfcompile


bfcode = input()

    
#%%
# wyświetlanie kodu w Pythonie i jego wykonanie

# inicjalizacja
cache = np.zeros(30000).astype("u1") # pamięć 256-bitowa
pointer=0 # położenie wskaźnika

pycode=bfcompile(bfcode)

print(pycode)        
exec(pycode)
    
