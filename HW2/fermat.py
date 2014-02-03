# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/asutherland/.spyder2/.temp.py
"""

## Fermat's Last Theorem 

def check_fermat(a,b,c,n):
    
    if a**(n)+b**(n)==c**(n) and n>2:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work" 
    
if __name__=='__main__':
    a = 1
    b = 2
    c = 3
    n = 3
    print check_fermat(a,b,c,n)