# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:46:45 2014

@author: asutherland
"""

## compare function
###### a compare function that returns 1 if x>y, 0 if x == y, and -1 if x<y

def compare(x,y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0 
        
print compare(2,4) 

