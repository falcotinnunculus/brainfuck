#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:20:50 2022

@author: Mateusz Winiarski
"""

from brainlib import bfgenerate

output = input("Enter string: ")

bfcode=bfgenerate(output)
print(bfcode)
