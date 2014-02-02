# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/asutherland/.spyder2/.temp.py
"""

    
# creating a grid 
def duplicate(thing):
    thing()
    thing()
    
def double_duplicate():
    duplicate(thing)
    duplicate(thing)
  
def print_OneSide():
    print '/    '
    
def print_OneTop():
    print '+----'
    
def print_TwoSides():
    duplicate(print_OneSide)
    
def print_TwoTops():
    duplicate(print_OneTop)
    
def print_OneRow():
    print_TwoTops()
    double_duplicate(print_TwoSides)
    
def print_grid():
    duplicate(print_OneRow)
    print_TwoSides

print_grid()

    
