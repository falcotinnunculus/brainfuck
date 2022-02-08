#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 03:47:14 2022

@author: Mateusz Winiarski
"""

from brainlib import bfgenerate

output = input("Enter string: ")


bfcode=bfgenerate(output)

name = input("Enter file name: ")

f = open(name,"w")
f.write(bfcode)
f.close()
