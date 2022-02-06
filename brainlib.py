#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 22:24:37 2022

@author: Mateusz Winiarski
"""

import re

def bfcompile(bfcode):
    # regex dzielący wejście na fragmenty złożone z takich samych znaków
    # ze względu na działanie funkcji split() nie można go zbytnio uprościć
    regex='([\[\]]?)([+-]+)([\[\]]?)'\
        +'|([\[\]]?)([<>]+)([\[\]]?)'\
        +'|([\[\]]?)(,+|\.+)([\[\]]?)'\
        +'|([\[\]]?)([^+\-<>.,\[\]\n\r]+)([\[\]]?)'\
        +'|([\[\]])'
    bflist = list(filter(None,re.split(regex,bfcode.replace('\n',''))))
    pycode = ""
    #%%
    #inicjalizacja
    
    indent=0 # poziom tabulacji
    depth=4 # ilość spacji w jednym wcięciu
    
    #%%
    # generator kodu
    
    
    if ',' in bfcode: pycode+= 'buffer=list(input()+\'\\0\')\n' # sprawdzenie czy wystąpi input
    
            
    for i in bflist:
        tab = ' ' * depth 
        tabs = tab * indent
        
        if '+' in i or '-' in i: # uproszczenie znaków +-
            num=i.count('+')-i.count('-')
            if num>0:
                pycode+= f'{tabs}cache[pointer]+={num}\n'
            elif num<0:
                pycode+= f'{tabs}cache[pointer]-={-num}\n'
                
        elif '>' in i or '<' in i: #uproszczenie znaków <>
            num=i.count('>')-i.count('<')
            if num>0:
                pycode+= f'{tabs}pointer+={num}\n'
            elif num<0:
                pycode+= f'{tabs}pointer-={-num}\n'
                
        elif i == '.':
            pycode+= f'{tabs}print(chr(cache[pointer]),end=\'\')\n'
        elif '.' in i: # uproszczenie znaków .
            pycode+= f'{tabs}for _ in range({len(i)}):\n'
            pycode+= f'{tabs+tab}print(chr(cache[pointer]),end=\'\')\n'
            
        elif i == ',':
            pycode+= f'{tabs}cache[pointer] = ord(buffer[0])\n{tabs}buffer.pop(0)\n'
        elif ',' in i: # uproszczenie znaków ,
            pycode+= f'{tabs}for _ in range({len(i)}):\n'
            pycode+= f'{tabs+tab}cache[pointer] = ord(buffer[0])\n{tabs+tab}buffer.pop(0)\n'
            
        elif i == '[':
            pycode+= f'{tabs}while cache[pointer]:\n'
            indent+=1
        elif i == ']':
            indent-=1
            
        elif i not in [' ','\n']:
            pycode+= '# {}\n'.format(i.strip().strip("\n"))
            
        if indent<0: # błąd gdy użyto więcej ] niż [
            raise SyntaxError("missing '['")
    
    if indent > 0: # błąd gdy użyto więcej [ niż ]
        raise SyntaxError("missing ']'")
        
    return pycode

#%%

def bfgenerate(output):
    prev = 0
    bfcode = ""
    
    for i in list(output):
        this = ord(i)
        diff = this - prev
        if diff>10:
            bfcode+= ('+' * (diff//10))+'[>'+('+' * 10)+'<-]>'+('+' * (diff%10))+'.<'
        elif diff>0:
            bfcode+= '>'+('+' * (diff))+'.<'
        elif diff<-10:
            bfcode+= ('+' * (-diff//10))+'[>'+('-' * 10)+'<-]>'+('-' * (-diff%10))+'.<'
        elif diff<0:
            bfcode+= '>'+('-' * (-diff))+'.<'
        elif diff==0:
            bfcode+= '>.<'
        prev = this
        
    if bfcode[-1]=='<': bfcode=bfcode[:-1]
    return bfcode.replace('<>','')